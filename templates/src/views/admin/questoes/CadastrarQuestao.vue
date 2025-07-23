<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type DisciplinaI from '@/interfaces/Disciplina'
import type QuestaoI from '@/interfaces/Questao'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const disciplinas = ref<DisciplinaI[]>([])
const router = useRouter()
const questao = ref<QuestaoI>({ enunciado: '', disciplina_id: 0 })
const imagens = ref<File[]>([])
const mensagemStore = useMensagemStore()

axios
  .get(`${apiUrl}/disciplinas/`)
  .then((result) => (disciplinas.value = result.data.disciplinas))
  .catch((erro) => router.push(`/admin/erro/${erro}`))

function adicionarImagem(event: Event): void {
  const imagemElement = event.target as HTMLInputElement
  if (imagemElement.files) {
    const imagem = imagemElement.files[0]
    questao.value.enunciado += '\n\n@image=' + imagem.name + '\n\n'
    imagens.value.push(imagem)
  }
}

function inserir(): void {
  axios
    .post(`${apiUrl}/questoes/`, questao.value)
    .then((result) => {
      mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' })
      router.push(`/admin/questoes/detalhe/${result.data.id}`)
    })
    .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
  const formData = new FormData()
  imagens.value.forEach((imagem) => formData.append('imagens', imagem))
  axios
    .post(`${apiUrl}/upload/`, formData, { headers: { 'Content-type': 'multipart/form-data' } })
    .then((result) => console.log(result.data))
    .catch((erro) => console.log(erro.response.data))
}
</script>

<template>
  <h1>Cadastro de Questões</h1>
  <form @submit.prevent="inserir()">
    <div class="row">
      <label for="disciplina">Disciplina</label>
      <select name="disciplina_id" id="disciplina" v-model="questao.disciplina_id">
        <option value="0"></option>
        <option v-for="disciplina in disciplinas" :key="disciplina.id" :value="disciplina.id">
          {{ disciplina.nome }}
        </option>
      </select>
    </div>
    <label for="enunciado" class="label-for-textarea">Enunciado</label>
    <textarea
      name="enunciado"
      id="enunciado"
      rows="20"
      cols="80"
      v-model="questao.enunciado"
    ></textarea>
    <div class="row">
      <label for="imagem" class="label-for-file-input">Adicione uma imagem</label>
      <input
        type="file"
        name="imagem"
        id="imagem"
        accept="image/png,image/jpeg,image/jpg"
        @change="adicionarImagem"
      />
    </div>
    <table v-if="imagens.length > 0">
      <thead>
        <tr>
          <td>Imagens Selecionadas</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="imagem in imagens" :key="imagem.name">
          <td>{{ imagem.name }}</td>
        </tr>
      </tbody>
    </table>
    <button type="submit">Cadastrar</button>
  </form>
</template>

<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type DisciplinaI from '@/interfaces/Disciplina'
import type QuestaoI from '@/interfaces/Questao'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const questao = ref<QuestaoI | null>(null)
const disciplinas = ref<DisciplinaI[]>([])
const imagens = ref<File[]>([])
const mensagemStore = useMensagemStore()
const route = useRoute()
const router = useRouter()

axios
  .get(`${apiUrl}/questoes/${route.params.id}`)
  .then((result) => (questao.value = result.data.questao))
  .catch((erro) => router.push(`/erro/${erro.response.data}`))

axios
  .get(`${apiUrl}/disciplinas/`)
  .then((result) => (disciplinas.value = result.data.disciplinas))
  .catch((erro) => router.push(`/erro/${erro.response.data}`))

function adicionarImagem(event: Event): void {
  const imagemElement = event.target as HTMLInputElement
  if (imagemElement.files && questao.value) {
    const imagem = imagemElement.files[0]
    questao.value.enunciado += '\n\n@image=' + imagem.name + '\n\n'
    imagens.value.push(imagem)
    const formData = new FormData()
    imagens.value.forEach((imagem) => formData.append('imagens', imagem))
    axios
      .post(`${apiUrl}/upload/`, formData, { headers: { 'Content-type': 'multipart/form-data' } })
      .then((result) => console.log(result.data))
      .catch((erro) => console.log(erro.response.data))
  }
}

function atualizar(): void {
  if (questao.value && questao.value.id) {
    questao.value.valida = undefined
    questao.value.disciplina = undefined
    axios
      .put(`${apiUrl}/questoes/${questao.value.id}`, questao.value)
      .then((result) => mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' }))
      .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
      .finally(() => router.push(`/admin/questoes/detalhe/${questao.value?.id}`))
  }
}
</script>

<template>
  <h1>Edição de Questão</h1>
  <form @submit.prevent="atualizar()">
    <div class="row">
      <label for="disciplina">Disciplina</label>
      <select v-if="questao" name="disciplina_id" id="disciplina" v-model="questao.disciplina_id">
        <option :value="questao.disciplina_id" disable>{{ questao.disciplina?.nome }}</option>
        <option v-for="disciplina in disciplinas" :key="disciplina.id" :value="disciplina.id">
          {{ disciplina.nome }}
        </option>
      </select>
    </div>
    <label for="enunciado" class="label-for-textarea">Enunciado</label>
    <textarea
      v-if="questao"
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
    <button type="submit">Atualizar</button>
  </form>
</template>

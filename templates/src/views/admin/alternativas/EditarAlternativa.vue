<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type AlternativaI from '@/interfaces/Alternativa'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const alternativa = ref<AlternativaI | null>(null)
const imagens = ref<File[]>([])
const route = useRoute()
const router = useRouter()
const mensagemStore = useMensagemStore()

axios
  .get(`${apiUrl}/alternativas/${route.params.id}`)
  .then((result) => (alternativa.value = result.data.alternativa))
  .catch((erro) => router.push(`/admin/erro/${erro.response.data.erro}`))

function adicionarImagem(event: Event): void {
  const imagemElement = event.target as HTMLInputElement
  if (imagemElement.files && alternativa.value) {
    const imagem = imagemElement.files[0]
    alternativa.value.texto += '@image=' + imagem.name
    imagens.value.push(imagem)
  }
}

function mostrarQuestao(): void {
  if (alternativa.value) {
    router.push(`/admin/questoes/detalhe/${alternativa.value.questao_id}`)
  }
}

function atualizar(): void {
  if (alternativa.value && alternativa.value.id) {
    axios
      .patch(`${apiUrl}/alternativas/${alternativa.value.id}`, alternativa.value)
      .then((result) => mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' }))
      .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
      .finally(() => router.push(`/admin/questoes/detalhe/${alternativa.value?.questao_id}`))
  }
}
</script>

<template>
  <h1>Edição de Alternativa</h1>
  <form v-if="alternativa" @submit.prevent="atualizar()">
    <div class="row">
      <label for="texto">Texto</label>
      <textarea
        name="texto"
        id="texto"
        rows="2"
        cols="60"
        v-model="alternativa.texto"
        autofocus
        required
      ></textarea>
    </div>
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
    <div class="row">
      <label for="correta">Correta?</label>
      <select name="correta" id="correta" v-model="alternativa.correta">
        <option :value="false">Não</option>
        <option :value="true">Sim</option>
      </select>
    </div>
    <div class="row">
      <label for="justificativa">Justificativa</label>
      <textarea
        name="justificativa"
        id="justificativa"
        rows="2"
        cols="60"
        v-model="alternativa.justificativa"
      ></textarea>
    </div>
    <button>Atualizar</button>
  </form>
  <button @click="mostrarQuestao()">Mostrar Questão</button>
</template>

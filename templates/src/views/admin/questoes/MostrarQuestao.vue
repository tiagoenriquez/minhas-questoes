<script setup lang="ts">
import TextoComponent from '@/components/TextoComponent.vue'
import apiUrl from '@/connections/ApiConnection'
import type QuestaoI from '@/interfaces/Questao'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ListarAlternativas from '../alternativas/ListarAlternativas.vue'

const questao = ref<QuestaoI | null>(null)
const route = useRoute()
const router = useRouter()
const mensagemStore = useMensagemStore()

function obter(): void {
  axios
    .get(`${apiUrl}/questoes/${route.params.id}`)
    .then((result) => (questao.value = result.data.questao))
    .catch((erro) => router.push(`/admin/erro/${erro.response.data.erro}`))
}

obter()

function editar(): void {
  if (questao.value && questao.value.id) {
    router.push(`/admin/questoes/edicao/${questao.value.id}`)
  }
}

function excluir(): void {
  if (questao.value && questao.value.id) {
    axios
      .delete(`${apiUrl}/questoes/${questao.value.id}`)
      .then((result) => {
        mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' })
        router.push('/admin/questoes/procura')
      })
      .catch((erro) => router.push(`/admin/erro/${erro.response.data.erro}`))
  }
}

function adicionarAlternativa(): void {
  if (questao.value && questao.value.id) {
    router.push(`/admin/alternativas/cadastro/${questao.value.id}`)
  }
}

function excluirAlternativa(id: number | undefined): void {
  axios
    .delete(`${apiUrl}/alternativas/${id}`)
    .then((result) => mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' }))
    .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
    .finally(() => obter())
}
</script>

<template>
  <h1>Detalhes de Questão</h1>
  <form v-if="questao">
    <div v-if="questao.valida" class="sucesso">
      <p>Questão válida</p>
    </div>
    <div v-else class="erro">
      <p>Questão inválida</p>
    </div>
    <div v-if="questao.disciplina" class="row">
      <label for="disciplina">Disciplina</label>
      <input
        type="text"
        name="disciplina"
        id="disciplina"
        v-model="questao.disciplina.nome"
        readonly
      />
    </div>
    <TextoComponent :texto="questao.enunciado" classe="enunciado" />
  </form>
  <ListarAlternativas
    v-if="questao && questao.alternativas"
    :alternativas="questao.alternativas"
    @excluir="excluirAlternativa"
  />
  <div class="row">
    <button @click="editar()">Editar</button>
    <button @click="adicionarAlternativa()">Adicionar Alternativa</button>
    <button @click="excluir()">Excluir</button>
  </div>
</template>

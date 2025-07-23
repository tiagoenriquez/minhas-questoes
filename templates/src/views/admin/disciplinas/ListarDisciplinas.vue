<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type DisciplinaI from '@/interfaces/Disciplina'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const disciplinas = ref<DisciplinaI[]>([])
const router = useRouter()
const mensagemStore = useMensagemStore()

function listar(): void {
  axios
    .get(`${apiUrl}/disciplinas/`)
    .then((result) => (disciplinas.value = result.data.disciplinas))
    .catch((erro) => router.push(`/admin/erro/${erro}`))
}

listar()

function editar(id: number | undefined): void {
  if (id) {
    router.push(`/admin/disciplinas/edicao/${id}`)
  }
}

function excluir(id: number | undefined): void {
  if (id) {
    axios
      .delete(`${apiUrl}/disciplinas/${id}`)
      .then((result) => mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' }))
      .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
      .finally(() => listar())
  }
}
</script>

<template>
  <h1>Lista de Disciplinas</h1>
  <table>
    <thead>
      <tr>
        <th>Nome</th>
        <th colspan="2"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="disciplina in disciplinas" :key="disciplina.id">
        <td>{{ disciplina.nome }}</td>
        <td>
          <button @click="editar(disciplina.id)">Editar</button>
        </td>
        <td>
          <button @click="excluir(disciplina.id)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

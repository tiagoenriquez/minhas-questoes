<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type QuestaoI from '@/interfaces/Questao'
import axios from 'axios'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const questoes = ref<QuestaoI[]>([])
const route = useRoute()
const router = useRouter()

axios
  .get(`${apiUrl}/questoes/lista/${route.params.trecho}`)
  .then((result) => (questoes.value = result.data.questoes))
  .catch((erro) => router.push(`/admin/erro/${erro.response.data.erro}`))

function limitarEnunciado(enunciado: string): string {
  if (enunciado.length < 80) {
    return enunciado
  }
  return `${enunciado.substring(0, 80)} [...]`
}

function mostrar(id: number | undefined): void {
  if (id) {
    router.push(`/admin/questoes/detalhe/${id}`)
  }
}
</script>

<template>
  <h1>Lista de Questões</h1>
  <table>
    <thead>
      <tr>
        <th>Questão</th>
        <th>Disciplina</th>
        <th>Válida</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="questao in questoes" :key="questao.id">
        <td>{{ limitarEnunciado(questao.enunciado) }}</td>
        <td>{{ questao.disciplina?.nome }}</td>
        <td v-if="questao.valida">
          <div class="sucesso">V</div>
        </td>
        <td v-else>
          <div class="erro">X</div>
        </td>
        <td>
          <button @click="mostrar(questao.id)">Mostrar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

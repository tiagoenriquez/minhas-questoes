<script setup lang="ts">
import { useProvaStore } from '@/stores/prova'
import { useRouter } from 'vue-router'

const provaStore = useProvaStore()
const router = useRouter()

function mostrarQuestao(numero: number): void {
  router.push(`/prova/detalhes-da-questao/${numero}`)
}
</script>

<template>
  <div v-if="provaStore.prova" class="column">
    <h1>Questões Respondidas</h1>
    <table>
      <tbody>
        <tr v-for="questao in provaStore.prova.questoesRespondidas()" :key="questao.numero">
          <td>Questão {{ questao.numero }}</td>
          <td v-if="questao.acertada">
            <div class="sucesso questao-acertada">V</div>
          </td>
          <td v-else>
            <div class="erro questao-acertada">X</div>
          </td>
          <td>
            <button @click="mostrarQuestao(questao.numero)">Detalhes</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { mostrarNumero } from '@/adapters/NumeroAdapter'
import { useProvaStore } from '@/stores/prova'

const provaStore = useProvaStore()
</script>

<template>
  <div v-if="provaStore.prova" class="column">
    <h1>Desempenho</h1>
    <table>
      <tbody>
        <tr>
          <td>Nº de questões</td>
          <td>{{ provaStore.prova.questoes.length }}</td>
        </tr>
        <tr>
          <td>Nº de questões respondidas</td>
          <td>{{ provaStore.prova.questoesRespondidas().length }}</td>
        </tr>
        <tr>
          <td>Nº de questões acertadas</td>
          <td>{{ provaStore.prova.questoesAcertadas() }}</td>
        </tr>
        <tr>
          <td>Nº de questões erradas</td>
          <td>{{ provaStore.prova.questoesErradas() }}</td>
        </tr>
        <tr>
          <td>Nota</td>
          <td>{{ mostrarNumero(provaStore.prova.nota()) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

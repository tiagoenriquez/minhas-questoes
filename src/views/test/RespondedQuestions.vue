<script setup lang="js">
import TestMenu from '@/components/TestMenu.vue';
import router from '@/router';
import store from '@/store';

const test = store.state.test;
const respondeds = test.questions.filter(question => question.responded);

function showDetails(id) {
  router.push(`/prova/detalhes-de-questao/${id}`);
}
</script>

<template>
  <TestMenu />
  <main>
    <h1>Questões Respondidas</h1>
    <table>
      <tbody>
        <tr v-for="question in respondeds" :key="question.id">
          <td>Questão {{ question.number }}</td>
          <td :class="question.correct ? 'correct' : 'wrong'">
            {{ question.correct ? 'Certo' : 'Errado' }}
          </td>
          <td>
            <button @click="() => showDetails(question.number - 1)">Detalhes</button>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>
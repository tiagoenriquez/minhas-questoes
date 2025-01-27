<script setup lang="js">
import TestMenu from '@/components/TestMenu.vue';
import store from '@/store';

const test = store.state.test;
let corrects = 0;
let respondeds = 0;

test.questions.forEach(question => {
  if (question.correct) corrects++;
  if (question.responded) respondeds++;
});
</script>

<template>
  <TestMenu />
  <main>
    <h1>Desempenho</h1>
    <table>
      <tbody>
        <tr>
          <td>Questões cadastradas</td>
          <td>{{ test.questions.length }}</td>
        </tr>
        <tr>
          <td>Questões respondidas</td>
          <td>{{ respondeds }}</td>
        </tr>
        <tr>
          <td>Questões acertadas</td>
          <td>{{ corrects }}</td>
        </tr>
        <tr>
          <td>Questões erradas</td>
          <td>{{ respondeds - corrects }}</td>
        </tr>
        <tr>
          <td>Nota</td>
          <td>{{ test.grade.toFixed(1).replace('.', ',') }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>
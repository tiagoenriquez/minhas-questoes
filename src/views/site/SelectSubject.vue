<script setup lang="js">
import { ref } from 'vue';
import AdminMenu from '@/components/AdminMenu.vue';
import { apiUrl, axios } from '@/connections/apiConnection';
import router from '@/router';
import store from '@/store';

const subjects = ref([]);

axios.get(`${apiUrl}/subjects/with-n-questions`).then(result => {
  subjects.value = result.data;
  result.data.forEach((instance, index) => {
    if (instance.n_questions > 1) {
      subjects.value[index].questions = 'questões';
    } else {
      subjects.value[index].questions = 'questão';
    }
  });
});

function select(id) {
  axios.post(`${apiUrl}/tests/${id}`).then(result => {
    const test = result.data;
    test.questions.forEach((question, index) => question.number = index + 1);
    store.commit('setTest', test);
    router.push('/prova/proxima-questao');
  }).catch(error => {
    store.commit('setError', error);
    router.push('/erro');
  });
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Selecione uma disciplina</h1>
    <select>
      <option value=""></option>
      <option v-for="subject in subjects" :key="subject.id" :value="subject.id" @click="() => select(subject.id)">
        {{ subject.name }} - {{ subject.n_questions }} {{ subject.questions }}
      </option>
    </select>
  </main>
</template>

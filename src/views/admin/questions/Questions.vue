<script setup lang="js">
import { ref } from 'vue';
import AdminMenu from '@/components/AdminMenu.vue';
import { apiUrl, axios } from '@/connections/apiConnection';
import store from '@/store';
import router from '@/router';
import { useRoute } from 'vue-router';

const route = useRoute()
const excerpt = route.params.excerpt;
const questions = ref([]);

axios.get(`${apiUrl}/questions`, { params: { trecho: excerpt } }).then(result => {
  questions.value = result.data;
  if (!questions.value.length) throw new Error('Não há questão cadastrada com o trecho informado.');
}).catch(error => {
  store.commit('setError', error.message);
  router.push('/erro');
});

function edit(id) {
  router.push(`/questao/edicao/${id}`)
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Questões encontradas</h1>
    <table>
      <thead>
        <tr>
          <th>Enunciado</th><th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="question in questions" :key="question.id">
          <td>{{ question.statement.substring(0, 128) }} [...]</td>
          <td>
            <button @click="() => edit(question.id)">Atualizar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>
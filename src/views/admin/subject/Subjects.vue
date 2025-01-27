<script setup lang="js">
import router from '@/router';
import { ref } from 'vue';
import AdminMenu from '@/components/AdminMenu.vue';
import MessageComponent from '@/components/MessageComponent.vue';
import store from '@/store';
import { apiUrl, axios } from '@/connections/apiConnection';

const subjects = ref([]);
const error = ref('');
const success = ref('');

axios.get(`${apiUrl}/subjects/`).then((result => {
  subjects.value = result.data;
  if (subjects.value.length === 0) throw new Error('Não há disciplina cadastrada.');
})).catch(error => {
  store.commit('setError', error.message);
  router.push('/erro');
});

function edit(id) {
  router.push(`edicao/${id}`);
}

function destroy(id) {
  axios.delete(`${apiUrl}/subjects/${id}`).then(result => {
    window.location.reload();
  }).catch(err => {
    error.value = err.response.data
  });
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Disciplinas</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <table>
      <thead>
        <tr>
          <th>Nome</th><th></th><th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subject in subjects" :key="subject.id">
          <td>{{ subject.name }}</td>
          <td>
            <button @click="() => edit(subject.id)">Atualizar</button>
          </td>
          <td>
            <button @click="() => destroy(subject.id)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>
<script setup lang="js">
import { reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import AdminMenu from '@/components/AdminMenu.vue';
import MessageComponent from '@/components/MessageComponent.vue';
import { apiUrl, axios } from '@/connections/apiConnection.js';

const route = useRoute();
const subject = reactive({ id: null, name: '' });
const error = ref('');
const success = ref('');

axios.get(`${apiUrl}/subjects/${route.params.id}`).then(result => {
  Object.keys(subject).forEach(key => subject[key] = result.data[key]);
});

function update() {
  axios.defaults.headers.common['Content-Type'] = 'application/json';
  axios.put(`${apiUrl}/subjects/${subject.id}`, subject)
    .then(result => success.value = result.data)
    .catch(err => error.value = err.response.data);
}
</script>

<template>
  <AdminMenu />
  <main v-if="subject">
    <h1>Edição de Disciplina</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <div class="row">
      <label for="name">Nome</label>
      <input type="text" id="name" v-model="subject.name" autofocus />
    </div>
    <button @click="update()">Salvar</button>
  </main>
</template>
<script setup lang="js">
import { ref } from 'vue';
import AdminMenu from '@/components/AdminMenu.vue';
import MessageComponent from '@/components/MessageComponent.vue';
import { apiUrl, axios } from '@/connections/apiConnection';

const name = defineModel('name');
const error = ref('');
const success = ref('');

function insert() {
  axios.defaults.headers.common['Content-Type'] = 'application/json';
  axios.post(`${apiUrl}/subjects/`, { name: name.value }, )
    .then(result => success.value = result.data)
    .catch(err => error.value = err.response.data);
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Cadastro de Disciplina</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <div class="row">
      <label for="name">Nome</label>
      <input type="text" v-model="name" autofocus />
    </div>
    <button @click="insert()">Salvar</button>
  </main>
</template>
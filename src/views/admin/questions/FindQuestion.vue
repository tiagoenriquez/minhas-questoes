<script setup lang="js">
import AdminMenu from '@/components/AdminMenu.vue';
import router from '@/router';
import { ref } from 'vue';

const trecho = ref('');

function find() {
  router.push({ name: 'questions', params: { excerpt: trecho.value } })
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Procurar Questão</h1>
    <div class="row">
      <label for="excerpt">Digite um trecho</label>
      <input type="text" id="excerpt" v-model="trecho" autofocus/>
    </div>
    <button @click="find()">Procurar</button>
  </main>
</template>
<script setup lang="js">
import AdminMenu from '@/components/AdminMenu.vue';
import store from '@/store';
import { ref } from 'vue';

const error = ref(store.state.error);
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Erro: {{ error }}</h1>
  </main>
</template>
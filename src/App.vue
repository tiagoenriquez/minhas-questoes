<script setup>
import { RouterView } from 'vue-router'
import store from './store';
import { ref } from 'vue';

const error = ref('');
error.value = store.state.error;
</script>

<template>
  <RouterView />
</template>
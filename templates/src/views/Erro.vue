<script setup lang="ts">
import { useRoute } from 'vue-router'

const erro = useRoute().params.erro
</script>

<template>
  <h1>Erro: {{ erro }}</h1>
</template>

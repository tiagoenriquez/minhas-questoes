<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <nav>
    <a href="/">Sair</a>
    <button @click="router.push('/prova/proxima-questao')">Próxima Questão</button>
    <button @click="router.push('/prova/questoes-respondidas')">Questões Respondidas</button>
    <button @click="router.push('/prova/desempenho')">Desempenho</button>
  </nav>
</template>

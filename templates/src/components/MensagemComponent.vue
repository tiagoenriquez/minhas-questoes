<script setup lang="ts">
import { useMensagemStore } from '@/stores/mensagem'

const mensagemStore = useMensagemStore()

function limparMensagem(): void {
  mensagemStore.excluirMensagem()
}
</script>

<template>
  <section v-if="mensagemStore.mensagem" :class="mensagemStore.mensagem.tipo">
    <p>{{ mensagemStore.mensagem.texto }}</p>
    <button @click="limparMensagem()">X</button>
  </section>
</template>

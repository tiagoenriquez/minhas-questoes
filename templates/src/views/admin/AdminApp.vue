<script setup lang="ts">
import AdminMenu from './AdminMenu.vue'
import { RouterView } from 'vue-router'
import MensagemComponent from '@/components/MensagemComponent.vue'
</script>

<template>
  <header>
    <AdminMenu />
  </header>
  <main>
    <MensagemComponent />
    <RouterView />
  </main>
</template>

<script setup lang="ts">
import MensagemComponent from '@/components/MensagemComponent.vue'
import SiteMenu from './SiteMenu.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <SiteMenu />
  </header>
  <MensagemComponent />
  <main>
    <RouterView />
  </main>
</template>

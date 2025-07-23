<script setup lang="ts">
import TextoComponent from '@/components/TextoComponent.vue'
import type AlternativaI from '@/interfaces/Alternativa'
import { useRouter } from 'vue-router'

const props = defineProps<{ alternativas: AlternativaI[] }>()
const router = useRouter()

function editar(id: number | undefined): void {
  if (id) {
    router.push(`/admin/alternativas/edicao/${id}`)
  }
}
</script>

<template>
  <div class="row alternativa" v-for="alternativa in alternativas" :key="alternativa.id">
    <input type="radio" :id="`alternativa-${alternativa.id}`" :checked="alternativa.correta" />
    <label :for="`alternativa-${alternativa.id}`" class="label-for-radio">
      <TextoComponent :texto="alternativa.texto" classe="alternativa" />
    </label>
    <button @click="editar(alternativa.id)">Atualizar</button>
    <button @click="$emit('excluir', alternativa.id)">Excluir</button>
  </div>
</template>

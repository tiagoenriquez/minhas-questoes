<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type Paragrafo from '@/interfaces/Paragrafo'

const props = defineProps<{ texto: string | undefined; classe: string }>()

const paragrafos: Paragrafo[] = props.texto
  ? props.texto.split('\n').map((paragrafo, indice) => ({ id: indice, texto: paragrafo }))
  : []

function eImagem(paragrafo: string): boolean {
  return paragrafo.startsWith('@image=')
}

function obterNomeDeImagem(paragrafo: string): string {
  const nome = paragrafo.replace('@image=', '')
  return `${apiUrl}/upload/${nome}`
}
</script>

<template>
  <div :class="classe" v-for="paragrafo in paragrafos" :key="paragrafo.id">
    <img
      v-if="eImagem(paragrafo.texto)"
      :src="obterNomeDeImagem(paragrafo.texto)"
      alt="Não foi possível obter a imagem."
    />
    <p v-else>{{ paragrafo.texto }}</p>
  </div>
</template>

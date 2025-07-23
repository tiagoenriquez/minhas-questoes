<script setup lang="ts">
import TextoComponent from '@/components/TextoComponent.vue'
import { useProvaStore } from '@/stores/prova'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const provaStore = useProvaStore()
const route = useRoute()
const questao = computed(() => provaStore.prova?.procurarQuestao(Number(route.params.numero)))
</script>

<template>
  <div v-if="questao" class="column">
    <h1>Questão {{ questao.numero }}</h1>
    <TextoComponent :texto="questao.enunciado" classe="enunciado" />
    <h2>Alternativas</h2>
    <div v-for="alternativa in questao.alternativas" :key="alternativa.id" class="column">
      <div v-if="alternativa.correta && alternativa.selecionada" class="alternativa-acertada">
        <p class="justificativa">Resposta correta: {{ alternativa.justificativa }}</p>
        <TextoComponent :texto="alternativa.texto" classe="enunciado" />
      </div>
      <div v-else-if="!alternativa.correta && alternativa.selecionada" class="alternativa-errada">
        <p class="justificativa">Resposta incorreta: {{ alternativa.justificativa }}</p>
        <TextoComponent :texto="alternativa.texto" classe="enunciado" />
      </div>
      <div v-else-if="alternativa.correta && !alternativa.selecionada" class="alternativa-correta">
        <p class="justificativa">Resposta correta: {{ alternativa.justificativa }}</p>
        <TextoComponent :texto="alternativa.texto" classe="enunciado" />
      </div>
      <TextoComponent v-else :texto="alternativa.texto" classe="enunciado" />
    </div>
  </div>
</template>

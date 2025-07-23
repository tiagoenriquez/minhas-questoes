<script setup lang="ts">
import { mostrarNumero } from '@/adapters/NumeroAdapter'
import TextoComponent from '@/components/TextoComponent.vue'
import { useProvaStore } from '@/stores/prova'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'

const provaStore = useProvaStore()
const questao = computed(() => provaStore.prova?.proximaQuestao())
const selecionadaId = ref<number | null>(null)
const router = useRouter()

if (!questao.value && provaStore.prova) {
  router.push('/prova/desempenho')
}

if (!questao.value && !provaStore.prova) {
  router.push('/')
}

function selecionar(alternativaId: number) {
  selecionadaId.value = alternativaId
}

function responder() {
  if (provaStore.prova && provaStore.prova.proximaQuestao() && selecionadaId.value) {
    provaStore.prova.proximaQuestao()?.responder(selecionadaId.value)
  }
  if (provaStore.prova && !provaStore.prova.proximaQuestao()) {
    router.push('/prova/desempenho')
  }
}
</script>

<template>
  <div v-if="provaStore.prova && questao" class="column">
    <button>Nota: {{ mostrarNumero(provaStore.prova.nota()) }}</button>
    <h1>Questão {{ questao.numero }}</h1>
    <TextoComponent
      v-if="questao"
      :texto="questao.enunciado"
      :key="questao.numero"
      classe="enunciado"
    />
    <form @submit.prevent="responder()">
      <div
        class="row alternativa"
        v-for="alternativa in questao.alternativas"
        :key="alternativa.id"
      >
        <input
          type="radio"
          name="alternativa"
          :id="`alternativa-${alternativa.id}`"
          @change="selecionar(alternativa.id)"
        />
        <label :for="`alternativa-${alternativa.id}`" class="label-for-radio">
          <TextoComponent :texto="alternativa.texto" classe="alternativa" />
        </label>
      </div>
      <button type="submit">Responder Questão</button>
    </form>
  </div>
</template>

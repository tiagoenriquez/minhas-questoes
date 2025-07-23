<script setup lang="ts">
import { useMensagemStore } from '@/stores/mensagem'
import AdminMenu from './admin/AdminMenu.vue'
import { ref } from 'vue'
import type DisciplinaI from '@/interfaces/Disciplina'
import type QuestaoI from '@/interfaces/Questao'
import axios from 'axios'
import apiUrl from '@/connections/ApiConnection'
import { useRouter } from 'vue-router'
import { useProvaStore } from '@/stores/prova'
import Questao from '@/models/Questao'

const mensagem = useMensagemStore().mensagem
const disciplinas = ref<DisciplinaI[]>([])
const disciplina_id = ref<number>(0)
const router = useRouter()
const provaStore = useProvaStore()

axios
  .get(`${apiUrl}/disciplinas/ordenadas-por-n-questoes`)
  .then((result) => (disciplinas.value = result.data.disciplinas))
  .catch((erro) => router.push(`/admin/erro/${erro}`))

async function gerarProva(): Promise<void> {
  const questoes: Questao[] = await axios
    .get(`${apiUrl}/questoes/sorteio/${disciplina_id.value}`)
    .then((result) =>
      result.data.questoes.map((questao: QuestaoI, index: number) =>
        questao.alternativas ? new Questao(index + 1, questao) : null,
      ),
    )
  provaStore.criar(questoes)
  router.push('/prova/proxima-questao')
}
</script>

<template>
  <header>
    <AdminMenu />
  </header>
  <main>
    <form @submit.prevent="gerarProva()">
      <section v-if="mensagem" :class="mensagem.tipo">{{ mensagem.texto }}</section>
      <h1>Selecione uma Disciplina</h1>
      <select
        v-if="disciplinas.length > 0"
        name="disciplina_id"
        id="disciplina"
        v-model="disciplina_id"
      >
        <option value="0"></option>
        <option v-for="disciplina in disciplinas" :key="disciplina.id" :value="disciplina.id">
          {{ disciplina.nome }}: {{ disciplina.n_questoes }} questoes
        </option>
      </select>
      <button>Resolver Questões</button>
    </form>
  </main>
</template>

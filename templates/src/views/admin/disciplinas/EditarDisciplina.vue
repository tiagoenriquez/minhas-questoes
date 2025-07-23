<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type DisciplinaI from '@/interfaces/Disciplina'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const disciplina = ref<DisciplinaI | null>(null)
const mensagemStore = useMensagemStore()
const router = useRouter()

axios
  .get(`${apiUrl}/disciplinas/${route.params.id}`)
  .then((result) => (disciplina.value = result.data.disciplina))
  .catch((erro) => erro.response.data.erro)

function atualizar(): void {
  if (disciplina.value && disciplina.value.id) {
    disciplina.value.n_questoes = undefined
    axios
      .put(`${apiUrl}/disciplinas/${disciplina.value.id}`, disciplina.value)
      .then((result) => {
        mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' })
        router.push('/admin/disciplinas/lista')
      })
      .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
  }
}
</script>

<template>
  <h1>Edição de Disciplina</h1>
  <form @submit.prevent="atualizar()">
    <div class="row">
      <label for="nome">Nome</label>
      <input
        type="text"
        name="nome"
        id="nome"
        v-if="disciplina"
        v-model="disciplina.nome"
        autofocus
        required
      />
    </div>
    <button type="submit">Atualizar</button>
  </form>
</template>

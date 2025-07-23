<script setup lang="ts">
import apiUrl from '@/connections/ApiConnection'
import type DisciplinaI from '@/interfaces/Disciplina'
import { useMensagemStore } from '@/stores/mensagem'
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const disciplina = ref<DisciplinaI>({ nome: '' })
const mensagemStore = useMensagemStore()
const router = useRouter()

function inserir(): void {
  axios
    .post(`${apiUrl}/disciplinas/`, disciplina.value)
    .then((result) => {
      mensagemStore.setMensagem({ texto: result.data.mensagem, tipo: 'sucesso' })
      router.push('/admin/disciplinas/lista')
    })
    .catch((erro) => mensagemStore.setMensagem({ texto: erro.response.data.erro, tipo: 'erro' }))
}
</script>

<template>
  <h1>Cadastro de Disciplina</h1>
  <form @submit.prevent="inserir">
    <div class="row">
      <label for="nome">Nome</label>
      <input type="text" name="nome" id="nome" v-model="disciplina.nome" autofocus required />
    </div>
    <button type="submit">Cadastrar</button>
  </form>
</template>

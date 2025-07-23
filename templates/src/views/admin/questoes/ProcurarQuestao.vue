<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const trecho = ref('')
const router = useRouter()

function listar() {
  router.push(`/admin/questoes/lista/${trecho.value}`)
}
</script>

<template>
  <h1>Procurar Questão</h1>
  <form @submit.prevent="listar()">
    <div class="row">
      <label for="trecho">Trecho</label>
      <input type="text" name="trecho" id="trecho" v-model="trecho" autofocus required />
    </div>
    <button>Procurar</button>
  </form>
</template>

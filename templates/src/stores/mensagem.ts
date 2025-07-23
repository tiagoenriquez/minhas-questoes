import { ref } from 'vue'
import { defineStore } from 'pinia'
import type Mensagem from '@/interfaces/Mensagem'

export const useMensagemStore = defineStore('mensagem', () => {
  const mensagem = ref<Mensagem | null>(null)

  function setMensagem(value: Mensagem): void {
    mensagem.value = value
  }

  function excluirMensagem(): void {
    mensagem.value = null
  }

  return { mensagem, setMensagem, excluirMensagem }
})

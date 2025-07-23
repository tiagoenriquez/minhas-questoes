import { ref } from 'vue'
import { defineStore } from 'pinia'
import Prova from '@/models/Prova'
import Questao from '@/models/Questao'

export const useProvaStore = defineStore('prova', () => {
  const prova = ref<Prova | null>(null)

  function criar(questoes: Questao[]): void {
    prova.value = new Prova(questoes)
  }

  function setProva(value: Prova): void {
    prova.value = value
  }

  return { prova, criar, setProva }
})

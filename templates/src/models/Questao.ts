import type QuestaoI from '@/interfaces/Questao'
import Alternativa from './Alternativa'

export default class Questao {
  numero: number
  enunciado: string
  alternativas: Alternativa[]
  respondida: boolean
  acertada: boolean

  constructor(numero: number, questao: QuestaoI) {
    this.numero = numero
    this.enunciado = questao.enunciado
    this.alternativas = questao.alternativas
      ? questao.alternativas.map((alternativa) => new Alternativa(alternativa))
      : []
    this.respondida = false
    this.acertada = false
  }

  responder(alternativaId: number): void {
    this.alternativas.forEach((alternativa) => {
      if (alternativaId === alternativa.id) {
        this.respondida = true
        this.acertada = alternativa.correta
        alternativa.selecionar()
      }
    })
  }
}

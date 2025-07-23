import type AlternativaI from '@/interfaces/Alternativa'

export default class Alternativa {
  id: number
  texto: string
  correta: boolean
  justificativa: string
  selecionada: boolean

  constructor(alternativa: AlternativaI) {
    this.id = alternativa.id ? alternativa.id : 0
    this.texto = alternativa.texto
    this.correta = alternativa.correta
    this.justificativa = alternativa.justificativa
    this.selecionada = false
  }

  selecionar(): void {
    this.selecionada = true
  }
}

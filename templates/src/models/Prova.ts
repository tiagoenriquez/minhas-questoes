import Questao from './Questao'

export default class Prova {
  questoes: Questao[]

  constructor(questoes: Questao[]) {
    this.questoes = questoes
  }

  nota(): number {
    const respondidas = this.questoes.filter((questao) => questao.respondida)
    if (respondidas.length === 0) {
      return 0
    }
    return (
      (respondidas.reduce((prev, questao) => prev + (questao.acertada ? 1 : 0), 0) * 10) /
      respondidas.length
    )
  }

  procurarQuestao(numero: number): Questao | undefined {
    return this.questoes.find((questao) => numero === questao.numero)
  }

  proximaQuestao(): Questao | undefined {
    return this.questoes.find((questao) => !questao.respondida)
  }

  questoesAcertadas(): number {
    return this.questoes.filter((questao) => questao.acertada).length
  }

  questoesErradas(): number {
    return this.questoes.filter((questao) => questao.respondida && !questao.acertada).length
  }

  questoesRespondidas(): Questao[] {
    return this.questoes.filter((questao) => questao.respondida)
  }
}

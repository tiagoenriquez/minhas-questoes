import type AlternativaI from './Alternativa'
import type DisciplinaI from './Disciplina'

export default interface QuestaoI {
  id?: number
  enunciado: string
  disciplina_id: number
  valida?: boolean
  disciplina?: DisciplinaI
  alternativas?: AlternativaI[]
}

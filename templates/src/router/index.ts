import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CadastrarDisciplina from '@/views/admin/disciplinas/CadastrarDisciplina.vue'
import AdminApp from '@/views/admin/AdminApp.vue'
import ListarDisciplinas from '@/views/admin/disciplinas/ListarDisciplinas.vue'
import Erro from '@/views/Erro.vue'
import EditarDisciplina from '@/views/admin/disciplinas/EditarDisciplina.vue'
import CadastrarQuestao from '@/views/admin/questoes/CadastrarQuestao.vue'
import ProcurarQuestao from '@/views/admin/questoes/ProcurarQuestao.vue'
import CadastrarAlternativa from '@/views/admin/alternativas/CadastrarAlternativa.vue'
import MostrarQuestao from '@/views/admin/questoes/MostrarQuestao.vue'
import EditarQuestao from '@/views/admin/questoes/EditarQuestao.vue'
import ListarQuestoes from '@/views/admin/questoes/ListarQuestoes.vue'
import EditarAlternativa from '@/views/admin/alternativas/EditarAlternativa.vue'
import ProximaQuestao from '@/views/site/ProximaQuestao.vue'
import SiteApp from '@/views/site/SiteApp.vue'
import Desempenho from '@/views/site/Desempenho.vue'
import QuestoesRespondidas from '@/views/site/QuestoesRespondidas.vue'
import DetalhesDaQuestao from '@/views/site/DetalhesDaQuestao.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin',
      component: AdminApp,
      children: [
        {
          path: 'alternativas',
          children: [
            {
              path: 'cadastro/:questao_id',
              name: 'cadastrar-alternativa',
              component: CadastrarAlternativa,
            },
            {
              path: 'edicao/:id',
              name: 'editar-alternativa',
              component: EditarAlternativa,
            },
          ],
        },
        {
          path: 'disciplinas',
          children: [
            {
              path: 'cadastro',
              name: 'cadastrar-disciplina',
              component: CadastrarDisciplina,
            },
            {
              path: 'edicao/:id',
              name: 'editar-disciplina',
              component: EditarDisciplina,
            },
            {
              path: 'lista',
              name: 'listar-disciplinas',
              component: ListarDisciplinas,
            },
          ],
        },
        {
          path: 'erro/:erro',
          name: 'erro-admin',
          component: Erro,
        },
        {
          path: 'questoes',
          children: [
            {
              path: 'cadastro',
              name: 'cadastrar-questao',
              component: CadastrarQuestao,
            },
            {
              path: 'edicao/:id',
              name: 'editar-questao',
              component: EditarQuestao,
            },
            {
              path: 'detalhe/:id',
              name: 'mostrar-questao',
              component: MostrarQuestao,
            },
            {
              path: 'lista/:trecho',
              name: 'listar-questoes',
              component: ListarQuestoes,
            },
            {
              path: 'procura',
              name: 'procurar-questao',
              component: ProcurarQuestao,
            },
          ],
        },
      ],
    },
    {
      path: '/prova',
      component: SiteApp,
      children: [
        {
          path: 'desempenho',
          name: 'desempenho',
          component: Desempenho,
        },
        {
          path: 'detalhes-da-questao/:numero',
          name: 'detalhes-da-questao',
          component: DetalhesDaQuestao,
        },
        {
          path: 'proxima-questao',
          name: 'proxima-questao',
          component: ProximaQuestao,
        },
        {
          path: 'questoes-respondidas',
          name: 'questoes-respondidas',
          component: QuestoesRespondidas,
        },
      ],
    },
  ],
})

export default router

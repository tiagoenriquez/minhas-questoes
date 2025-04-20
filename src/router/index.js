import { createRouter, createWebHistory } from 'vue-router'
import CreateQuestion from '@/views/admin/questions/CreateQuestion.vue'
import CreateSubject from '@/views/admin/subject/CreateSubject.vue'
import EditSubject from '@/views/admin/subject/EditSubject.vue'
import Error from '@/views/error.vue'
import SelectSubject from '@/views/site/SelectSubject.vue'
import Subjects from '@/views/admin/subject/Subjects.vue'
import FindQuestion from '@/views/admin/questions/FindQuestion.vue'
import Questions from '@/views/admin/questions/Questions.vue'
import EditQuestion from '@/views/admin/questions/EditQuestion.vue'
import TestNextQuestion from '@/views/test/TestNextQuestion.vue'
import Performance from '@/views/test/Performance.vue'
import RespondedQuestions from '@/views/test/RespondedQuestions.vue'
import QuestionDetails from '@/views/test/QuestionDetails.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'select-subject',
      component: SelectSubject,
    },
    {
      path: '/disciplina/cadastro',
      name: 'create-subject',
      component: CreateSubject
    },
    {
      path: '/disciplina/lista',
      name: 'subjects',
      component: Subjects
    },
    {
      path: '/disciplina/edicao/:id',
      name: 'edit-subject',
      component: EditSubject
    },
    {
      path: '/erro',
      name: 'error',
      component: Error
    },
    {
      path: '/prova/desempenho',
      name: 'performance',
      component: Performance
    },
    {
      path: '/prova/detalhes-de-questao/:id',
      name: 'question-detail',
      component: QuestionDetails
    },
    {
      path: '/prova/proxima-questao',
      name: 'test-next-question',
      component: TestNextQuestion
    },
    {
      path: '/prova/questoes-respondidas',
      name: 'responded-questions',
      component: RespondedQuestions
    },
    {
      path: '/questao/cadastro',
      name: 'create-question',
      component: CreateQuestion
    },
    {
      path: '/questao/edicao/:id',
      name: 'edit-question',
      component: EditQuestion
    },
    {
      path: '/questao/lista/:excerpt',
      name: 'questions',
      component: Questions
    },
    {
      path: '/questao/procurar',
      name: 'find-question',
      component: FindQuestion
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      redirect: '/erro'
    }
  ],
})

export default router

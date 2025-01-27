<script setup lang="js">
import router from '@/router';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import AdminMenu from '@/components/AdminMenu.vue';
import MessageComponent from '@/components/MessageComponent.vue';
import store from '@/store';
import { apiUrl, axios } from '@/connections/apiConnection';

const route = useRoute();
const error = ref('');
const success = ref('');
const id = ref(0);
const subject = ref(null);
const subjects = ref([]);
const subjectId = ref(0);
const statement = ref('');
const alternatives = ref([]);

axios.get(`${apiUrl}/subjects`).then(result => subjects.value = result.data);

axios.get(`${apiUrl}/questions/${route.params.id}`).then(result => {
  id.value = result.data.id;
  subjectId.value = result.data.subject_id;
  subject.value = subjects.value.filter(subject => subject.id === result.data.subject_id)[0];
  statement.value = result.data.statement;
  result.data.alternatives.forEach(alternative => {
    alternatives.value.push({
      id: alternative.id,
      text: alternative.alternative_text,
      correct: alternative.correct,
      repeated: false
    });
  });
  if (!result.data) throw new Error('Questão não encontrada');
}).catch(error => {
  store.commit('setError', error.message);
  router.push('/erro');
});

function update() {
  if (repeatedAlternatives()) {
    error.value = 'Existem alternativas repetidas.';
    return;
  }
  axios.defaults.headers.common['Content-Type'] = 'application/json';
  axios.put(`${apiUrl}/questions/${id.value}`, {
    subject_id: subjectId.value,
    statement: statement.value,
    alternatives: alternatives.value
  }).then(result => {
    success.value = result.data;
  }).catch(err => error.value = err.response.data);
}

function destroy() {
  axios.delete(`${apiUrl}/questions/${id.value}`).then(result => router.push('/questao/procurar'));
}

function fixAlternatives(event) {
  alternatives.value.forEach(alternative => {
    alternative.correct = alternative.id === parseInt(event.target.id.split('-')[1]);
  });
}

function repeatedAlternatives() {
  let repeated = false
  alternatives.value.forEach(alternative => alternative.repeated = false);
  alternatives.value.forEach((alternative, index) => {
    alternatives.value.slice(index + 1).forEach(otherAlternative => {
      if (alternative.text === otherAlternative.text) {
        alternative.repeated = true;
        otherAlternative.repeated = true;
        repeated = true;
      }
    });
  });
  return repeated;
}

function addAlternative() {
  alternatives.value.push({ id: alternatives.value.length + 1, correct: false, text: 'Errado', repeated: false });
  repeatedAlternatives();
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Edição de Questão</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <div v-if="subjects" class="row">
      <label for="subject">Disciplina</label>
      <select v-model="subjectId">
        <option v-if="subject" :value="subjectId">{{ subject.name }}</option>
        <option v-for="subject in subjects" :key="subject.id" :value="subject.id">{{ subject.name }}</option>
      </select>
    </div>
    <div class="column">
      <label for="statement" class="label-for-textarea">Enunciado</label>
      <textarea id="statement" cols="64" rows="8" v-model="statement">{{ statement }}</textarea>
    </div>
    <div class="alternatives">
      <div class="row" v-for="alternative in alternatives" :key="alternative.id">
        <input
          type="radio"
          :id="`alternative-${alternative.id}`"
          name="correct-alternative"
          :checked="alternative.correct"
          @click="fixAlternatives"
        >
        <textarea
          cols="48"
          rows="2"
          :class="alternative.repeated ? 'repeated' : ''"
          @keyup="repeatedAlternatives()"
          v-model="alternative.text"
        >
          {{ alternative.text }}
        </textarea>
      </div>
    </div>
    <div class="row">
      <button @click="addAlternative()">Adicionar Alternativa</button>
      <button @click="update()">Salvar</button>
      <button @click="destroy()">Excluir</button>
    </div>
  </main>
</template>
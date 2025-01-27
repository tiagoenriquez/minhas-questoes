<script setup lang="js">
import { ref } from 'vue';
import AdminMenu from '@/components/AdminMenu.vue';
import MessageComponent from '@/components/MessageComponent.vue';
import { axios, apiUrl } from '@/connections/apiConnection';

const error = ref('');
const success = ref('');
const subjects = ref([]);
const subjectId = ref(0);
const statement = ref('');
const image = ref(null);
const imageName = ref('');
const alternatives = ref(
  [{ id: 1, correct: true, text: 'Certo', repeated: false },
  { id: 2, correct: false, text: 'Errado', repeated: false }]
);

axios.get(`${apiUrl}/subjects/`).then(result => subjects.value = result.data);

function insert() {
  if (!subjectId.value) {
    error.value = 'Escolha uma disciplina';
    return;
  }
  if (repeatedAlternatives()) {
    error.value = 'Existem alternativas repetidas.';
    return;
  }
  const formData = new FormData();
  formData.append('subject_id', subjectId.value.toString());
  formData.append('statement', statement.value);
  formData.append('alternatives', JSON.stringify(alternatives.value));
  formData.append('image', image.value);
  axios.defaults.headers.common['Content-Type'] = 'multipart/form-data';
  axios.post(`${apiUrl}/questions/`, formData).then(result => {
    success.value = result.data;
    cleanFiealds();
  })
  .catch(err => error.value = err.response.data);
}

function writeImage(event) {
  const file = event.target.files[0];
  imageName.value = file.name;
  image.value = file;
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

function removeAlternative(id) {
  const filter = (alternative) => alternative.id === id;
  if (alternatives.value.length <= 2) {
    error.value = 'O número de alternativas deve ser no mínimo 2';
    return;
  }
  if (alternatives.value.filter(filter)[0].correct) {
    error.value = 'Deve haver uma alternativa correta';
    return;
  }
  const index = alternatives.value.findIndex(filter);
  alternatives.value.splice(index, 1);
  repeatedAlternatives();
}

function fixAlternatives(event) {
  alternatives.value.forEach(alternative => {
    alternative.correct = alternative.id === parseInt(event.target.id.split('-')[1]);
  });
}

function cleanFiealds() {
  statement.value = '';
  alternatives.value.forEach(alternative => alternative.text = '');
}
</script>

<template>
  <AdminMenu />
  <main>
    <h1>Cadastro de Questão</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <div class="row">
      <label for="subject">Disciplina</label>
      <select id="subject" v-model="subjectId" autofocus>
        <option value="0"></option>
        <option v-for="subject in subjects" :key="subject.id" :value="subject.id">{{ subject.name }}</option>
      </select>
    </div>
    <div class="column">
      <label for="statement" class="label-for-textarea">Enunciado</label>
      <textarea id="statement" cols="64" rows="8" v-model="statement"></textarea>
    </div>
    <div class="row">
      <label for="image" class="image-label">Imagem</label>
      <input type="file" id="image" accept="image/png,image/jpeg" @change="writeImage" />
      <input type="text" v-model="imageName" title="Cole o nome da imagem onde deseja que apareça no texto." readonly />
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
        <button @click="() => removeAlternative(alternative.id)">Excluir</button>
      </div>
    </div>
    <div class="row">
      <button @click="addAlternative()">Adicionar Alternativa</button>
      <button @click="insert()">Salvar</button>
    </div>
  </main>
</template>
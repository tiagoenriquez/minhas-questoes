<script setup lang="js">
import { computed, ref, watch } from 'vue';
import MessageComponent from '@/components/MessageComponent.vue';
import TestMenu from '@/components/TestMenu.vue';
import router from '@/router';
import store from '@/store';

const error = ref('');
const success = ref('');
const alternatives = ref(null);
const paragraphs = ref([]);
const selected = ref(null);

const question = computed(() => {
  const index = store.state.test.questions.findIndex(q => !q.responded);
  if (index !== -1) {
    return { ...store.state.test.questions[index], index };
  }
  return null;
});

watch(question, (newQuestion) => {
  if (newQuestion) {
    paragraphs.value = newQuestion.statement.split('\n').map((paragraph, id) => ({ id, text: paragraph }));
    alternatives.value = newQuestion.alternatives.map((alternative, index) => ({
      index,
      selected: false,
      paragraphs: alternative.alternative_text.split('\n').map((paragraph, index) => ({
        index,
        text: paragraph,
      })),
    }));
    selected.value = null;
  } else {
    router.push('/prova/desempenho');
  }
}, { immediate: true });

function getImageSource(text) {
  const fileName = text.replace('@image=', '').replace('\r', '');
  const imageSource = store.state.test.images.filter(image => image.name === fileName)[0].content;
  return `data:image/png;base64,${imageSource}`;
}

function calculateGrade(test) {
  let corrects = 0;
  let respondeds = 0
  test.questions.forEach(question => {
    if (question.correct) corrects++;
    if (question.responded) respondeds++;
  });
  return (corrects / respondeds) * 10;
}

function respond() {
  if (selected.value === null) {
    error.value = 'Selecione uma alternativa';
    return;
  }
  const currentQuestion = store.state.test.questions[question.value.index];
  currentQuestion.responded = true;
  currentQuestion.alternatives.forEach((alternative, index) => {
    alternative.selected = index === selected.value;
    if (alternative.selected && alternative.correct) {
      currentQuestion.correct = true;
    }
  });
  const test = store.state.test;
  test.questions[question.id] = currentQuestion;
  test.grade = calculateGrade(test);
  store.commit('setTest', test);
  console.log(test.questions.length);
  if (!store.state.test.questions.some(q => !q.responded)) {
    router.push('/prova/desempenho');
  }
}
</script>

<template>
  <TestMenu />
  <main v-if="question">
    <button>Nota: {{ store.state.test.grade.toFixed(1).replace('.', ',') }}</button>
    <h1>Questão {{ question.number }}</h1>
    <div v-if="error">
      <MessageComponent class-name="error" :message="error" @close="error = ''" />
    </div>
    <div v-if="success">
      <MessageComponent class-name="success" :message="success" @close="success = ''" />
    </div>
    <div class="text">
      <div v-for="paragraph in paragraphs" :key="paragraph.id">
        <p v-if="!paragraph.text.startsWith('@image=')">{{ paragraph.text }}</p>
        <img v-else :src="getImageSource(paragraph.text)" alt="Imagem não encontrada" />
      </div>
    </div>
    <div class="alternatives">
      <div class="alternative" v-for="alternative in alternatives" :key="alternative.index">
        <input type="radio" name="correct" :id="`alternative-${alternative.index}`" v-model="selected" :value="alternative.index"/>
        <label class="text-alternative" :for="`alternative-${alternative.index}`">
          <p v-for="paragraph in alternative.paragraphs" :key="paragraph.index">{{ paragraph.text }}</p>
        </label>
      </div>
    </div>
    <button @click="respond()">Responder</button>
  </main>
</template>
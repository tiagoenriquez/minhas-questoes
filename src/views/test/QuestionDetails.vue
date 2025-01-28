<script setup lang="js">
import { useRoute } from 'vue-router';
import TestMenu from '@/components/TestMenu.vue';
import store from '@/store';

const test = store.state.test;
const route = useRoute();
const question = test.questions[route.params.id];

const paragraphs = question.statement.split('\n').map((paragraph, index) => {
  return { index, text: paragraph };
});

function getImageSource(text) {
  const fileName = text.replace('@image=', '').replace('\r', '');
  const imageSource = store.state.test.images.filter(image => image.name === fileName)[0].content;
  return `data:image/png;base64,${imageSource}`;
}

function getAlternativeCommentAndClass(alternative) {
  if (alternative.correct && alternative.selected) {
    return { class: 'correct', comment: 'Alternativa correta selecionada:' };
  }
  if (alternative.correct && !alternative.selected) {
    return { class: 'unselected', comment: 'Alternativa correta:' };
  }
  if (!alternative.correct && alternative.selected) {
    return { class: 'wrong', comment: 'Alternativa selecionada:' };
  }
  return false;
}

const alternatives = question.alternatives.map((alternative, index) => {
  const commentAndClass = getAlternativeCommentAndClass(alternative);
  return {
    index,
    comment: commentAndClass.comment,
    class: commentAndClass.class,
    paragraphs: alternative.alternative_text.split('\n').map((paragraph, index) => {
      return { index, text: paragraph };
    })
  };
});
</script>

<template>
  <TestMenu />
  <main>
    <h1>Detalhes da questão {{ question.number }}</h1>
    <div class="text">
      <div v-for="paragraph in paragraphs" :key="paragraph.id">
        <p v-if="!paragraph.text.startsWith('@image=')">{{ paragraph.text }}</p>
        <img v-else :src="getImageSource(paragraph.text)" alt="Imagem não encontrada" />
      </div>
    </div>
    <div class="alternatives">
      <div class="alternative" v-for="alternative in alternatives" :key="alternative.index">
        <div :class="`text ${alternative.class}`">
          <p v-if="alternative.class" class="comment">{{ alternative.comment }}</p>
          <p v-for="paragraph in alternative.paragraphs" :key="paragraph.index">{{ paragraph.text }}</p>
        </div>
      </div>
    </div>
  </main>
</template>
<script setup lang="js">
const props = defineProps({ message: String, className: String });
const emit = defineEmits(['close']);

function close() {
  emit('close');
}
</script>

<template>
  <div v-if="message" :class="className">
    {{ message }}
    <button @click="close()">X</button>
  </div>
</template>
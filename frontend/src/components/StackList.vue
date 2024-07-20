<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

const stacks = ref([]);

const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  stacks.value = response.data;
  console.log(stacks.value);
};

onMounted(() => {
  getStacks();
});

</script>

<template>
  <p class="fs-2 stack__title text-center mt-1 mb-4">Мои инструменты</p>
  <div class="stack col-2" v-for="stack in stacks" :key="stack.id">
    <img
      class="logo-stack"
      :src="stack.img"
      :alt="stack.title"
      :title="stack.title"
    />
  </div>
</template>

<style scoped>
.stack {
  margin-block: 20px;
}

.logo-stack {
  width: 80px;
  height: 80px;
  cursor: pointer;
  transition: all 0.3s ease-in;

  &:hover {
    transform: scale(1.2);
    filter: brightness(1.1);
  }
}

.stack__title {
  color: white;
  text-shadow: 2px 2px 3px #f5e60f95;
}

</style>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

const stacks = ref([]);
const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  console.log(response.data);
  stacks.value = response.data;
};
onMounted(() => getStacks());
</script>
<template>
  <div class="home text-center text">
    <p>
      Привет! Я Сергей Бойцов.<br />
      Начинающий fullstack разработчик.
    </p>
<!-- 
    <div v-for="stack in stacks" :key="stack.id" class="col">
      <p class="text-center text">{{ stack.title }}</p>
    </div> -->
  </div>

  <div class="container">
    <div class="row"></div>
  </div>
</template>

<style scoped>
.home {
  width: 100%;
  min-height: 50vh;
  background: linear-gradient(90deg, #2c3136, #03e9f4);
}

.text {
  font-size: 2rem;
  color: #690175;
  text-shadow: 0 0 5px #03e9f4;
  animation: animate 1.5s linear infinite;
}
</style>

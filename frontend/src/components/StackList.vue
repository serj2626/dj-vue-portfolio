<script setup>
import axios from "axios";
import { computed, onMounted, ref } from "vue";
import Progress from "../components/Progress.vue";
import CircleProgress from "@/components/CircleProgress.vue";
const stacks = ref([]);

const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  stacks.value = response.data;
  console.log(stacks.value);
};

onMounted(() => {
  getStacks();
});

const helperInfo = ref(false);
const stackInfo = ref({});

const mouseIn = (value) => {
  helperInfo.value = true;
  stackInfo.value = value;
};

const mouseOut = () => {
  helperInfo.value = false;
  stackInfo.value = {};
};
</script>

<template>
  <p class="fs-2 stack__title text-center mt-1 mb-4">Мои инструменты</p>
  <div class="grid">
    <div class="item" v-for="stack in stacks" :key="stack.id">
      <img
        @mouseenter="mouseIn(stack)"
        @mouseleave="mouseOut"
        class="logo-stack"
        :src="stack.img"
        :alt="stack.title"
      />

      <transition name="fade">
        <div
          class="card text-center  text-white"
          v-if="helperInfo && stackInfo.id === stack.id"
        >
          <p class="stackInfo__title">{{ stackInfo.title }}</p>
          <p>Знание инструмента</p>
          <div class="w-75 mx-auto">
            <circle-progress
              :is-shadow="true"
              :viewport="true"
              :transition="1200"
              :size="120"
              :value="stackInfo.level"
              :percent="stackInfo.level"
              :show-percent="true"
              :is-bg-shadow="true"
            />
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<style scoped>
/* ANIMATION */
.fade-enter-active {
  transition: opacity 0.8s ease-in;
}
.fade-leave-active {
  transition: opacity 0.3s ease-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* STACK */

.stackInfo__title{
  font-size: 20px;
  text-transform: uppercase;
  color: orange;
}

.card {
  position: absolute;
  top: -220px;
  left: 100px;
  z-index: 10;
  padding: 10px;
  min-width: 200px;
  box-sizing: border-box;
  border: 1px solid #03e9f4;
  box-shadow: 0 0 10px #03e9f4;
  border-radius: 30px 0 30px 10px;
  background-color: rgb(60, 55, 55);
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  grid-auto-rows: 100px;
  grid-gap: 60px;
  place-items: center;
  margin-block: 60px;
  margin-inline: auto;
}
.item {
  position: relative;
}

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

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import Progress from "../components/Progress.vue";
import CircleProgress from "@/components/CircleProgress.vue";

const stacks = ref([]);

const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  console.log(response.data);
  stacks.value = response.data;
};

onMounted(() => {
  getStacks();
});
</script>
<template>
  <div class="container py-1">

    <div class="row">
      <div class="info">
        <div class="d-flex justify-content-around">
        <div class="text-center text">
          <p>
            Привет! Я Сергей Бойцов.<br />
            Начинающий fullstack разработчик.
          </p>
          <p>
            На этом сайте представлены мои пет-проекты,<br />
            статьи и вся контактная информация.
          </p>
        </div>
        <div>
          <img width="500" height="auto" src="/avatar.png" alt="" />
        </div>
      </div>
      </div>
      
    </div>

    <div class="row">
      <p class="fs-1 title text-center my-3">Инструменты</p>
      <div class="stack col-2" v-for="stack in stacks" :key="stack.id">
        <img
          class="logo-stack"
          :src="stack.img"
          :alt="stack.title"
          :title="stack.title"
        />
      </div>
    </div>

    <div class="row">
      <div class="d-flex justify-content-around text-white">
        <div class="d-flex flex-column w-50 text-center">
          <p class="fs-1 title">Знание стека</p>
          <div class="progress_bar" v-for="stack in stacks" :key="stack.id">
            <Progress :title="stack.title" :progress="stack.level" />
          </div>
        </div>
        <div class="w-50 ml-2 position-relative text-center">
       <p class="fs-1 title">Статистика</p>         
          <div class="circle">
            <CircleProgress />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info{
  padding-block: 50px;
  border: none;
  border-radius: 20px;
  background-color: #23272a;
}
.circle {
  position: absolute;
  right: 20%;
  top: 10%;
}
.row {
  margin-block: 90px;
}

.stack {
  margin-block: 20px;
}

.logo-stack {
  width: 80px;
  height: 80px;
  cursor: pointer;
  transition: 0.5s;

  &:hover {
    transform: scale(1.1);
  }
}

.title {
  color: #03e9f4;
}

img {
  filter: brightness(1.2);
}

.text {
  font-size: 2rem;
  font-family: "Poppins", sans-serif;
  color: #03e9f4;
  animation: animate 4.5s linear alternate;
}

@keyframes animate {
  0% {
    opacity: 0;
  }

  25% {
    opacity: 0.2;
  }

  50% {
    opacity: 0.5;
  }

  75% {
    opacity: 0.7;
  }

  100% {
    opacity: 1;
  }
}

/* @keyframes animate {
  0% {
    color: #9fa2a0;
    text-shadow: 0 0 5px #03e9f4;
  }
  50% {
    color: #03e9f4;
    text-shadow: 0 0 10px #03e9f4;
  }
  100% {
    color: #9fa2a0;
    text-shadow: 0 0 5px #03e9f4;
  }
} */
</style>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import Progress from "../components/Progress.vue";
import CircleProgress from "@/components/CircleProgress.vue";

const stacks = ref([]);

const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  stacks.value = response.data;
};

onMounted(() => {
  getStacks();
});
</script>
<template>
  <div class="d-flex justify-content-center align-items-center mb-5">
    <div class="aboutMe">
      Привет, я Сергей Бойцов <br>Начинающий Full-Stack разработчик.
    </div>
 
      <img width="1000" height="auto" src="@/assets/home.png" alt="" />
 
  </div>


  <div class="row mx-auto w-75">
    <p class="fs-2 title text-center mt-1 mb-4">Инструменты</p>
    <div class="stack col-2" v-for="stack in stacks" :key="stack.id">
      <img class="logo-stack" :src="stack.img" :alt="stack.title" :title="stack.title" />
    </div>
  </div>

  <div class="row">
    <div class="d-flex justify-content-around text-white">
      <div class="d-flex flex-column w-50">
        <p class="fs-2 title text-center">Знание стека</p>
        <div class="progress_bar" v-for="stack in stacks" :key="stack.id">
          <Progress :title="stack.title" :progress="stack.level" />
        </div>
      </div>
      <div class="w-50 ml-2 position-relative">
        <p class="fs-2 title text-center">Статистика</p>
        <div class="circle">
          <CircleProgress />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.aboutMe {

  text-align: center;
  font-size: 36px;
  letter-spacing: 1.5px;
  font-family: "Poppins", sans-serif;
  color: #45b1ff;
  font-style: italic;

  animation-name: start-show-aboutMe;
  animation-duration: 3s;
  animation-fill-mode: forwards;
  animation-timing-function: linear;
}

@keyframes start-show-aboutMe {
  0% {
    opacity: 0;
    scale: 0.2;
    color: white;
  }

  50% {
    opacity: 0.5;
  }



  100% {
    opacity: 1;
  }
}

img{
  animation: image-to-color 5s linear ;
}

@keyframes image-to-color {
  0% {
    filter: brightness(0.7);
  }

  50% {
    filter: brightness(1.1);
  }

  100% {
    filter: brightness(1.5);
  }
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
    transform: scale(1.2);
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
  color: #d1ded5;

  padding: 60px 20px;
  border: none;
  border-radius: 20px;
  background-color: #343c42;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.5);
}
</style>

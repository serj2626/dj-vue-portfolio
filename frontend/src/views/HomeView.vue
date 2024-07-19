<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
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

</script>
<template>
  <div class="d-flex justify-content-center align-items-center mb-5 w-75 mx-auto">
    <div class="aboutMe">
      Привет, я Сергей Бойцов. Начинающий Full-Stack разработчик.
    </div>

    <img width="auto" height="auto" src="@/assets/home.png" alt="" />

  </div>


  <div class="row mx-auto w-75">
    <p class="fs-2 stack__title text-center mt-1 mb-4">Мои инструменты</p>
    <div class="stack col-2" v-for="stack in stacks" :key="stack.id">
      <img class="logo-stack" :src="stack.img" :alt="stack.title" :title="stack.title" />
    </div>
  </div>

  <div class="row">
    <div class="d-flex justify-content-around text-white">
      <div class="d-flex flex-column w-50">
        <p class="fs-2 stack__title text-center">Знание стека</p>
        <div class="progress_bar" v-for="stack in stacks" :key="stack.id">
          <Progress :title="stack.title" :progress="stack.level" />
        </div>
      </div>
      <div class="w-50 ml-2 position-relative">
        <p class="fs-2 stack__title text-center">Статистика</p>
        <div class="circle">
          <CircleProgress />
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="w-75 mx-auto">

      <div class="statistic">
        <div class="block1">100</div>
        <div class="block2">213</div>
        <div class="block3">123123</div>
      </div>

    </div>
  </div>



  <div class="row mx-auto w-75">
    <p>Знание стека</p>

    <div v-for="stack in stacks" :key="stack.id">
      <span class="text-white">{{ stack.title }} {{ stack.level }}%</span>
      <hr class="text-white" :style="{ width: stack.level + '%' }">
      <div class="z bg-warning" :style="{ width: stack.level + '%' }">
      </div>
    </div>
  </div>


</template>

<style scoped>

.statistic {
  display: flex;
  justify-content: center;
  align-items: center;

}

.block1 {
  width: 250px;
  height: 150px;
  background-color: red;
  border-radius: 10px;
}

.block2 {
  width: 250px;
  height: 150px;
  background-color: green;
  border-radius: 10px;
  margin-inline: 30px;
}

.block3 {
  width: 250px;
  height: 150px;
  background-color: blue;
  border-radius: 20px;
}

.z {
  border: 2px solid rgb(250, 250, 250);
  margin-block: 10px;
  border-radius: 10px;
  box-sizing: border-box;
  height: 30px;
}

/* aadsad */


.aboutMe {

  text-align: center;
  font-size: 36px;
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

img {
  animation: image-to-color 5s linear;
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

.stack__title {
  color: white;
  text-shadow: 2px 2px 3px #f5e60f95;
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

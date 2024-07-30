<script setup>
import StacklList from "../components/StackList.vue";
</script>
<template>
  <div class="row bg-warning">
    <img class="header-img col-6 w-75" src="@/assets/home.png" alt="Photo" />
    <div class="col-4 gap-2">
      <div class="header-desc">
        <h1 class="header-title text-white">Сергей Бойцов</h1>
        <p class="header-text text-white">
          фрилансер, веб-разработчик,<br />
          создание сайтов
        </p>
      </div>
    </div>
  </div>

  <!-- <div class="d-flex justify-content-center align-items-center">
      <div class="aboutMe">
        <h1 class="header-title">Сергей Бойцов</h1>
        <p class="header-text">
          фрилансер, веб-разработчик,<br />
          создание сайтов
        </p>
      </div>

      <img src="@/assets/home.png" alt="" />
    </div> -->

  <div class="row mx-auto w-75 stacks">
    <StacklList />
  </div>

  <div class="row">
    <div class="w-75 mx-auto">
      <p class="fs-2 statistic__title text-center text-white mt-5">
        Статистика сайта
      </p>

      <div class="statistic text-center">
        <div class="block">
          <h4>Статей</h4>
          <span>4</span>
        </div>
        <div class="block">
          <h4>Проектов</h4>
          <span>6</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes stacks-scroll {
  from {
    opacity: 0;
    scale: 0.5;
    transform: translateY(300px);
  }
}

.stacks {
  animation-name: stacks-scroll;
  animation-fill-mode: both;
  animation-timing-function: ease-in;

  view-timeline-name: --stacks-scroll;
  animation-timeline: --stacks-scroll;
  animation-range: 20% 50%;
}

.statistic {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 20px;
}

.statistic__title {
  text-shadow: 3px 3px 3px #f5e60f95;
}

/**  BLOCK STATISTIC  */
@keyframes block-from-left {
  from {
    opacity: 0;
    transform: translateX(-250px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
@keyframes block-from-right {
  from {
    opacity: 0;
    transform: translateX(250px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
.statistic .block:nth-child(1) {
  animation-name: block-from-left;
  animation-fill-mode: both;
  animation-timing-function: ease-in;

  view-timeline-name: --block-from-left;
  animation-timeline: --block-from-left;
  animation-range: 20% 40%;
}

.statistic .block:nth-child(2) {
  animation-name: block-from-right;
  animation-fill-mode: both;
  animation-timing-function: ease-in;

  view-timeline-name: --block-from-right;
  animation-timeline: --block-from-right;
  animation-range: 20% 40%;
}

.statistic .block:nth-child(1):hover {
  rotate: 5deg;
    translate: 0 -10px;
    background-color: rgb(64, 59, 59);
}
.statistic .block:nth-child(2):hover {
  rotate: -5deg;
    translate: 0 -10px;
    background-color: rgb(64, 59, 59);
}
.block {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  padding: 20px 10px;
  width: 250px;
  height: 150px;
  color: #07bcc6;
  background-color: rgb(32, 31, 31);
  border-radius: 10px;
  box-sizing: border-box;
  box-shadow: 0 0 20px white;
  transition: all 0.5s ease;

  /* &:hover {
    rotate: 5deg;
    translate: 0 -10px;
    background-color: rgb(64, 59, 59);
  } */
}

.block span {
  font-size: 36px;
  font-family: "Poppins", sans-serif;
  color: #f0cc00;
  font-style: italic;
}

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
    scale: 0.7;
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

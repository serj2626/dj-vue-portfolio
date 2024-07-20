<script setup>
import StacklList from "../components/StackList.vue";
</script>
<template>
  <div class="row col-10 mx-auto">
    <div class="col-5">
      <img
        class="header-img text-center"
        src="@/assets/home.png"
        srcset="./img/photo@2x.jpg 2x"
        alt="Photo"
      />
    </div>
    <div class="col-4">
      <div class="header-desc">
        <h1 class="header-title text-white">Сергей Бойцов</h1>
        <p class="header-text text-white">
          фрилансер, веб-разработчик,<br />
          создание сайтов
        </p>

        <div class="header-btns">
          <a href="#" class="btn">Портфолио</a>
          <a href="#" class="btn-outline">Контакты</a>
        </div>
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

  <div class="row mx-auto w-75">
    <StacklList />
  </div>

  <div class="row">
    <div class="w-75 mx-auto">
      <p class="fs-2 statistic__title text-center text-white mt-5">
        Статистика сайта
      </p>

      <div class="statistic text-center">
        <div class="block text-white">
          <h4>Количество статей</h4>
          <span>4</span>
        </div>
        <div class="block text-white">
          <h4>Количество проектов</h4>
          <span>6</span>
        </div>
      </div>
    </div>
  </div>
  -->
</template>

<style scoped>
.statistic {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 60px;
}

.statistic__title {
  text-shadow: 3px 3px 3px #f5e60f95;
}

.block {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  padding: 20px 10px;
  width: 250px;
  height: 150px;
  background-color: rgb(32, 31, 31);
  border-radius: 10px;
  box-sizing: border-box;
  box-shadow: 0 0 10px white;
  transition: all 0.5s ease;

  &:hover {
    rotate: 5deg;
    translate: 0 -10px;
    background-color: rgb(64, 59, 59);
  }
}

.block span{
  font-size: 36px;
  font-family: "Poppins", sans-serif;
  color: #45b1ff;
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

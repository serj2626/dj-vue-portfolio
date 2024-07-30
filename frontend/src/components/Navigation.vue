<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
</script>

<template>
  <div class="btns">
    <RouterLink class="nav-link" :to="{ name: 'home' }">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Главная
    </RouterLink>
    <RouterLink class="nav-link" :to="{ name: 'projects' }">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Проекты
    </RouterLink>
    <RouterLink class="nav-link" :to="{ name: 'resume' }">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Резюме
    </RouterLink>
    <RouterLink class="nav-link" :to="{ name: 'contacts' }">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Контакты
    </RouterLink>
  </div>
</template>

<style scoped>
.btns {
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-link {
  position: relative;
  display: inline-block;
  padding: 25px 30px;
  margin: 40px 0;
  color: #03e9f4;
  text-transform: uppercase;
  letter-spacing: 4px;
  text-decoration: none;
  font-size: 24px;
  overflow: hidden;
  transition: 0.5s;
}

.nav-link:hover {
  background: #03e9f4;
  color: #050801;
  box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
    0 0 200px #03e9f4;
}

.nav-link span {
  position: absolute;
  display: block;
}

.nav-link span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #03e9f4);
  animation: animate1 1s linear infinite;
}

@keyframes animate1 {
  0% {
    left: -100%;
  }

  50%,
  100% {
    left: 100%;
  }
}

.nav-link span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #03e9f4);
  animation: animate2 1s linear infinite;
  animation-delay: 0.25s;
}

@keyframes animate2 {
  0% {
    top: -100%;
  }

  50%,
  100% {
    top: 100%;
  }
}

.nav-link span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #03e9f4);
  animation: animate3 1s linear infinite;
  animation-delay: 0.5s;
}

@keyframes animate3 {
  0% {
    right: -100%;
  }

  50%,
  100% {
    right: 100%;
  }
}

.nav-link span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #03e9f4);
  animation: animate4 1s linear infinite;
  animation-delay: 0.75s;
}

@keyframes animate4 {
  0% {
    bottom: -100%;
  }

  50%,
  100% {
    bottom: 100%;
  }
}

.router-link-active {
  background: #07bcc6;
  color: #050801;
  box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
    0 0 200px #03e9f4;
}

/* a {
    position: relative;
    display: inline-block;
    padding: 25px 30px;
    margin: 40px 0;
    color: #03e9f4;
    text-transform: uppercase;
    letter-spacing: 4px;
    text-decoration: none;
    font-size: 24px;
    overflow: hidden;
    transition: 0.5s;
}

a:hover{
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4,
        0 0 25px #03e9f4,
        0 0 50px #03e9f4,
        0 0 200px #03e9f4;
}

a span {
    position: absolute;
    display: block;
}

a span:nth-child(1) {
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

@keyframes animate1 {
    0% {
        left: -100%;
    }

    50%,
    100% {
        left: 100%;
    }
}

a span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg, transparent, #03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}

@keyframes animate2 {
    0% {
        top: -100%;
    }

    50%,
    100% {
        top: 100%;
    }
}

a span:nth-child(3) {
    bottom: 0;
    right: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.5s;
}

@keyframes animate3 {
    0% {
        right: -100%;
    }

    50%,
    100% {
        right: 100%;
    }
}

a span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg, transparent, #03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}

@keyframes animate4 {
    0% {
        bottom: -100%;
    }

    50%,
    100% {
        bottom: 100%;
    }
} */
</style>

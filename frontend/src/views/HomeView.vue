<script setup>
</script>
<template>
  <div class="container my-5">
    <div class="row">
      <div class="d-flex justify-content-around">
        <div class="text-center text pt-2">
          <p>
            Привет! Я Сергей Бойцов.<br />
            Начинающий fullstack разработчик.
          </p>
          <p>На этом сайте представлены мои пет-проекты,
            статьи и вся контактная информация.
          </p>
        </div>
        <div>
          <img width="500" height="auto" src="/avatar.png" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
img{
  filter: brightness(1.2);
}
.text {
  font-size: 2rem;
  color: #f8fafa;
  text-shadow: 0 0 5px #03e9f4;
  animation: animate 1.5s linear infinite alternate;
}

@keyframes animate {
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
}
</style>

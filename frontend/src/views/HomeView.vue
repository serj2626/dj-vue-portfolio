<script setup></script>
<template>

    <div class="home">
        <div class="h-100 d-flex flex-column justify-content-center align-items-center">
        <p class="text-center text">Привет!
            Я Сергей Бойцов.<br>
            Начинающий fullstack разработчик.
        </p>

        </div>
    </div>



</template>

<style scoped>
.home  {
    width: 100%;
    height: 70vh;
    background: linear-gradient(90deg, #2c3136, #03e9f4);
}
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.text{
    font-size: 2rem;
    color: #690175;
    text-shadow: 0 0 5px #03e9f4;
    animation: animate 1.5s linear infinite;

}
</style>
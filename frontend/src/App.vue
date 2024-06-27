<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue'
import Footer from './components/Footer.vue';
import { useDark, useToggle } from '@vueuse/core';

</script>

<template>
  <div class="app">
    <header>
      <Navigation />
    </header>

    <main>
      <RouterView />
    </main>
    <!-- <footer>
      <Footer />
    </footer> -->
  </div>

</template>

<style scoped>
.app {
  min-height: 100vh;
  /* background-color: #2c3136; */
  background-color: #1b1e20;
}

button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  color: white;
  font-size: 22px;
}

footer {
  /* position: absolute;
  bottom: 0; */
  /* width: 100%;
  height: 80px; */
}

</style>

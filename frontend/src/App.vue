<script setup>
import { RouterLink, RouterView } from "vue-router";
import Navigation from "./components/Navigation.vue";
import Footer from "./components/Footer.vue";
import { useDark, useToggle } from "@vueuse/core";
</script>

<template>
  <div class="app">
    <header>
      <Navigation />
    </header>

    <main>
      <div class="container-fluid py-1">
        <div class="row">
          <div class="info my-5 mx-auto">
            <RouterView />
            <!-- <router-view v-slot="{ Component }">

                <transition name="route" mode="out-in">
                  <component :is="Component" />
                </transition>
 
            </router-view> -->
          </div>
        </div>
      </div>
    </main>

    <footer>
      <Footer />
    </footer>
  </div>
</template>

<style scoped>
/* ///////   Animation  ПЛАВНОЕ ПОЯВЛЕНИЕ РОУТЕРА  ////////////// */

.route-enter-from {
  opacity: 0;
  transform: translateY(200px);
  scale: 0.5;
}

/* .route-enter-to {
  opacity: 1;
  transform: translateY(0);
  scale: 1;
} */

.route-enter-active {
  transition: all 0.9s ease;
}

/* .route-leave-from {
  opacity: 1;
  transform: translateY(0);
  scale: 1;
} */

.route-leave-to {
  opacity: 0;
  transform: translateY(-200px);
}

.route-leave-active {
  transition: all 0.3s ease;
}


/* ///////////////////// */
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

.info {
  padding-block: 10px;
  width: 90%;
  min-height: 90vh;
  border: none;
  border-radius: 20px;
  background-color: #23272a;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
}

footer {
  width: 100%;
  height: 80px;
}
</style>

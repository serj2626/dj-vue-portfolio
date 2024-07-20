<script setup>
import { gsap } from "gsap";

defineProps({
  about: String,
});



const beforeEnter = (el) => {
  console.log("before Enter");
  el.style.transform = "translateY(-180px)";
  el.style.opacity = 0;
};

const enter = (el, done) => {
  console.log("enter");

  gsap.to(el, {
    opacity: 1,
    duration: 3,
    y: 0,
    ease: "bounce.out",
    onComplete: done,
  });
};

const afterEnter = (el) => {
  console.log("after Enter");
};
</script>

<template>
  <p class="about__title fs-1 text-white">О себе</p>
  <div class="row my-5">
    <transition
      @before-enter="beforeEnter"
      @enter="enter"
      @after-enter="afterEnter"
      appear
    >
      <p class="fs-5 text-white about__text" v-html="about"></p>
    </transition>
  </div>
</template>
<style scoped>
.about__title {
  text-shadow: 3px 3px 3px #f5b80f95;
  text-align: center;
}

.about__text {
  letter-spacing: 1px;
  line-height: 1.5;
}
</style>

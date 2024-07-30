<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
const skills = ref([]);

const getSkills = async () => {
  const response = await axios.get("/api/skills/");
  skills.value = response.data;
};

onMounted(() => {
  getSkills();
});


import { gsap } from "gsap";


const beforeEnter = (el) => {
  el.style.opacity = 0;
  el.style.transform = "translateY(160px)";
};
const enter = (el, done) => {
  gsap.to(el, {
    opacity: 1,
    y: 0,
    duration: 1.8,
    onComplete: done,
    delay: el.dataset.index * 0.4,
    // ease: "bounce.out",
  });
};
const afterEnter = (el) => {
  gsap.to(el, {
    opacity: 1,
    duration: 0.5,
  });
};

</script>

<template>
  <p class="fs-1 text-white mb-5 skills__title">Навыки</p>

  <div class="w-50 mx-auto ">
    <transition-group
      @before-enter="beforeEnter"
      @enter="enter"
      @after-enter="afterEnter"
      appear
      name="list"
      tag="ul"
      class="skills__list"
    >
      <li v-for="(skill, index) in skills" :key="index" :data-index="index">
        {{ skill.title }}
      </li>
    </transition-group>

    <!-- <ul class="skills__list" v-for="skill in skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul> -->
  </div>
</template>
<style scoped>
.skills__title {
  text-shadow: 3px 3px 3px #f5e60f95;
}
.skills__list {
  height: 40px;
  font-size: 20px;
  color: white;
  padding: 0;
  transition: all 0.3s ease-in;
  animation: show-skills 1s ease-in;
}

.skills__list li {
  text-align: start;
  margin-block: 10px;
}

/* @keyframes show-skills {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateY(160px);
  }
  100% {
    opacity: 1;
  }
} */
</style>

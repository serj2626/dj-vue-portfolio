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
</script>

<template>
  <p class="fs-1 text-white mb-5 skills__title">Навыки</p>

  <div class="w-50 mx-auto">
    <ul class="skills__list" v-for="skill in skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul>
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
  font-family: "Times New Roman", Times, serif;

}

.skills__list li {
  text-align: start;
  transition: all 0.3s ease-in;
  animation: show-skills 1s ease-in;

  &:hover,
  :hover::marker {
    cursor: auto;
    transform: translateX(60px);
    scale: 1.2;
    text-shadow: 2px 2px 3px #f5e60f95;
  }
}

@keyframes show-skills {
  0% {
    opacity: 0;
    transform: translateY(260px);
  }
  100% {
    opacity: 1;
  }

}
</style>

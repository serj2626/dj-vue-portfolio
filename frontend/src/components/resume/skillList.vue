<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
const skills = ref([]);

const getSkills = async () => {
  const response = await axios.get('/api/skills/');
  skills.value = response.data;
}

onMounted(() => {
  getSkills();
})

</script>

<template>

  <p class="fs-1 text-white mb-5 skills-title">Навыки</p>


  <div class="w-50 mx-auto">
    <ul class="skill-list" v-for="skill in skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul>
  </div>

</template>
<style scoped>

.skills-title {
  text-shadow: 3px 3px 3px #f5e60f95;
}
.skill-list {
  height: 40px;
  font-size: 20px;
  color: white;
  padding: 0;
  font-family: "Times New Roman", Times, serif;
}

.skill-list li {
  transition: all 0.8s ease-in;
  text-align: start;

  &:hover,
  :hover::marker {
    cursor: pointer;
    transform: translateX(60px);
    color: #f5e60f;
  }
}
</style>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  experience: Array,
});

console.log(props.experience);

const showExperience = ref(null);

const updateShow = (id) => {
  if (showExperience.value === id) {
    showExperience.value = null;
  } else {
    showExperience.value = id;
  }
}
</script>

<template>
  <p class="fs-1 text-white">Опыт работы</p>
  <div class="w-75 mx-auto my-5" v-for="obj in props.experience" :key="obj.id">


    <div class="experience">
      <p>{{ obj.vacancy_title }}</p>
      <button @click="updateShow(obj.id)" class="btn btn-outline-dark">
        <i class="fa-solid fa-arrow-down fa-xl" style="color: #f5b80f;"></i>
      </button>
    </div>

    <article v-show="showExperience === obj.id">
      <p v-html="obj.responsibilities"></p>
    </article>
  </div>

</template>
<style scoped>
.experience {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-inline: 10px;
  font-size: 20px;
  color: white;
  font-family: 'Times New Roman', Times, serif;
  background: #42494f;
  margin-bottom: 15px;
  cursor: auto;
  height: 60px;
  transition: all 0.8s ease;
}

article {
 color: white;
 font-size: 20px;
 font-family: serif;
 text-align: start;

 border-radius: 10px;
 padding: 20px;
 height: 500px;
 overflow: auto;
 transition: all 0.8s ease;
}
</style>

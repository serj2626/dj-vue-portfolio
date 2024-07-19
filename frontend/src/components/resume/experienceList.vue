<script setup>
import { ref } from "vue";

const props = defineProps({
  experience: Array,
});

const showExperience = ref(null);

const updateShow = (id) => {
  if (showExperience.value === id) {
    showExperience.value = null;
  } else {
    showExperience.value = id;
  }
};
</script>

<template>
  <p class="experience__title fs-1 text-white">Опыт работы</p>
  <div class="w-75 mx-auto my-5" v-for="obj in props.experience" :key="obj.id">
    <div class="experience d-flex align-items-center">

        <p>{{ obj.vacancy_title }}</p>

      <div>
        <button
          v-if="showExperience === obj.id"
          @click="updateShow(obj.id)"
          class="btn btn-outline-dark"
        >
          <i class="fa-solid fa-arrow-up fa-xl" style="color: #f5b80f"></i>
        </button>
        <button v-else @click="updateShow(obj.id)" class="btn btn-outline-dark">
          <i class="fa-solid fa-arrow-down fa-xl" style="color: #f5b80f"></i>
        </button>
      </div>
    </div>
    <transition name="fade">
      <article class="" v-show="showExperience === obj.id">
        <p v-html="obj.responsibilities"></p>
      </article>
    </transition>
  </div>
</template>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.9s ease-in;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.experience__title {
  text-shadow: 3px 3px 3px #f5e60f95;
}

.experience {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-inline: 10px;
  font-size: 20px;
  color: white;
  font-family: "Times New Roman", Times, serif;
  background: #42494f;
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
  scrollbar-color: #f5b80f #2e2b2c;
  scrollbar-width: thin;
  transition: all 0.8s ease;
}
</style>

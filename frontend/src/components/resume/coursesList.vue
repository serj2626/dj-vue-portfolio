<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const courses = ref([]);

const getCourses = async () => {
  const response = await axios.get("/api/courses/");
  courses.value = response.data;
  console.log(courses.value);
};

onMounted(() => {
  getCourses();
});
</script>

<template>
  <p class="courses__title fs-1 text-white">Курсы</p>
  <div class="row mt-5 w-75 mx-auto">
    <div class="d-flex gap-3">
      <div class="card" v-for="course in courses" :key="course.id">
        <div
          class="card-img-top d-flex flex-column justify-content-center align-items-center h-50"
        >
          <img class="py-2 course__img" :src="course.img" alt="" />
        </div>

        <div class="card-body h-50 d-flex flex-column justify-content-center">
          <h3>{{ course.title }}</h3>
          <p v-html="course.description" class="card-text"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  height: 350px;
  box-sizing: border-box;
  box-shadow: 0 0 10px 0 rgb(86, 209, 186);
  transition: all 0.3s ease;
  &:hover {
    transform: scale(0.9);
  }
}

.courses__title {
  font-size: 3rem;
  color: white;
  text-shadow: 3px 3px 3px #f5b80f95;
}

.course__img {
  width: 50%;
  height: auto;
}
</style>

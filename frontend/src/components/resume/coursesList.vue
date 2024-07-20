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

    <div class="card col-5 mx-3" v-for="course in courses" :key="course.id">
        <div class="card-header h-25"><h4>{{ course.title }}</h4>{{ course.company }}</div>
        <div class="card-body h-50">
            <img class="w-75 h-75 py-2" :src="course.img" alt="">
        </div>
        <div class="card-footer h-25">
            <p v-html="course.description" class="card-text"></p>
        </div>
      <!-- <img
        :src="course.img"
        class="card-img-top h-50 w-auto"
        :alt="course.title"
      />
      <div class="card-body">
        <h5 class="card-title">{{ course.title }}</h5>
        <p v-html="course.description" class="card-text"></p>
      </div> -->
    </div>
  </div>
</template>

<style scoped>
.card {
  height: 350px;
  box-sizing: border-box;
  box-shadow: 0 0 20px 0 rgb(189, 241, 240);
}

.courses__title {
  font-size: 3rem;
  color: white;
  text-shadow: 3px 3px 3px #f5b80f95;
}
</style>

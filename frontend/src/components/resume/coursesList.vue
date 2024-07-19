<script setup>
import axios from 'axios';
import {ref, onMounted} from 'vue';

const courses = ref([]);

const getCourses = async () => {
    const response = await axios.get('/api/courses/');
    courses.value = response.data;
    console.log(courses.value);
}

onMounted(() => {
    getCourses();
})
</script>

<template>
    <p class="courses__title fs-1 text-white">Курсы</p>
    <div class="row mt-5" v-for="course in courses" :key="course.id">

            <div class="card col-4" >
                <img :src="course.img" class="card-img-top" :alt="course.title">
                <div class="card-body">
                    <h5 class="card-title">{{ course.title }}</h5>
                    <p v-html="course.description" class="card-text"></p>
                </div>
            </div>
  
    </div>
</template>

<style scoped>
.card{
    height: 450px;
    box-sizing: border-box;
}


.courses__title {
    font-size: 3rem;
    color: white;
    text-shadow: 3px 3px 3px #f5b80f95;
}

</style>
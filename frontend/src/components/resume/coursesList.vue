<script setup>
const url = 'http://127.0.0.1:8000'
const props = defineProps({
    courses: Array
})

console.log(props.courses);
</script>

<template>
    <p class="courses__title fs-1 text-white">Курсы</p>
    <div class="row mt-5" v-for="course in props.courses" :key="course.id">

            <div class="card col-4" >
                <img :src="url + course.img" class="card-img-top" :alt="course.title">
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
<script setup>
const props = defineProps({
    courses: Array
})

console.log(props.courses);
</script>

<template>
    <p class="courses__title fs-1 text-white">Курсы</p>
    <div class="row">
        <div v-for="course in props.courses" :key="course.id">
            <div class="btn-about w-75 mx-auto">
                <p>{{ course.title }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>

.courses__title {
  font-size: 3rem;
  color: white;
  text-shadow: 3px 3px 3px #f5b80f95;
}


.btn-about {
    padding: 10px;
    border-radius: 10px;
    margin-block: 10px;
    font-size: 20px;
    color: white;
    font-family: serif;
    background: #42494f;
    cursor: auto;
    transition: all 0.8s ease;

    &:hover {
        scale: 1.1;
    }

}

.btn-about span {
    font-size: 30px;
}
</style>
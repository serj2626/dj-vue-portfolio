<script setup>
const props = defineProps({
    courses: Array
})
</script>

<template>
    <div>

        <div v-for="course in props.courses" :key="course.id">
            <div class="btn-about w-75 mx-auto">
                <p>{{ course.title }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
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

    &:hover{
        scale: 1.1;
    }

}

.btn-about span {
    font-size: 30px;
}
</style>
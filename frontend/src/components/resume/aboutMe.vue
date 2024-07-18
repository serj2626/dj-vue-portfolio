<script setup>

defineProps({
    about: String
})
</script>


<template>

    <p class="about__title fs-1 text-white">О себе</p>
    <div class="row my-5 w-75 mx-auto">
        <p class=" fs-5 text-white text-start" v-html="about"></p>
    </div>


</template>
<style scoped>
.about__title {
    text-shadow: 3px 3px 3px #f5b80f95;
    text-align: center;
}
</style>
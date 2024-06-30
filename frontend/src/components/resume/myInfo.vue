<script setup>

const props = defineProps({
    user: Object
})
</script>
<template>
    <div>
        <i class="fs-2 text-white">{{ props.user.name }} {{ props.user.surname }}</i><br>
        <i class="fs-2 text-white">{{ props.user.position }}</i><br>
        <i class="fs-2 text-white">Санкт-Петербург</i>
    </div>
    <div class="flex justify-content-center align-items-center mt-5">
        <i class="fa-brands fa-github fa-2xl" style="color: red;"></i>
        <i class="fa-brands fa-telegram fa-2xl" style="color: #74C0FC;"></i>
        <i class="fa-brands fa-instagram fa-2xl" style="color: #FFD43B;"></i>
        <i class="fa-brands fa-vk fa-2xl" style="color: #74C0FC;"></i>
        <i class="fa-brands fa-linkedin fa-2xl" style="color: #74C0FC;"></i>
    </div>

</template>

<style scoped>
.fa-brands {
    color: #74C0FC;
    width: 70px;
    height: 70px;
}
</style>
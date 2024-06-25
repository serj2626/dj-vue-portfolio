<script setup>

const props = defineProps({
    user: Object
})
</script>


<template>
    <div class="d-flex flex-column justify-content-around align-items-center text-white fs-5">
        <p>{{ user.surname }} {{ user.name }}</p>
        <hr />
        <p>{{ user.position }}</p>
        <hr />
        <p>{{ user.min_salary }} - {{ user.max_salary }}</p>
        <hr />
        <p>{{ user.github_url }}</p>
        <hr />
    </div>
</template>
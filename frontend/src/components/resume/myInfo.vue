<script setup>

const props = defineProps({
    user: Object
})
</script>


<template>
    <ul>
        <li>
            <i class="fa-solid fa-user fa-xl" style="color: #63E6BE;"></i>
            <span class="fs-2 text-white">
                {{ user.surname }} {{ user.name }}
            </span>
        </li>
        <li>
            <i class="fa-solid fa-computer fa-xl" style="color: #63E6BE;"></i>
            <span class="fs-2 text-white">
                {{ user.position }}
            </span>
        </li>
        <li>
            <i class="fa-solid fa-money-bill fa-xl" style="color: #63E6BE;"></i>
            <span class="fs-2 text-white">
                {{ user.min_salary }} - {{ user.max_salary }}
            </span>
        </li>
        <li>
            <i class="fa-brands fa-github fa-xl" style="color: #63E6BE;"></i>
            <span class="fs-2 text-white">
                <a :href="user.github_url">github_url</a>
            </span>
        </li>

    </ul>
</template>

<style scoped>

ul{
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
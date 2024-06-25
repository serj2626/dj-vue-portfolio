<script setup>

const props = defineProps({
    skills: Array
})
</script>


<template>
    <div
          v-if="showInfo === 3"
          class="d-flex flex-column justify-content-around align-items-center text-white fs-5"
        >
          <p>Навыки</p>
          <hr />
          <div v-for="skill in props.skills" :key="skill.id">
            <p>{{ skill }}</p>
            <hr />
          </div>
        </div>
</template>
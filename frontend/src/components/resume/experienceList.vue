<script setup>

const props = defineProps({
    experience: Array
})
</script>


<template>
    <div
          class="d-flex flex-column justify-content-around align-items-center text-white fs-5"
        >
          <p>Опыт работы</p>
          <hr />
          <div v-for="obj in props.experience" :key="obj.id">
            <p>{{ obj }}</p>
            <hr />
          </div>
        </div>
</template>
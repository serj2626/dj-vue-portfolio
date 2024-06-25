<script setup>

const props = defineProps({
  experience: Array
})

console.log(props.experience);
</script>


<template>
  <div class="d-flex flex-column justify-content-around align-items-center text-white fs-5">
    <p>Опыт работы</p>

    <div v-for="obj in props.experience" :key="obj.id">
      <div class="card">
        <div class="card-title">
          {{ obj.vacancy_title }}
        </div>
        <div class="card-text">
          <p v-html="obj.responsibilities"></p>
        </div>
      </div>
    </div>
  </div>
</template>
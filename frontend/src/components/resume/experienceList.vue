<script setup>

const props = defineProps({
  experience: Array
})

console.log(props.experience);
</script>


<template>
  <div class="text-white">
    <p>Опыт работы</p>

    <div class="card-text" v-for="obj in props.experience" :key="obj.id">
      {{ obj.vacancy_title }}
      <p class="card-text" v-html="obj.responsibilities"></p>
    </div>
  </div>

</template>
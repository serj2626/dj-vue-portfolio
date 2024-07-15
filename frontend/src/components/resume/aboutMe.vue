<script setup>

defineProps({
    about: String
})
</script>


<template>

          <p class="fs-1 text-white">О себе</p>
          <hr />
          <p class=" fs-5 text-white" v-html="about"></p>
     
</template>
<style scoped>

</style>
<script setup>

defineProps({
    about: String
})
</script>


<template>
    <div
          class="d-flex flex-column justify-content-around align-items-center text-white fs-5"
        >
          <p class="fs-2 text">О себе</p>
          <hr />
          <p v-html="about"></p>
        </div>
</template>
<style scoped>

.text{
  color: #03e9f4;
}
</style>
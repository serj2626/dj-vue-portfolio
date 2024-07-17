<script setup>
const props = defineProps({
  skills: Array,
});
console.log(props.skills);
</script>

<template>

  <p class="fs-1 text-white mb-5">Навыки</p>


  <div class="w-50 mx-auto">
    <ul v-for="skill in props.skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul>
  </div>

</template>
<style scoped>
ul {
  height: 40px;
  font-size: 20px;
  color: white;
  padding: 0;
  font-family: "Times New Roman", Times, serif;
}

ul li {
  transition: all 0.5s ease-in;
  text-align: start;

  &:hover,
  :hover::marker {
    cursor: pointer;
    transform: translateX(60px);
    color: #f5e60f;
  }
}
</style>

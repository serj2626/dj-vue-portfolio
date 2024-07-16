<script setup>

const props = defineProps({
  skills: Array
})
console.log(props.skills);
</script>


<template>
<a href="" class="text-white text-decoration-none"></a>
  <p class="fs-1 text-white">Навыки</p>
  <hr />
  <div class="w-75 mx-auto">
    <ul v-for="skill in props.skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul>
  </div>


</template>
<style scoped>
ul {
  /* list-style-type: none; */
  height: 40px;
  padding-block: 10px;
  font-size: 20px;
  color: white;
  font-family: 'Times New Roman', Times, serif;
  /* background: #42494f; */
  cursor: auto;
  transition: all 0.8s ease;

  &:hover{
    transform: scale(1.1);
  }

  &::marker {
    color: #f5b80f;
  }
}
</style>
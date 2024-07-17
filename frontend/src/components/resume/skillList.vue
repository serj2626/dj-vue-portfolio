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
  <div class="w-50 mx-auto">
    <ul v-for="skill in props.skills" :key="skill.id">
      <li>{{ skill.title }}</li>
    </ul>
  </div>


</template>
<style scoped>
ul {
  /* list-style-type: none; */
  height: 40px;
  font-size: 20px;
  color: white;
  padding: 0;
  font-family: 'Times New Roman', Times, serif;
}

ul li{
  transition: all 0.6s ease-in;
  text-align: start;



  &:hover{
    cursor: pointer;
    transform: translateX(150px);
    color: #f5b80f;
  }

  &:hover:marker{
    color: #f5b80f;
  }
}
</style>
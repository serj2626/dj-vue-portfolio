<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";


const router = useRouter();
const projects = ref([]);

const getProjects = async () => {
  const response = await axios.get("/api/projects/");
  projects.value = response.data;
  console.log(projects.value);
};

onMounted(() => {
  getProjects();
});
</script>

<template>

  <div class="row my-5">

    <div class="w-75 mx-auto">


      <div v-for="project in projects" :key="project.id" 
      class="d-flex align-items-center justify-content-between mb-5">
        <h4 class="title">{{ project.title }}</h4>
        <div class="list-stack" v-for="stack in project.stack" :key="stack.id">
          <img width="35" height="auto" class="logo-stack" :src="stack.img" :alt="stack.title" :title="stack.title" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.title {
  color: #03e9f4;
  text-shadow: 0 0 2px wheat;
}
</style>

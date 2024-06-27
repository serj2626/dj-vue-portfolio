<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const stacks = ref([]);
const projects = ref([]);

const getStacks = async () => {
  const response = await axios.get("/api/stacks/");
  console.log(response.data);
  stacks.value = response.data;
};

const getProjects = async () => {
  const response = await axios.get("/api/projects/");
  console.log(response.data);
  projects.value = response.data;
};

onMounted(() => {
  getStacks();
  getProjects();
});
</script>

<template>
  <div class="container py-5">
    <div class="row">
      <p class="fs-1 title text-center my-5">Проекты</p>
      <div class="col-4" v-for="project in projects" :key="project.id">
        <div
        @click="router.push({ name: 'project', params: { slug: project.slug } })"
        class="card" style="width: 26rem; height: 25rem">
          <img
            :src="project.avatar"
            class="card-img-top h-75"
            :alt="project.title"
            :title="project.title"
          />
          <div class="card-body">
            <h5 class="card-title">{{ project.title }}</h5>
          </div>
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

.card {
  cursor: pointer;
  overflow: hidden;
  transition: 0.5s all ease-in-out;


  &:hover {
    transform: scale(1.1);
  }
}
</style>

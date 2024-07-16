<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();
const props = defineProps({
  slug: String,
});

const project = ref({});

const getProject = async () => {
  try {
    const res = await axios.get(`/api/projects/${props.slug}/`);
    project.value = res.data;
    console.log(project.value);
  } catch {
    toast.error("Что-то пошло не так");
  }
};

onMounted(() => {
  getProject();
});
</script>

<template>

  <div class="row">
    <p class="fs-1 py-3 title1">{{ project.title }}</p>
  </div>
  <div class="d-flex align-items-center justify-content-center gap-5 mb-5">
    <img class="img-stack" v-for="stack in project.stack" :src="stack.img" :alt="stack.title" :title="stack.title">
  </div>
  <div class="row">
    <img class="rounded-4 w-75 mx-auto img-ava" :src="project.avatar" :alt="project.title" :title="project.title" />
  </div>


  <div class="row mt-5 text-white">
    <p v-html="project.description"></p>
  </div>
  <div class="row">
    <a class="text-white text-decoration-none" :href="project.url" target="_blank">Исходный код</a>
  </div>

</template>

<style scoped>
.img-stack {
  width: 60px;
  height: auto;
}

.img-ava{
 filter: brightness(1.1);
}

.title1 {
  color: #fa0aee;
  text-align: center;
}
</style>

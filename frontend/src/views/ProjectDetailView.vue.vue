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
    console.log(res.data);
    project.value = res.data;
  } catch {
    toast.error("Что-то пошло не так");
  }
};

onMounted(() => {
  getProject();
});
</script>

<template>
  <div class="container py-5">
    <div class="row">
      <div
        class="project d-flex flex-column justify-content-between align-items-center text-white fs-5"
      >
        <p class="fs-1 py-3 title">{{ project.title }}</p>
        <img
          class="rounded-4"
          :src="project.avatar"
          :alt="project.title"
          :title="project.title"
        />
        <div>
          <p v-html="project.description"></p>
        </div>
        <div class="" v-for="stack in project.stack" :key="stack.id">
            <div class="col">
            <button class="btn btn-outline-light">{{ stack.title }}</button>    
            </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 80%;
  height: auto;
  shape-outside: circle(50%);
}

.title {
  color: #fa0aee;
  text-align: center;
}
</style>

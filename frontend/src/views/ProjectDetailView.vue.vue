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
  <p class="fs-1 py-3 project__title">{{ project.title }}</p>

  <div class="row my-5">
    <div class="d-flex align-items-center justify-content-center gap-5 mb-5">
      <img
        class="img-stack"
        v-for="stack in project.stack"
        :src="stack.img"
        :alt="stack.title"
        :title="stack.title"
      />
    </div>
    <div class="row">
      <img
        class="w-75 mx-auto project__avatar"
        :src="project.avatar"
        :alt="project.title"
        :title="project.title"
      />
    </div>

    <div class="row my-5 text-white">
      <div class="w-75 mx-auto position-relative">
        <p v-html="project.description"></p>
        <a
          class="text-decoration-none project__url position-absolute bottom-0 end-0"
          :href="project.url"
          target="_blank"
          >Исходный код</a
        >
      </div>
    </div>
  </div>

</template>

<style scoped>
.img-stack {
  width: 60px;
  height: auto;
  box-shadow: 0 0 10px #03e9f4;
  cursor: pointer;
  box-sizing: border-box;
  padding: 10px;
  object-fit: cover;
  transition: box-shadow 0.23s ease-in;

  &:hover {
    box-shadow: 0 0 10px #03e9f4, 0 0 20px #03e9f4, 0 0 30px #03e9f4,
      0 0 40px #03e9f4, 0 0 50px #03e9f4, 0 0 60px #03e9f4, 0 0 70px #03e9f4;
  }
}

.project__avatar {
  filter: brightness(1.1);
  border-radius: 6px;
}

.project__title {
  color: white;
  text-shadow: 3px 3px 3px #f5b80f95;
  text-align: center;
}

.project__url {
  color: #f7ff0c;
}
</style>

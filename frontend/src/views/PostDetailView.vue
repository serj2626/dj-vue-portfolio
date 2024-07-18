<script setup>
import axios from "axios";
import { onMounted, ref, defineProps } from "vue";

const props = defineProps({
  id: String,
});
const post = ref({});

const getPost = async () => {
  const response = await axios.get(`/api/posts/${props.id}/`);
  post.value = response.data;
  console.log(post.value);
};

onMounted(() => {
  getPost();
});
</script>

<template>
  <div class="text-white w-75 mx-auto p-5">
    <h1 class="text-center mb-5">{{ post.title }}</h1>
    <p v-html="post.content"></p>
  </div>
</template>

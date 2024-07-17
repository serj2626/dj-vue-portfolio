<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";


const router = useRouter();
const posts = ref([]);

const getProjects = async () => {
  const response = await axios.get("/api/posts/");
  posts.value = response.data;
  console.log(posts.value);
};

onMounted(() => {
  getProjects();
});
</script>

<template>
  <h1 class="title my-5">Посты</h1>

  <div class="row w-75 mx-auto">

    <article v-for="post in posts" :key="post.id">
      <div class="post">
        <RouterLink :to="{ name: 'post', params: { id: post.id } }">
          {{ post.title }}
        </RouterLink>
        
      </div>
    </article>

  </div>

</template>

<style scoped>
.title {
  color: #f6f6f6cb;
  text-shadow: 0 0 2px wheat;
  text-align: center;
}

.post{
  color: white;
  width: 50%;
  background: linear-gradient(to right, #1b5976, #8f215f);
  border-radius: 10px;
  font-size: 22px;
  padding: 10px 15px;
  margin: 10px;
  margin: 0 auto;
}
</style>

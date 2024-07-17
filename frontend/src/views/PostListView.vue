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
      <div class="card w-50">
        <div class="card-body">
          <h5 class="card-title">{{ post.title }}</h5>
          <RouterLink :to="{ name: 'post', params: { id: post.id } }">
            <a href="#" class="btn btn-primary">Читать</a>
          </RouterLink>
        </div>
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

.card {
  background: linear-gradient(45deg, #03e9f4, #10d569,#fdde42);
}
</style>

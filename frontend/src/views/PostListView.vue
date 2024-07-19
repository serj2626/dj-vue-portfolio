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
  <h1 class="post__title fs-1">Посты</h1>

  <div class="row">
    <div class="d-flex justify-content-center gap-5 flex-wrap">
      <article class="card position-relative col-md-3 py-3 px-2" v-for="post in posts" :key="post.id">
        <div class="card-body">
          <h5 class="card-title">{{ post.title }}</h5>
          <RouterLink :to="{ name: 'post', params: { id: post.id } }">
            <button class="btn btn-dark">Читать</button>
          </RouterLink>
        </div>
      </article>
    </div>

  </div>



</template>

<style scoped>
.post__title {
  color:  white;
  text-shadow: 3px 3px 3px #f5e60f95;
  font-weight: 700;
  text-align: center;
  margin-bottom: 100px;
  margin-top: 50px;
}

.card {
  background: linear-gradient(45deg, #03e9f4, #10d569, #fdde42);
  border: 2px solid white;
  box-sizing: border-box;
  cursor: pointer;
  min-height: 150px;
  transition: all 0.3s ease-in;
  box-shadow:  0 0 35px #fdfdfd;

  &:hover {
    transform: scale(1.1);
 
  }
}

.card-title {
  color: rgba(0, 0, 0, 0.629);
  font-weight: 700;
  text-shadow: 0 0 2px wheat;
}

.btn{
  position: absolute;
  bottom: 0;
  right: 0;
  margin-right: 10px;
  margin-bottom: 5px;
}
</style>

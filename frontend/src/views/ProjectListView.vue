<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import { EffectCoverflow, Pagination } from "swiper/modules";
import "swiper/css/effect-coverflow";
import "swiper/css/pagination";

const modules = [EffectCoverflow, Pagination];

const router = useRouter();
const projects = ref([]);

const getProjects = async () => {
  const response = await axios.get("/api/projects/");
  projects.value = response.data;
};

onMounted(() => {
  getProjects();
});
</script>

<template>
  <swiper
    :effect="'coverflow'"
    :grabCursor="true"
    :centeredSlides="true"
    :slidesPerView="'auto'"
    :coverflowEffect="{
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    }"
    :pagination="true"
    :modules="modules"

    class="mySwiper"
  >
    <swiper-slide v-for="project in projects" :key="project.id">
      <div
        @click="
          router.push({ name: 'project', params: { slug: project.slug } })
        "
        class="card"
      >
        <img
          :src="project.avatar"
          class="card-img-top"
          :alt="project.title"
          :title="project.title"
        />
        <div class="card-body">
          <h5 class="card-title text-center">{{ project.title }}</h5>
        </div>
      </div>
    </swiper-slide>
  </swiper>
</template>

<style scoped>
.swiper {
  width: 100%;
  padding-top: 150px;
  padding-bottom: 150px;
}

.swiper-slide {
  background-position: center;
  background-size: cover;
  width: 600px;
  height: 500px;
}
.card {
  width: 600px;
  height: 500px;
}
.swiper-slide img {
  display: block;
  height: 100%;
  width: 100%;
}

.title {
  color: #03e9f4;
  text-shadow: 0 0 2px wheat;
}
</style>

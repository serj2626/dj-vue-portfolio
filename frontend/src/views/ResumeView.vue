<script setup>
import axios from "axios";
import { onMounted, reactive, ref } from "vue";
import { useToast } from "vue-toastification";
import myInfo from "../components/resume/myInfo.vue";
import experienceList from "../components/resume/experienceList.vue";
import coursesList from "../components/resume/coursesList.vue";
import skillList from "../components/resume/skillList.vue";
import aboutMe from "../components/resume/aboutMe.vue";

const toast = useToast();
const showInfo = ref(4);

const addShowInfo = (data) => {
  showInfo.value = data;
};

const user = reactive({
  name: "",
  surname: "",
  position: "",
  min_salary: "",
  max_salary: "",
  github_url: "",
  avatar: "",
});

const experience = ref([]);
const courses = ref([]);
const skills = ref([]);
const stacks = ref([]);
const about = ref("");

const getResume = async () => {
  try {
    const res = await axios.get("/api/resume/");

    about.value = res.data.about;
    console.log(res.data);
  } catch (error) {
    toast.error("Что-то пошло не так");
  }
};
onMounted(() => getResume());
</script>

<template>
  <div class="d-flex justify-content-center pb-5">
    <a
      class="btn-info"
      :class="{ active: showInfo === 4 }"
      @click="addShowInfo(4)"
      >Контакты</a
    >
    <a
      class="btn-info"
      :class="{ active: showInfo === 3 }"
      @click="addShowInfo(3)"
      >Навыки</a
    >
    <a
      class="btn-info"
      :class="{ active: showInfo === 2 }"
      @click="addShowInfo(2)"
      >Опыт работы</a
    >
    <a
      class="btn-info"
      :class="{ active: showInfo === 5 }"
      @click="addShowInfo(5)"
      >Курсы</a
    >
    <a
      class="btn-info"
      :class="{ active: showInfo === 1 }"
      @click="addShowInfo(1)"
      >О себе</a
    >
  </div>

  <div class="row mx-auto text-center">
    <div class="col-4 position-relative">
      <img src="/avatar.png" class="ava rounded-5" alt="avatar" />
    </div>
    <div class="col-8">
      <aboutMe v-if="showInfo === 1" :about="about" />
      <experienceList v-else-if="showInfo === 2" :experience="experience" />
      <skillList v-else-if="showInfo === 3" :skills="skills" />
      <myInfo v-else-if="showInfo === 4" :user="user" />
      <coursesList v-else-if="showInfo === 5" :courses="courses" />
    </div>
  </div>
</template>

<style scoped>
.ava {
  transform: rotate3d(0, 1, 0, 180deg);
  filter: brightness(1.1);
  width: 80%;
  height: auto;
  margin: 30px;
  /* box-shadow: 0 0 10px #03e9f4, 0 0 20px #03e9f4, 0 0 30px #03e9f4,
  0 0 40px #03e9f4, 0 0 50px #03e9f4, 0 0 60px #03e9f4, 0 0 70px #03e9f4; */
  box-shadow: 0 0 30px 20px #03e9f4;
  cursor: pointer;
}
/* img{
  transition: all 0.8s ease ;
}
img:hover{
  cursor: pointer;
  transform: translate3d(0, -10px, 0);  
} */

.btn-info {
  color: white;
  text-decoration: none;
  margin-inline: 10px;
  font-size: 22px;
  font-weight: bold;
  margin-block: 40px;
  cursor: pointer;
  padding-bottom: 10px;
  border-bottom: 2px solid transparent;

  &:hover {
    color: #03e9f4;
    transition: 0.2s;
    border-bottom: 2px solid #03e9f4;
  }
}

.active {
  color: #03e9f4;
  transition: 0.2s;
  border-bottom: 2px solid #03e9f4;
}
</style>

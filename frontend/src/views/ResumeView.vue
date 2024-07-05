<script setup>
import axios from "axios";
import { onMounted, reactive, ref } from "vue";
import myInfo from "../components/resume/myInfo.vue";
import experienceList from "../components/resume/experienceList.vue";
// import coursesList from "../components/resume/coursesList.vue";
import skillList from "../components/resume/skillList.vue";
import aboutMe from "../components/resume/aboutMe.vue";

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
    console.log(res.data);
    user.name = res.data.name;
    user.surname = res.data.surname;
    user.position = res.data.position;
    user.min_salary = res.data.min_salary;
    user.max_salary = res.data.max_salary;
    user.github_url = res.data.github_url;
    user.avatar = res.data.get_avatar;
    experience.value = res.data.experience;
    courses.value = res.data.course;
    skills.value = res.data.skill;
    stacks.value = res.data.stack;
    about.value = res.data.about;
  } catch (error) {
    console.log("error " + error);
  }
};
onMounted(() => getResume());
</script>

<template>
  <div class="d-flex justify-content-center pb-5 ">
    <a @click="addShowInfo(4)" class="btn-info">Контакты</a>
    <a @click="addShowInfo(3)" class="btn-info">Навыки</a>
    <a @click="addShowInfo(2)" class="btn-info">Опыт работы</a>
    <a @click="addShowInfo(4)" class="btn-info">Курсы</a>
    <a @click="addShowInfo(1)" class="btn-info">О себе</a>
  </div>


  <div class="d-flex justify-content-around">
    <img class="rounded-4" width="400" height="500" :src="user.avatar" alt="avatar" />
    <div>
      <aboutMe v-if="showInfo === 1" :about="about" />
      <experienceList v-else-if="showInfo === 2" :experience="experience" />
      <skillList v-else-if="showInfo === 3" :skills="skills" />
      <myInfo v-else-if="showInfo === 4" :user="user" />
    </div>

  </div>

</template>

<style scoped>
.btn-info {
  color: white;
  text-decoration: none;
  margin-inline: 10px;
  font-size: 22px;
  font-weight: bold;
  margin-block: 40px;
  cursor: pointer;
  padding-bottom: 10px;


  &:hover {
    color: #03e9f4;
    transition: 0.2s;
    border-bottom: 2px solid #03e9f4;
  }
}
</style>

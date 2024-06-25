<script setup>
import axios from "axios";
import { onMounted, reactive, ref } from "vue";
import myInfo from "../components/resume/myInfo.vue";
import experienceList from "../components/resume/experienceList.vue";
// import coursesList from "../components/resume/coursesList.vue";
import skillList from "../components/resume/skillList.vue";
import aboutMe from "../components/resume/aboutMe.vue";

const showInfo = ref(null);

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
  <div class="container">
    <div class="row">
      <div class="left col-md-3 mx-auto">
        <div class="d-flex flex-column justify-content-around align-items-center">
          <img class="rounded-4" :src="user.avatar" alt="avatar" />
          <div class="d-flex">
            <button @click="addShowInfo(3)" class="link">Навыки</button>
            <button @click="addShowInfo(2)" class="link">Опыт работы</button>
            <button @click="addShowInfo(1)" class="link">О себе</button>
          </div>
        </div>
      </div>
      <div class="right col-md-8">
        <aboutMe v-if="showInfo === 1" :about="about" />
        <experienceList v-else-if="showInfo === 2" :experience="experience" />
        <skillList v-else-if="showInfo === 3" :skills="skills" />
        <myInfo v-else :user="user" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin-top: 80px;
}

.link {
  border: none;
  padding: 15px 20px;
  border-radius: 10px;
  margin: 10px;
  background: linear-gradient(90deg, #42494f, #03e9f4);
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.link:hover {
  background: linear-gradient(90deg, #42494f, #01fcca);
}

/* .left {
  height: 70vh;
  width: 30%;
} */

.right {
  min-height: 70vh;
  padding: 0 30px;
  margin-left: 20px;
}
</style>

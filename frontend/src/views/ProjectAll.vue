<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

const stacks = ref([]);
const projects = ref([]);

const getStacks = async () => {
    const response = await axios.get("/api/projects/");
    console.log(response.data);
    stacks.value = response.data;
};
onMounted(() => getStacks());
</script>

<template>
    <div class="container mt-5">
        <div class="row">
            <p class="fs-1 title text-center my-5">
                Используемый стек
            </p>
            <div class="stack col-2" 
            v-for="stack in stacks" 
            :key="stack.id">
                <img class="logo-stack" 
                :src="stack.img" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.stack {
    margin-block: 20px;
}

.logo-stack {
    width: 100px;
    height: 100px;
    cursor: pointer;

    &:hover {
        transform: scale(1.1);
    }
}

.title {
    color: #03e9f4;
    text-shadow: 0 0 2px wheat ;
}
</style>

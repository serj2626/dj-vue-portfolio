<script setup>

const props = defineProps({
    user: Object
})
</script>
<template>
    <p class="contact__title fs-1 text-white">Мои контакты</p>
    <div class="row my-5">
        <div class="d-flex flex-column align-content-center w-50 mx-auto">
            <div class="btn-about">
                <p><span>👨‍🍼 </span>{{ props.user.name }} {{ props.user.surname }}</p>
            </div>
            <div class="btn-about">
                <p><span>👉 </span>{{ props.user.position }}</p>
            </div>
            <div class="btn-about">
                <p><span>☎️ </span>{{ props.user.phone }}</p>
            </div>
            <div class="btn-about">
                <p><span>✉️ </span><a class="text-white text-decoration-none"
                        href="mailto:serj2626@mail.ru">{{ props.user.email }}</a></p>
            </div>
            <div class="btn-about">
                <p><span>🇷🇺 </span>{{ props.user.country }}, {{ props.user.city }}</p>
            </div>
        </div>
    </div>

</template>

<style scoped>
.contact__title {
    text-shadow: 3px 3px 3px #f5b80f95;
}

.btn-about {
    padding: 10px;
    border-radius: 10px;
    margin-block: 10px;
    font-size: 20px;
    color: white;
    font-family: serif;
    background: #42494f;
    cursor: auto;
    transition: all 0.8s ease;

    &:hover {
        scale: 1.1;
    }

}

.btn-about span {
    font-size: 30px;
}
</style>
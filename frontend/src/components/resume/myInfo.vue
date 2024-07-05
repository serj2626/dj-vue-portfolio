<script setup>

const props = defineProps({
    user: Object
})
</script>
<template>
    <ul class="list-unstyled text-white">
        <li class="col"><p>{{ props.user.name }} {{ props.user.surname }}</p></li>
        <li class="col"><p>{{ props.user.position }}</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
        <li><span>Телефон</span><p>+7-953-160-53-84</p></li>
    </ul>

    <div class="text-white w-100">
        <div class="row">
            <div class="col-6"><span>Имя</span>
                <p>{{ props.user.name }} {{ props.user.surname }}</p>
            </div>
            <div class="col-6"><span>Должность</span>
                <p>{{ props.user.position }}</p>
            </div>
        </div>
        <div class="row">
            <div class="col-6"><span>Телефон</span>
                <p>+7-953-160-53-84</p>
            </div>
            <div class="col-6"><span>Телефон</span>
                <p>+7-953-160-53-84</p>
            </div>
        </div>
        <div class="row">
            <div class="col-6"><span>Телефон</span>
                <p>+7-953-160-53-84</p>
            </div>
            <div class="col-6"><span>Телефон</span>
                <p>+7-953-160-53-84</p>
            </div>
        </div>
    </div>


</template>

<style scoped></style>
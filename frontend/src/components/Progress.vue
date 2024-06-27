<script setup>
const props = defineProps({
    title: String,
    progress: Number,
});
const color = (props.progress < 50) ? 'red' : (props.progress < 50) ? 'green' : (props.progress < 75) ? 'orange' : 'yellow';

const style = {
    "width": `${props.progress}%`,
    "background-color": color
}
const colorText = {
    color
}
</script>

<template>
        <div class="pro-bar">
            <small class="progress_bar_title" :style="colorText">
                {{ props.title }}
                <span class="progress_number">{{ props.progress }}%</span>
            </small>
            <span class="progress-bar-inner" :style="style" :data-value="props.progress"
                :data-percentage-value="props.progress"></span>
        </div>
</template>

<style >
.progress_bar .pro-bar {
    background: hsl(0, 0%, 97%);
    box-shadow: 0 1px 2px hsla(0, 0%, 0%, 0.1) inset;
    height: 4px;
    margin-bottom: 12px;
    margin-top: 50px;
    position: relative;
}

.progress_bar .progress_bar_title {
    font-size: 15px;
    font-weight: 300;
    position: relative;
    top: -28px;
    z-index: 1;
}

.progress_bar .progress_number {
    float: right;
  
}

.progress_bar .progress-bar-inner {

    display: block;
    width: 0;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    transition: width 1s linear 0s;
}

.progress_bar .progress-bar-inner:before {
    content: "";
    border-radius: 50%;
    width: 4px;
    height: 4px;
    position: absolute;
    right: 1px;
    top: 0;
    z-index: 1;
}

.progress_bar .progress-bar-inner:after {
    content: "";
    width: 14px;
    height: 14px;
    background-color: inherit;
    border-radius: 50%;
    position: absolute;
    right: -4px;
    top: -5px;
}
</style>

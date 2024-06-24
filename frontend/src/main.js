import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'

import Toast from "vue-toastification";

import './style.css'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "vue-toastification/dist/index.css";

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app 
    .use(createPinia())
    .use(Toast)
    .use( axios)
    .mount('#app')
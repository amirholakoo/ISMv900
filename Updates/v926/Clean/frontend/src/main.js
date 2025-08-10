import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';
import VueAxios from 'vue-axios';
import './assets/tailwind.css'
import { Html2CanvasPlugin } from 'vue3-html2canvas';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const app = createApp(App)

app.use(VueAxios, axios)
app.use(router)
app.use(Html2CanvasPlugin);
app.mount('#app')

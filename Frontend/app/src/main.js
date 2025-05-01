// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // <-- import du router

const app = createApp(App)
app.use(router) // <-- utilisation du router
app.mount('#app')



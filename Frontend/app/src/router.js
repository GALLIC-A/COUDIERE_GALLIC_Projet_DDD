import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from './vues/VueAuth.vue'
import Direction from './vues/VueDirection.vue'
import Marketing from './vues/VueMarketing.vue'
import Edition from './vues/VueEdition.vue'
import Client from './vues/VueClient.vue'
import { isAuthenticated } from './auth.js'

const routes = [
    {
        path: '/',
        redirect: '/login', // 👈 Redirection par défaut
      },
    {
      path: '/login',
      name: 'Login',
      component: LoginForm,
      meta: { public: true }
    },
    {
      path: '/direction',
      name: 'Direction',
      component: Direction,
      meta: { public: false }
    },
    {
        path: '/marketing',
        name: 'Marketing',
        component: Marketing,
        meta: { public: false }
    },
    {
        path: '/edition',
        name: 'Edition',
        component: Edition,
        meta: { public: false }
    },
    {
        path: '/client',
        name: 'Client',
        component:Client,
        meta:{ public: false}
    }
  ]
  
  const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  router.beforeEach((to, from, next) => {
    const isPublic = to.meta.public
    const loggedIn = isAuthenticated()
  
    if (!isPublic && !loggedIn) {
      return next('/login') // ↩️ redirige si non connecté
    }
  
    next()
  })
  
  export default router

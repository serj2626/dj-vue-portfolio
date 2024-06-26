import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/resume',
      name: 'resume',
      component: () => import('../views/ResumeView.vue')
    },
    {
      path: '/contacts',
      name: 'contacts',
      component: () => import('../views/ContactsView.vue')
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('../views/ProjectAll.vue')
    },
    {
      path: '/posts',
      name: 'posts',
      component: () => import('../views/PostListView.vue')
    },
    {
      path: '/posts/:id',
      name: 'post',
      component: () => import('../views/PostDetailView.vue')
    },

  ]
})

export default router

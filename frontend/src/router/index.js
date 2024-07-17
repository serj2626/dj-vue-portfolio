import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
      meta: {
        title: "Главная",
      },
    },
    {
      path: '/resume',
      name: 'resume',
      component: () => import('../views/ResumeView.vue'),
      meta: {
        title: "Резюме",
      },
    },
    {
      path: '/contacts',
      name: 'contacts',
      component: () => import('../views/ContactsView.vue'),
      meta: {
        title: "Контакты",
      },
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('../views/ProjectListView.vue'),
      meta: {
        title: "Проекты",
      },
    },
    {
      path: '/projects/:slug',
      name: 'project',
      component: () => import('../views/ProjectDetailView.vue.vue'),
      props: true,
      meta: {
        title: "Проект",
      },
    },
    {
      path: '/posts/',
      name: 'posts',
      component: () => import('../views/PostListView.vue'),
      meta: {
        title: "Мои статьи",
      },
    },
    {
      path: '/posts/:id',
      name: 'post',
      component: () => import('../views/PostDetailView.vue'),
      props: true,
      meta: {
        title: "Моя статья",
      },
    },
    ,
    {
      path: "/:pathMatch(.*)*",
      name: "notFound",
      component: () => import("@/views/PageNotFoundView.vue"),
      // redirect: { name: "home" },
      meta: {
        title: "Not Found",
      },
    }
  ]
})


router.beforeEach((to, from) => {
  document.title = to.meta.title || "Моё Портфолио";
  return true
});

export default router

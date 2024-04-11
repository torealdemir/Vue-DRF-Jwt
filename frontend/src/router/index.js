import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import MyAccount from '../views/MyAccount.vue'

import Projects from '../views/Projects.vue'
import About from '../views/About.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/Projects',
    name: 'Projects',
    component: Projects
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

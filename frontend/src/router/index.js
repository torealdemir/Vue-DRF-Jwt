import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import MyAccount from '../views/MyAccount.vue'
import Mapss from '../views/Mapss.vue'
import Photos from '../views/Photos.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
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
    path: '/maps',
    name: 'Mapss',
    component: Mapss
  },
  {
    path: '/pictures',
    name: 'Photos',
    component: Photos
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

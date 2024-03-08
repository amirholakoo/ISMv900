import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import addTruck from "@/components/addTruck.vue";
import addSupplier from "@/components/addSupplier.vue";
import addCustomer from "@/components/addCustomer.vue";
import addRawMaterial from "@/components/addRawMaterial.vue";
import addNewReel from "@/components/addNewReel.vue";
import forkliftPanel from "@/components/forkliftPanel.vue";
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/myapp/addTruck/',
    name: 'addTruck',
    component: addTruck
  },
  {
    path: '/myapp/addSupplier/',
    name: 'addSupplier',
    component: addSupplier
  },
  {
    path: '/myapp/addCustomer/',
    name: 'addCustomer',
    component: addCustomer
  },
  {
    path: '/myapp/addRawMaterial/',
    name: 'addRawMaterial',
    component: addRawMaterial
  },
  {
    path: '/myapp/addNewReel/',
    name: 'addNewReel',
    component: addNewReel
  },
  {
    path: '/myapp/forkliftPanel/',
    name: 'forkliftPanel',
    component: forkliftPanel
  },
]

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  history: createWebHistory(),
  routes,
})

export default router

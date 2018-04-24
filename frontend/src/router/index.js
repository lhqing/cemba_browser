import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '/random', component: 'Random' },
  { path: '/celltype/cluster', component: 'Cluster' },
  { path: '/overview/rs1', component: 'RS1' },
  { path: '*', component: 'NotFound' } // 404 page
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})

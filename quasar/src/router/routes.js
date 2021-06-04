import ComponentNCEnvirosdanDual from 'pages/nc-enviroscan-dual'

const routes = [
  {
    path: '/',
    component: () => import('pages/nc-enviroscan.vue')
  }
]

const ncedual = {
  path: '/dual',
  component: ComponentNCEnvirosdanDual
}

routes.push(ncedual)

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('components/Error404.vue')
  })
}

export default routes

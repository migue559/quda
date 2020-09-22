/* eslint-disable comma-dangle */
/* eslint-disable object-property-newline */

const routes = [
  { path: '/auth/login', name: 'login', component: () => import('pages/auth/Login.vue') },
  {
    path: '', component: () => import('layouts/Layout.vue'),
    children: [
      { path: '/', name: 'dashboard', component: () => import('pages/Dashboard.vue') }
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  { path: '*', edirect: '/404' },
  { path: '/404', name: '404', component: () => import('@/pages/errors/404.vue') }
]

export default routes

import { VERIFY_AUTH } from '@/store/auth.store'

export default ({ router, store }) => {
  router.beforeEach((to, from, next) => {
    // Ensure we checked auth before each page load.
    Promise.all([store.dispatch(VERIFY_AUTH)]).then(next)
    // Scroll page to top on every route change
    setTimeout(() => {
      window.scrollTo(0, 0)
    }, 100)
  })
}

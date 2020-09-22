import { apolloService } from '@/core/services/apollo.service'
import JwtService from '@/core/services/jwt.service'
import { GET_TOKEN, VERIFY_TOKEN } from '@/core/models/auth'

// action types
export const VERIFY_AUTH = 'verifyAuth'
export const LOGIN = 'login'
export const LOGOUT = 'logout'
export const REGISTER = 'register'
export const UPDATE_USER = 'updateUser'
// mutation types
export const PURGE_AUTH = 'logOut'
export const SET_AUTH = 'setUser'
export const SET_ERROR = 'setError'

const apollo = apolloService.defaultClient

const state = {
  errors: [],
  user: {},
  isAuthenticated: !!JwtService.getToken()
}

const getters = {
  currentUser (state) {
    return state.user
  },
  isAuthenticated (state) {
    return state.isAuthenticated
  },
  hasPermission: state => (permissions = undefined, hasperm = false) => {
    if (!permissions) { return true }
    if (!state.user.permissions) { return hasperm }
    for (const permission of permissions) {
      if (state.user.permissions.indexOf(permission) > -1) { hasperm = true; break }
    }
    return hasperm
  },
  hasModule (state) {
    return state.isAuthenticated
  }
}

const actions = {
  async [LOGIN] (context, credentials) {
    return await apollo
      .mutate({
        mutation: GET_TOKEN(credentials)
      }).then(({ data }) => {
        context.commit(SET_AUTH, data.tokenAuth)
        return data
      }).catch((error) => {
        context.commit(SET_ERROR, error)
        return 0
      })
  },
  async [VERIFY_AUTH] (context) {
    const token = JwtService.getToken()
    const username = JwtService.getUsername()
    if (token && username) {
      await apollo
        .query({
          query: VERIFY_TOKEN(token, username)
        })
        .then(({ data }) => {
          context.commit(SET_AUTH, data)
        })
        .catch((error) => {
          context.commit(SET_ERROR, error)
          // context.commit(PURGE_AUTH)
        })
    } else {
      context.commit(PURGE_AUTH)
    }
  },
  [LOGOUT] (context) {
    context.commit(PURGE_AUTH)
  }
}

const mutations = {
  [SET_ERROR] (state, error) {
    state.errors = [error]
  },
  [SET_AUTH] (state, token) {
    state.isAuthenticated = true
    state.user = {
      organization: token.mriuser.organization,
      permissions: token.mriuser.getAllPermissions.substring(1, token.mriuser.getAllPermissions.length - 1).replace(/ /g, '').replace(/'/g, '').split(','),
      username: token.mriuser.username,
      visibleUsername: token.mriuser.visibleUsername,
      id: token.mriuser.id
    }
    if ('token' in token) JwtService.saveToken(token)
  },
  [PURGE_AUTH] (state) {
    state.isAuthenticated = false
    state.user = {}
    state.errors = {}
    JwtService.destroyToken()
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}

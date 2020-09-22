const ID_TOKEN_KEY = 'id_token'
const ID_USERNAME = 'id_username'

export const getToken = () => {
  return window.localStorage.getItem(ID_TOKEN_KEY)
}

export const getUsername = () => {
  return window.localStorage.getItem(ID_USERNAME)
}

export const saveToken = token => {
  window.localStorage.setItem(ID_TOKEN_KEY, token.token)
  window.localStorage.setItem(ID_USERNAME, token.coreuser.id)
}

export const destroyToken = () => {
  window.localStorage.removeItem(ID_TOKEN_KEY)
  window.localStorage.removeItem(ID_USERNAME)
}

export default { getToken, getUsername, saveToken, destroyToken }

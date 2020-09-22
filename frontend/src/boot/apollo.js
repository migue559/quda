import VueApollo from 'vue-apollo'
import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import JwtService from '@/core/services/jwt.service'

const GRAPHQL_URL = 'http://localhost:8000/graphql/'

const getHeaders = () => {
  const headers = {
    authorization: ''
  }
  headers.authorization = `JWT ${JwtService.getToken()}`
  return headers
}

const httpLink = createHttpLink({
  uri: GRAPHQL_URL,
  fetch,
  headers: getHeaders()
})

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
  link: httpLink,
  cache
})

export const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

export default ({ app, Vue }) => {
  Vue.use(VueApollo)
  app.apolloProvider = apolloProvider
}

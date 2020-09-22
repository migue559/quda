import Vue from 'vue'
import Vuetify from 'vuetify'

Vue.use(Vuetify)

const vuetifyProvider = new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: '#5867dd',
        secondary: '#e8ecfa',
        accent: '#5d78ff',
        error: '#fd397a',
        info: '#5578eb',
        success: '#0abb87',
        warning: '#ffb822'
      }
    }
  }
})

export default ({ app, Vue }) => {
  Vue.use(Vuetify)
  app.vuetify = vuetifyProvider
}

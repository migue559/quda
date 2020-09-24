<template lang='pug'>
  q-page.flex.flex-center
    h1 Hola, {{hello}}
</template>

<script>
import gql from 'graphql-tag'
export default {
  name: 'PageIndex',
  data () {
    return {
      hello: ''
    }
  },
  apollo: {
    // Subscriptions
    $subscribe: {
      // When a tag is added
      hello: {
        query: gql`subscription {
          hello
        }`,
        // Result hook
        // Don't forget to destructure `data`
        result ({ data }) {
          this.hello = data.hello
        }
      }
    }
  }
}
</script>

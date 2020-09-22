<template lang="pug">
q-layout
  q-page-container
    q-page.flex.bg-image.flex-center
      q-card(v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}")
        q-card-section
          q-avatar.absolute-center.shadow-10(size='103px')
            img(src='~assets/img/auth/user.png')
        q-card-section
          .text-center.q-pt-lg
            .col.text-h6.ellipsis
              | HERRAMIENTA DE CALIDAD DE DATOS
        q-card-section
          q-form.q-gutter-md
            q-input(
              filled=''
              v-model='username'
              label='Tu usuario'
              lazy-rules=''
            )
            q-input(
              filled=''
              v-model='password'
              :type="isPwd ? 'password' : 'text'"
              label='Tu contraseña'
              lazy-rules=''
            )
              template(v-slot:append='')
                q-icon.cursor-pointer(:name="isPwd ? 'visibility_off' : 'visibility'", @click='isPwd = !isPwd')
            div
            .col-6
              q-item
                q-checkbox.full-width(dense='', outlined='', v-model='remember', label='Recuerdame')
            q-btn(label='INGRESAR', to='/', type='button', color='primary')
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      remember: true,
      isPwd: 'password'
    }
  }
}
</script>

<style>
  .bg-image {
    background-image: url(~assets/img/auth/bg.png);
    background-position: right;
    background-size: cover;
  }
</style>

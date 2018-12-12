<template>
  <div class="has-text-centered">
    <h1 class="title has-text-white">
      {{title}}
    </h1>
    <form>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" type="email" placeholder="Email" v-model="email">
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input class="input" type="password" placeholder="Password" v-model="password">
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>
      <button class="button is-pulled-right is-info is-uppercase" @click="handleLogin()">
        {{button}}
      </button>
    </form>
  </div>
</template>

<script>
import toasts from '../mixins/user-toasts';
import { loginUser } from '../utils/users-api';

export default {
  name: 'login-user',
  data() {
    return {
      title: 'Login User',
      button: 'login',
      email: '',
      password: '',
    };
  },
  mixins: [toasts],
  methods: {
    handleLogin() {
      const data = {
        email: this.email,
        password: this.password,
      };
      loginUser(data)
        .then((response) => {
          if (response.status === 'success') {
            this.successToast('Logged in successfully');
          }
        })
        .catch((err) => {
          if (err.response.data.status === 'fail') {
            const msg = JSON.stringify(err.response.data.errors);
            this.errorToast(msg);
          } else {
            console.error(err);
            this.errorToast('Back-end server error!');
          }
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

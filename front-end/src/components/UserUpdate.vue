<template>
  <div class="has-text-centered">
    <h1 class="title has-text-white">
      {{title}}
    </h1>
    <form>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" type="number" placeholder="ID" v-model="id">
          <span class="icon is-small is-left">
            <i class="fas fa-id-badge"></i>
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
      <div class="field">
        <p class="control has-icons-left">
          <input class="input" type="password" placeholder="New password" v-model="newPassword">
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>
      <div class="level">
        <div class="level-left">
        </div>
        <div class="level-right">
          <button class="button level-item is-warning is-uppercase" @click="handleUpdate()">
            {{button}}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import toasts from '../mixins/user-toasts';
import { updateUser } from '../utils/users-api';

export default {
  name: 'update-user',
  data() {
    return {
      title: 'Update your credentials',
      button: 'update',
      id: '',
      password: '',
      newPassword: '',
    };
  },
  mixins: [toasts],
  methods: {
    handleUpdate() {
      const data = {
        id: this.id,
        password: this.password,
        newPassword: this.newPassword,
      };
      updateUser(data)
        .then((response) => {
          if (response.status === 'success') {
            this.successToast('User password updated successfully');
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

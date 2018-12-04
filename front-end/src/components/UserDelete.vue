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
      <div class="level">
        <div class="level-left">
        </div>
        <div class="level-right">
          <button class="button level-item is-danger is-uppercase" @click="handleDelete()">
            {{button}}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { toasts } from '../mixins/user-toasts';
import { deleteUser } from '../utils/users-api';

export default {
  name: 'delete-user',
  data() {
    return {
      title: 'Delete your account',
      button: 'delete',
      id: '',
    };
  },
  mixins: [toasts],
  methods: {
    handleDelete() {
      const data = {
        id: this.id,
      };
      deleteUser(data)
        .then((response) => {
          if (response.status === 'success') {
            this.successToast(`User [${this.id}]: ${response.data.email} deleted successfully`);
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

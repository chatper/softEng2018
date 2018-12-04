<template>
  <div class="has-text-centered">
    <h1 class="title has-text-white">
      {{title}}
    </h1>
    <table class="container table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Email</th>
          <th>Password</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{user.id}}</td>
          <td>{{user.email}}</td>
          <td>{{user.password}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { getUsers } from '../utils/users-api';

export default {
  name: 'list-user',
  data() {
    return {
      title: 'List available users',
      users: [],
    };
  },
  methods: {
    fetchUsers() {
      getUsers().then((users) => {
        this.users = users.data;
      });
    },
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

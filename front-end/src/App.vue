<template>
  <section class="hero is-danger is-fullheight">
  <!-- Hero head: will stick at the top -->
  <div class="hero-head">
    <nav class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item">
            <p class="title">Solidity</p>
          </a>
        </div>
        <div class="navbar-menu">
          <div class="navbar-end">
            <span class="navbar-item">
              <a class="button is-primary is-inverted">
                <span class="icon">
                  <i class="fab fa-github"></i>
                </span>
                <a href="https://github.com/PavlosTsourapas/Dummy-Repo" target="_blank">Documentation</a>
              </a>
            </span>
          </div>
        </div>
      </div>
    </nav>
  </div>

  <!-- Hero content: will be in the middle -->
  <div class="hero-body" :style="{'background-image': `url(${require('./assets/hands.jpg')})`}">
  <!-- <div class="hero-body"> -->
    <div id="app" class="container">
      <router-view></router-view>
    </div>
  </div>

  <!-- Hero footer: will stick at the bottom -->
  <div class="hero-foot">
    <nav class="tabs is-boxed is-fullwidth">

      <div class="container">
        <ul>
          <li :class="{ 'is-active': $route.path == '/list' }">
            <router-link to="/list">List</router-link>
          </li>
          <li :class="{ 'is-active': $route.path == '/register' }">
            <router-link to="/register">Register</router-link>
          </li>
          <li :class="{ 'is-active': $route.path == '/login' }">
            <router-link to="/login">Login</router-link>
          </li>
          <li :class="{ 'is-active': $route.path == '/update' }">
            <router-link to="/update">Update</router-link>
          </li>
          <li :class="{ 'is-active': $route.path == '/delete' }">
            <router-link to="/delete">Delete</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</section>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
    }
  }
}
</script>

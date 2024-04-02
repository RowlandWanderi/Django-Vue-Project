<!-- //The styling here uses bulma but you can use bootstrap  or any other framework/library of your choice -->


<template>
  <div id='wrapper'>
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/"><strong>Myproject</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <!-- //the v-bind is used here to connect the burger button to the navbar menu -->
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="option1" class="navbar-item">option1</router-link>
          <router-link to="option2" class="navbar-item">option2</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="login" class="button is-light">Log in</router-link>
              <router-link to="cart" class="button is-success">
                <span class="icon"><i class="fa fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>

        </div>
      </div>

    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">copyright (c) 2024</p>
    </footer>
  </div>
</template>


<!-- //create a new script for the responsivenes of the burger button on smaller screens -->

<script>
export default{
  data(){
    return{
      showMobileMenu : false
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma'
</style>

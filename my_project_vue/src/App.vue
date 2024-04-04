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
                <span>Cart ({{ cartTotalLength }})</span>
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
      showMobileMenu : false,
      cart: {
        items: []
      }
    }
  },
  //before anything else we need to initialize the store
  //commit is used to call the mutations
  beforeCreate(){
    this.$store.commit('initializeStore')
  },
  //set the cart to be the cart  from the vuex store
  mounted(){
    this.cart = this.$store.state.cart
  },
  // computed are calculated variables based on things around on the whole page
  computed: {
    cartTotalLength(){
      let totalLength = 0
      //loop through all the items in the cart
      for(let i = 0; i < this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength

    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma'
</style>

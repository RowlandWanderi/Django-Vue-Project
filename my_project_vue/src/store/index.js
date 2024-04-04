import { createStore } from 'vuex'

export default createStore({
  state: {
    //normally used to  store data that needs to be accessed using authentication
    cart :{
      items : [],
      isLoading : false,
      isAuthenticated : false,
      token : '',
    }
  },
  getters: {
  },
  mutations: {
    //function to initialize the store
    initializeStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      //if the user is logged in  set auth status and token
      if (localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }else{
        state.token = ''
        state.isAuthenticated = false
      }
    },

    //function to add items to the cart
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if(exists.length){
        //if the item is already in the cart, add the quantity
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }else{
        //else add the item to the cart
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    //function to set the loading
    setIsLoading(state,status){
      state.isLoading = status;
    },

    //function to set the token upon login
    setToken(state,token){
      state.token = token
      state.isAuthenticated = true
    },

    //function to remove the token upon logout
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },

    //function to clear the cart
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
  },
  actions: {
  },
  modules: {
  }
})

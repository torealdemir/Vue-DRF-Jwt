<template>
  <nav>
    <router-link to="/">Home</router-link>
    <span> || </span>
    <router-link to="/login">Login</router-link>
    <span> || </span>
    <router-link to="/signup">SignUp!</router-link>
  </nav>
  <router-view/>

  
</template>

<script>
import axios from 'axios'

export default {
  name:'App',

  beforeCreate(){
    this.$store.commit('initializeStore')
    
    const access = this.$store.state.access
    const user = this.$store.state.isAuthenticated

    if((access) && (user)){
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

  // mounted(){
  //   const user = this.$store.state.isAuthenticated
  //   if(user) {

  //   }
  // }

  methods: {
    logoutForm(e){
      this.$store.commit('removeAccess');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      axios.defaults.headers.common['Authorization']=''
      const user = this.$store.state.isAuthenticated

      if(!user){
        this.$router.push('/login')
      }
    },

    getAccess(e){
      const accessData = {
        refresh: this.$store.state.refresh
      }

      axios
      .post('api/v1/token/refresh/', accessData)
      .then(response => {
        const access = response.data.access
        localStorage.setItem('access', access)
        this.$store.commit('setAccess', access)
      })
      .catch(error => {
        console.log(error)
      })
    }
  }

}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

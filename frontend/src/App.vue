<template>
  <div class="MainApp"> 
    <Navbar />
  </div>
  <router-view />
  
</template>

<script>
import axios from 'axios';
import Navbar from '@/components/Nav.vue';




export default {
  name: 'App',
  components: {
    Navbar,
  },

  beforeCreate() {
    this.$store.commit('initializeStore')
    
    const access = this.$store.state.access
    const user = this.$store.state.isAuthenticated

    if ((access) && (user)) {
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

  mounted(){
    const user = this.$store.state.isAuthenticated
    if(user){
      setInterval(()=>{
        this.getAccess()
      }, 29900)
    } else {
      this.$router.push('/')
    }
  },

  methods: {
    logoutForm(e){
      this.$store.commit('removeAccess');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      axios.defaults.headers.common['Authorization']= ''
      const user = this.$store.state.isAuthenticated
      if(!user){
        this.$router.push('/')
      }
    },
    getAccess(e){
      const accessData = {
        refresh: this.$store.state.refresh
      }

      axios
          .post('/auth/jwt/refresh/', accessData)
          .then(response => {
            const access = response.data.access
            localStorage.setItem('access', access)
            this.$store.commit('setAccess', access)
          }).catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style lang="scss" scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3d78b4;
  margin-bottom: 20vh;
}


</style>
<template>
  <nav class="navbar navbar-expand-md bg-dark">
    <router-link to="/" class="navbar-brand fs-3 ms-3 text-secondary">Home</router-link>
    <span> || </span>
    <router-link to="/maps" class="nav-link mx-3 fs-4 text-secondary">About</router-link>
    <span> || </span>
    <router-link to="/pictures" class="nav-link mx-3 fs-4 text-secondary">Projects</router-link>

    <button class="navbar-toggler d-flex ms-auto text-warning m-3 d-md-none" type="button" data-bs-toggle="collapse" data-bs-target="#btn">
      <i class="bi bi-body-text">=</i>
    </button>

    <div class="control">

      
    </div>
    <div class="collapse navbar-collapse" id="btn">
      <template v-if="this.$store.state.isAuthenticated">
        <div class="navbar-nav ms-auto d-flex align-items-center">
          <router-link to="myAccount" class="nav-item btn btn-primary my-2 me-2">My Account</router-link>
          <!-- <button @click="logoutHandler" class="btn btn-danger d-flex align-items-center justify-content-center">Logout</button> -->
          <router-link @click="logoutHandler" class="btn btn-danger mx-2" to="/">Logout</router-link>
        </div>
      </template>
      <template v-else>
        <div class="navbar-nav ms-auto d-flex">
          <router-link to="/login" class="btn btn-warning mx-2 my-2">Login!</router-link>
          <router-link to="/signup" class="btn btn-primary my-2 mx-2">SignUp!</router-link>
        </div>
      </template>
    </div>
  </nav>
</template>



<script>


export default {
    name:'Navbar',

    

    methods: {
      logoutHandler(){
        console.log('logout')

        this.$store.commit('removeAccess')
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        localStorage.clear()
        this.$store.state.isAuthenticated= false
        this.$router.push('/login')
        
      }
    }
    
}
</script>
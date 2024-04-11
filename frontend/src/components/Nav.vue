<template>
  <nav class="navbar navbar-expand-md" :class="{'navbar-dark' :isDarkMode, 'bg-dark' : isDarkMode, 'navbar-light': !isDarkMode}">
    <router-link to="/" class="navbar-brand fs-3 ms-3 text-secondary">Home</router-link>
    <span> || </span>
    <router-link to="/about" class="nav-link mx-3 fs-4 text-secondary">About</router-link>
    <span> || </span>
    <router-link to="/projects" class="nav-link mx-3 fs-4 text-secondary">Projects</router-link>

    <button class="navbar-toggler d-flex ms-auto text-warning m-3 d-md-none" type="button" data-bs-toggle="collapse" data-bs-target="#btn">
      <i class="bi bi-body-text">=</i>
    </button>

    <div class="control">

      
    </div>
    <div class="collapse navbar-collapse" id="btn">

      <template v-if="this.$store.state.isAuthenticated">
        <div class="navbar-nav ms-auto d-flex align-items-center">
          <router-link to="myAccount" class="nav-item btn btn-primary my-2 me-2">My Account</router-link>
          <router-link @click="logoutHandler" class="btn btn-danger mx-2" to="/">Logout</router-link>
        </div>
      </template>
      <template v-else>
        <div class="navbar-nav ms-auto d-flex">
          <router-link to="/login" class="btn btn-warning mx-2 my-2">Login!</router-link>
          <router-link to="/signup" class="btn btn-primary my-2 mx-2">SignUp!</router-link>
        </div>
      </template>
      <div class="switch">
        <input
          type="checkbox"
          id="themeSwitch"
          class="switch-checkbox"
          v-model="isDarkMode"
        />
      <label for="themeSwitch" class="switch-label"></label>
     </div>
    </div>
  </nav>
</template>



<script>


export default {
    name:'Navbar',
    
    computed : {
      isDarkMode: {
        get() {
          return this.$store.state.isDarkMode
        },
        set(value){
          this.$store.commit('setDarkMode', value);
        }
      }
    },

    methods: {
      logoutHandler(){
        console.log('logout')

        this.$store.commit('removeAccess')
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        localStorage.clear()
        this.$store.state.isAuthenticated= false
        this.$router.push('/login')
        
      },

      toggleTheme(){
        this.isDarkMode = event.target.checked
      }
    }
    
}
</script>


<style scoped>
.switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}

.switch-checkbox {
  display: none;
}

.switch-label {
  position: absolute;
  top: 0;
  left: 0;
  width: 50px;
  height: 24px;
  background-color: #ccc;
  border-radius: 24px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.switch-label::after {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background-color: #fff;
  border-radius: 50%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s;
}

.switch-checkbox:checked + .switch-label {
  background-color: #53637c;
}

.switch-checkbox:checked + .switch-label::after {
  transform: translateX(26px);
}
</style>

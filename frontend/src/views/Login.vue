<template>
   
    
    <div class="container-sm" >
        <h1 class="d-flex justify-content-center my-4 text-success">Login!</h1>
        <div class="control">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email address</label>
                    <input type="email" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
<Footer class="fixed-bottom">
</Footer>
</template>

<script>
import axios from 'axios';
import Footer from '@/components/Footer.vue'

export default {
    name:'Login',
    components: {
        Footer,
    },

    data(){
        return {
            username:'',
            password:''
        }
    },

    methods: {
        submitForm(e){
            const formData = {
                username: this.username,
                password: this.password
            }
        
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('access')

            axios
                .post('auth/jwt/create/', formData)
                .then(response => {
                    const access = response.data.access
                    const refresh = response.data.refresh

                    this.$store.commit('setAccess', access)
                    this.$store.commit('setRefresh', refresh)

                    axios.defaults.headers.common['Authorization']= 'JWT ' + access
                    localStorage.setItem('access', access)
                    localStorage.setItem('refresh', refresh)

                    const user = this.$store.state.isAuthenticated
                    this.$store.isAuthenticated = true
                    if(user){
                        this.$router.push('/')
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }

}


</script>
<template>
    <h1>SignUp!</h1>

    <div class="container-sm" >
        <div class="control">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email address</label>
                    <input type="email" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <!-- <div class="mb-3">
                    <label for="username" class="form-label">username</label>
                    <input type="text" v-model="username" class="form-control" id="username" aria-describedby="emailHelp">
                </div> -->
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword2" class="form-label">RePassword</label>
                    <input type="password" v-model="repassword" class="form-control" id="exampleInputPassword2">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>

</template>
<script>
import axios from 'axios'

export default{
    name:'SignUp',

    data(){
        return {
            username: '',
            // username:'',
            password: '',
            repassword:'',
            errors:[]
        }
    },

    methods: {
        submitForm(){
            console.log('Submit!')
            this.errors=[]
            if(this.username === ''){
                this.errors.push('username is missing')
                console.log('empty mail')
            }
            if(this.password === ''){
                this.errors.push('password is missing')
                console.log('missing pass')
            }
            if(this.password !== this.repassword){
                this.errors.push('pass must be same')
                console.log('pass must be same')
            }
            if(!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password,
                    // username:this.username,
                }

                axios
                    .post('auth/users/', formData)
                    .then(response => {
                        this.$router.push('/login')
                        console.log(token)
                    })
                    .catch(error => {
                        console.log(error)
                        console.log(formData)
                    })
            }
        }

        
    }
}
</script>

<style>
button {
    margin-bottom: 20px;
}
</style>

<!-- //'api/v1/auth/' -->
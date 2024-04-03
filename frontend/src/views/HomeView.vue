<template>
  <div>
    <h1 class="bg-light d-flex justify-content-center">Home!</h1>
    <div v-for="content in contents" :key="content.id">
      <h1>{{ content.title }}</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeView',
  data() {
    return {
      contents: []
    };
  },
  // created() {
  //   this.loadContent();
  // },
  methods: {
    loadContent() {
      const accessToken = localStorage.getItem('access');
      const refreshToken = localStorage.getItem('refresh');

      axios
        .get('/ToCo', {
          headers: {
            Authorization: `JWT ${accessToken}`
          }
        }) 
        .then(response => {
          console.log(response.data);
          this.contents = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
  }
}
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
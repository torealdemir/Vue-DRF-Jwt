<template>
  <div>
    <div class="position-relative">
      <img src="https://images.unsplash.com/photo-1569852741721-ee5a94bf719e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="img-fluid shadow-lg rounded" alt="Fluid Image">
      <div class="position-absolute top-50 start-50 translate-middle">
        <div class="bg-translucent p-3 shadow-sm rounded">
          <h1 class="mb-3 text-white fs-4 fs-sm-5 fs-md-6">Odtu Metalurji Malzeme</h1>
          <h5 class="mb-4 text-white fs-6 fs-sm-7 fs-md-8">Nano Materials Field</h5>
        </div>
      </div>
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
  .position-relative {
    position: relative;
  }

  .position-absolute {
    position: absolute;
  }

  .top-50 {
    top: 50%;
  }

  .start-50 {
    left: 50%;
  }

  .translate-middle {
    transform: translate(-50%, -50%);
  }

  .bg-translucent {
    background-color: rgba(0, 0, 0, 0.5);
  }

  #intro {
      height: 100vh;
    }

  @media (min-width: 992px) {
    /* Desktop mode font sizes */
    .fs-xxl-9 {
      font-size: 2.5rem;
    }

    .fs-xxl-11 {
      font-size: 4.5arem;
    }
  }
</style>
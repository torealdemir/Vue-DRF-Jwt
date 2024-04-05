<template>


  <!-- Background image -->
  <div id="intro" class="bg-image shadow-2-strong">
    <div class="position-relative">
      <img src="https://images.unsplash.com/photo-1569852741721-ee5a94bf719e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="mainImage img-fluid shadow-lg rounded shadow-img" alt="Fluid Image">
      <div class="position-absolute top-50 start-50 translate-middle">
        <div class="">
          <h1 class="headers mb-3">Odtu Metalurji ve Malzeme Bolumu</h1>
          <h5 class="headers mb-4">Nano Materials Field</h5>
        </div>
      </div>
      <hr class="my-5" />
    </div>

  </div>
    
  



<!--Main layout-->
<main class="mt-5">
  <div class="container">
    <!--Section: Content-->
    <section>
      <div class="row">
        <div class="col-md-6 gx-5 mb-4">
          <div class="bg-image hover-overlay shadow-2-strong" data-mdb-ripple-init data-mdb-ripple-color="light">
            <img src="https://plus.unsplash.com/premium_photo-1664036937272-6ae6080d2d51?q=80&w=1950&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="img-fluid " />
            <a href="#!">
              <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
            </a>
          </div>
        </div>

        <div class="col-md-6 gx-5 mb-4 d-flex align-items-center">
          <div class="">
            <h4><strong>Facilis consequatur eligendi</strong></h4>
            <p class="text-muted">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis consequatur
              eligendi quisquam doloremque vero ex debitis veritatis placeat unde animi laborum
              sapiente illo possimus, commodi dignissimos obcaecati illum maiores corporis.
            </p>
          </div>
          <div class="mx-3">
            <h4><strong>Doloremque vero ex debitis veritatis?</strong></h4>
            <p class="text-muted">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod itaque voluptate
              nesciunt laborum incidunt. Officia, quam consectetur. Earum eligendi aliquam illum
              alias, unde optio accusantium soluta, iusto molestiae adipisci et?
            </p>
          </div>
          
          
        </div>
      </div>
    </section>
    <!--Section: Content-->

    <hr class="my-5" />

    <!--Section: Content-->
    <section class="text-center">
      <h4 class="mb-5"><strong>Facilis consequatur eligendi</strong></h4>

      <div class="row">
        <div class="col-lg-4 col-md-12 mb-4">
          <div class="card">
            <div class="bg-image hover-overlay" data-mdb-ripple-init data-mdb-ripple-color="light">
              <img src="https://plus.unsplash.com/premium_photo-1661382310239-8958f2c87f3f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="img-fluid" />
              <a href="#!">
                <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
              </a>
            </div>
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">
                Some quick example text to build on the card title and make up the bulk of the
                card's content.
              </p>
              <a href="#!" class="btn btn-primary" data-mdb-ripple-init>Button</a>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card">
            <div class="bg-image hover-overlay" data-mdb-ripple-init data-mdb-ripple-color="light">
              <img src="https://plus.unsplash.com/premium_photo-1681426645543-ba5027b4c6ba?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="img-fluid" />
              <a href="#!">
                <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
              </a>
            </div>
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">
                Some quick example text to build on the card title and make up the bulk of the
                card's content.
              </p>
              <a href="#!" class="btn btn-primary" data-mdb-ripple-init>Button</a>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card">
            <div class="bg-image hover-overlay" data-mdb-ripple-init data-mdb-ripple-color="light">
              <img src="https://plus.unsplash.com/premium_photo-1681426678542-613c306013e1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="img-fluid" />
              <a href="#!">
                <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
              </a>
            </div>
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">
                Some quick example text to build on the card title and make up the bulk of the
                card's content.
              </p>
              <a href="#!" class="btn btn-primary" data-mdb-ripple-init>Button</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!--Section: Content-->

    <hr class="my-5" />

   
  </div>
</main>
<!--Main layout-->

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
body {
  font-family: "KoHo", sans-serif;
}

.headers {
  font-size: 5.5rem;
  color: rgb(157, 168, 168);
}


.mainImage{
  filter: blur(4px);
  -webkit-filter: blur(4px);
}

</style>
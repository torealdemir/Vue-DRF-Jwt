<template>
<div id="about">
    <div id="intro" class="bg-image shadow-2-strong">
        <div class="position-relative">
            <img src="https://i.pinimg.com/originals/9b/cf/06/9bcf06fcd555d2089a61139cafbcf05e.jpg" id="background-img" class="img-fluid rounded" alt="">
        </div>
    </div>
</div>
<Footer />

</template>

<script>
import Footer from '@/components/Footer.vue'

export default{

    name:'About',
    components:{
      Footer
    }

    
}
</script>
<style scoped>
#background-img{
    width: 100%;
}

li {
  list-style: none;
}

</style>
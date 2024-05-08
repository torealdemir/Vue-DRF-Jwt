<template>
    <footer>
        <div class="position-relative fixed-bottom py-4 text-center text-secondary bg-dark">
            <span>All Rights Reserved @Metu Engineering Section</span>
            <div class="row py-6 mt-3">
                <ul>
                    <li>
                    <p>Adress:Odtu Engineering Section Material Engineering</p>
                    </li>
                    <li>
                    <a href='mailto:metuedu@xyz.com?subject=me&body=Hello!'>Contact us!</a>
                    </li>
                </ul>            
            </div>
        </div>
    </footer>
</template>
<script>
export default {
    name: 'Footer',

    methods: {
        mailTo(){
        window.location("mailto:xys@metuedu.com")
        console.log('mail!')
      }
    }
}

</script>
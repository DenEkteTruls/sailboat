<script>

</script>



<div class="container">
    <img id="image" src="http://192.168.10.194:4444/video_feed" alt="" width="1024" heigh="600" autoplay>
    <img on:click={() => {window.location.assign("/");}} id="home_button" src="icons/home.png" alt=""/>
</div>



<style>
    .container {
        width: 100vw;
        height: 100vh;
        background-color: white;
        margin: -8px;
        overflow-y: hidden;
    }

    #image {
        position: absolute;
    }

    #home_button {
        position: absolute;
        width: 50px;
        height: 50px;
        top: 20px;
        right: 2.7vw;
        box-shadow: 0 0 10px #949494;
        border-radius: 20px;
    }
</style>
<script>
    import Sidebar_App from "./Sidebar_App.svelte";
    export let apps;

    let time = new Date();
    $: hours = (time.getHours()<10?'0':'') + time.getHours();
    $: minutes = (time.getMinutes()<10?'0':'') + time.getMinutes();

    setInterval(() => {
        time = new Date();
    }, 1000);
</script>


<div class="container">
    <div class="top">
        <h3>{hours}:{minutes}</h3>
        <div class="status">
            <img class="top-icons" src="icons/dekning.png" alt=""/>
            <img class="top-icons" src="icons/wifi.png" alt=""/>
        </div>
    </div>
    <div class="apps">
        {#each {length: 3} as _, i}
            <Sidebar_App app={apps[i]}/>
        {/each}
    </div>
    <div class="bottom">

    </div>
</div>


<style>
    .container {
        background-color: rgb(249, 173, 159);
        width: 90px;
        height: 600px;
    }
    
    .apps {
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        position: absolute;
        width: 90px;
        height: 300px;
        top: 120px;
    }

    .top {
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        width: 90px;
        height: 80px;
    }

    .status {
        display: flex;
        width: 90px;
        height: 20px;
        justify-content: center;
        align-items: center;
        margin-left: 15px;
        margin-top: 10px;
    }

    .top-icons {
        width: 40px;
    }

    h3 {
        font-size: 22px;
        font-weight: bolder;
        margin: 0;
    }

</style>
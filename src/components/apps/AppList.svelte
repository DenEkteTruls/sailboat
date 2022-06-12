<script>
    import App from "./App.svelte";
    export let apps;
</script>


<div class="container">
    {#each {length: 8} as _, i}
        <App app={apps[i]}/>
    {/each}
</div>


<style>
    .container {
        position: absolute;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        top: 30px;
        left: 130px;
        width: 850px;
        height: 450px;
        align-items: center;
        justify-content: space-between;
    }
</style>
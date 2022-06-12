<script>
    export let app;

    function clicked()
    {
        window.location.assign(app.title);
    }
</script>

<img on:click={clicked} src="{app.icon}" alt=""/>


<style>
    img {
        width: 170px;
        height: 170px;
        margin: 12px;
        border-radius: 30px;
    }

    img:hover {
        user-select: none;
        cursor: pointer;
        transform: scale(1.03);
        transition: all 0.1s;
    }
</style>
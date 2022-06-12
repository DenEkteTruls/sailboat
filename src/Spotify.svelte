<script>
    let playlists = [
        {"album": "B.B. King Live", "artist": "B.B. King"},
        {"album": "The Essential Count Basie", "artist": "Count Basie"},
        {"album": "Vær Meg Nær", "artist": "Evangeliesenteret"},
        {"album": "Sinatra Basie", "artist": "Frank Sinatra & Count Basie"},
        {"album": "Continuum", "artist": "John Mayer"},
        {"album": "Room For Squares", "artist": "John Mayer"},
        {"album": "Ole Ivars 20 Beste", "artist": "Ole Ivars"},
        {"album": "Ole Ivars 50 år", "artist": "Ole Ivars"}
    ];

    let current_album_index = 0;
    let playing = false;

    function getCover(index)
    {
        let playlist = playlists[index];
        let first = playlist.album.toLowerCase().replaceAll(" ", "-");
        let second = playlist.artist.toLowerCase().replaceAll(" ", "-");
        return "spotify/playlists/"+second+":"+first+"/cover.jpg";
    }

    function play()
    {
        playing = !playing;
    }

</script>



<div class="container">
    <div class="playlists">
        <h1 id="playlist-title">Playlists</h1>
        {#each playlists as pl, i}
            <div class="playlist">
                <img src="{getCover(i)}" alt=""/>
                <h1>{pl.album}</h1>
                <p>{pl.artist}</p>
            </div>
        {/each}
    </div>
    <div class="player">
        <div class="left">
            <img src="{getCover(current_album_index)}" alt=""/>
            <div class="album_and_artist">
                <h1>{playlists[current_album_index].album}</h1>
                <p>by {playlists[current_album_index].artist}</p>
            </div>
        </div>
        <div class="right">
            <div class="buttons">
                <img class="button" src="spotify/player/last.png" alt=""/>
                {#if playing}
                    <img class="button" on:click={play} src="spotify/player/pause.png" alt=""/>
                {:else}
                    <img class="button" on:click={play} src="spotify/player/play.png" alt=""/>
                {/if}
                <img class="button" src="spotify/player/next.png" alt=""/>
            </div>
            <div class="playbar"/>
        </div>
    </div>
    <img on:click={() => {window.location.assign("/")}} id="home_button" src="icons/home.png" alt=""/>
</div>



<style>
    .container {
        width: 100vw;
        height: 100vh;
        background-color: white;
        margin: -8px;
        overflow-y: hidden;
    }

    .playlists {
        max-width: 92.5vw;
        height: 280px;
        background-color: #EDEDED;
        margin-left: 2.5vw;
        margin-top: 100px;
        border-radius: 15px;
        display: flex;
        padding: 10px;
        overflow-x: scroll;
        -webkit-overflow-scrolling: touch;
    }

    .playlist {
        display: flex;
        flex-direction: column;
        background-color: white;
        min-width: 170px;
        margin: 10px 5px;
        border-radius: 10px;
        align-items: center;
        padding: 20px 10px;
    }

    .playlist > img {
        border-radius: 10px;
        width: 140px;
        
    }

    .playlist > h1 {
        font-size: 15px;
        max-width: 135px;
        text-overflow: ellipsis;
        overflow: hidden;
        font-weight: 600;
        white-space: nowrap;
        margin-top: 15px;
        margin-bottom: 2px;
    }

    .playlist > p {
        font-size: 12px;
        margin: 0;
        padding: 0;
        font-weight: 500;
        color: #949494;
        max-width: 75%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    #playlist-title {
        position: absolute;
        color: #757575;
        top: 20px;
        font-weight: 500;
        left: 32px;
    }

    .player {
        position: absolute;
        display: flex;
        width: 100vw;
        height: 80px;
        bottom: 0;
        box-shadow: 0px -5px 15px 0px rgba(0, 0, 0, 0.5);
    }

    .left {
        display: flex;
        width: 25%;
    }

    .left img {
        width: 80px;
        height: 80px;
    }

    .album_and_artist {
        display: flex;
        flex-direction: column;
        margin-left: 15px;
        justify-content: center;
    }

    .album_and_artist h1 {
        font-size: 15px;
        margin: 0;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }

    .album_and_artist p {
        font-size: 12px;
        font-weight: 500;
        color: #949494;
        margin: 0;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }

    .right {
        display: flex;
        width: 50%;
        justify-content: center;
        flex-direction: column;
    }

    .right .playbar {
        background-color: black;
        width: 100%;
        height: 5px;
        margin-top: 20px;
        border-radius: 20px;
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

    .buttons {
        width: 300px;
        display: flex;
        justify-content: space-around;
        margin-left: calc(50% - 150px);
    }

    .button {
        width: 30px;
        height: 30px;
    }

</style>
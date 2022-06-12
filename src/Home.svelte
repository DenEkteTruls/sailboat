<script>
	import SideBar from "./components/Sidebar.svelte";
	import AppList from "./components/apps/AppList.svelte";
	import ButtonList from "./components/apps/ButtonList.svelte";

	let apps = [
                {"title": "spotify", "icon": "icons/spotify.png"},
                {"title": "sailboat", "icon": "icons/sailboat.png"},
                {"title": "settings", "icon": "icons/settings.png"},
                {"title": "calculator", "icon": "icons/calculator.png"},
                {"title": "camera", "icon": "icons/camera.png"},
                {"title": "clock", "icon": "icons/clock.png"},
                {"title": "contacts", "icon": "icons/contacts.png"},
                {"title": "podcasts", "icon": "icons/podcasts.png"}
            ];
</script>


<body>
	<div class="container">
		<SideBar {apps}/>
		<AppList {apps}/>
		<ButtonList/>
	</div>
</body>


<style>
	body {
		width: 100vw;
		height: 100vh;
		margin: 0 auto;
		margin: -8px;
		overflow-y: hidden;
		font-family: 'Roboto', monospace;
	}

	.container {
		background-image: url("background.jpg");
		background-size: cover;
		background-position-y: -160px;
		margin: -8px;
	}
</style>

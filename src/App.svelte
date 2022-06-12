<script>
	import page from 'page';

	import Home from './Home.svelte';
	import Spotify from './Spotify.svelte';
	import Sailboat from './Sailboat.svelte';

	let current = Home;

	page('/', () => (current = Home));
	page('/spotify', () => (current = Spotify));
	page('/sailboat', () => (current = Sailboat));
	page.start();
</script>

<svelte:component this={current}/>
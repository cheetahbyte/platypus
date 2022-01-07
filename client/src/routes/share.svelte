<script lang="ts">
  import Logo from "../components/logo.svelte";
  import Footer from "../components/footer.svelte";
  import Theme from "../components/themeswitch.svelte";
  //
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  // vars
  let fid: string = $page.url.searchParams.get("id");
</script>

<Logo />
<Footer />
<Theme />
<center>
  <h3 style="color: #54a0ff;">The file was uploaded to the server !</h3>
</center>
<p ></p>
{fid}
<style>
  
  h3 {
    font-family: "Roboto", sans-serif;
  }
</style>

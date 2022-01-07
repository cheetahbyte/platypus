<script lang="ts">
import { onMount } from "svelte";

  import { SunIcon, MoonIcon } from "svelte-feather-icons";

  let darkMode: boolean = false;

  function changeMode() {
    darkMode = !darkMode;
    // set localstorage to darkmode
    localStorage.setItem("darkMode", JSON.stringify(darkMode));
    invokeMode()
  }
  function invokeMode() {
    if (darkMode) {
      document.body.classList.add("dark");
      document.body.classList.remove("light");
    } else {
      document.body.classList.remove("dark");
      document.body.classList.add("light");
    }
  }

  onMount(() => {
      darkMode = JSON.parse(localStorage.getItem("darkMode") || "false");
      invokeMode()
  })
</script>

<div>
    {#if darkMode}
  <div on:click={changeMode}>
    <SunIcon size="24" class="ts-icon" />
  </div>
{:else}
  <div on:click={changeMode}>
    <MoonIcon size="24" class="ts-icon" />
  </div>
{/if}
</div>

<style>
    div {
        position: absolute;
        top: 5%;
        right: 4%;
        cursor: pointer;
        transition: all ease-in-out 0.2s;
    }
    div:hover {
        transform: translateY(-2%)
    }
</style>
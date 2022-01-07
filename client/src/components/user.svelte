<script lang="ts">
  import { LogInIcon } from "svelte-feather-icons";
  // vars
  let loggedIn: boolean = false;

  // functions
  function redirect() {}
</script>

<div class="user-icon-login">
  {#if !loggedIn}
    <div on:click={() => {window.location.href="/login"}}>
      <LogInIcon />
    </div>
  {/if}
</div>

<script lang="ts">
  import Notification from "./notification.svelte";
  import { notifications } from "../stores/notification";
import { onDestroy } from "svelte";

  let nots;
  const unsubcribe = notifications.subscribe((n) => {
    nots = n;
  });

  onDestroy(unsubcribe)
</script>

<button
  on:click={() =>
    notifications.add({ title: "abc", description: "abc", color: "abc" })}
  >add not</button
>
<div class="notification-area">
  {#each nots as notification}
    <Notification {...notification} />
  {/each}
</div>

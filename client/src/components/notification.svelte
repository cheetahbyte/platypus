<script lang="ts">
    export const title: string = "abc";
    export const description: string = "abc";
    export const color: string = "abc"; 
    import {fly, fade} from "svelte/transition"
</script>

<div class="notification" in:fly={{ x: 50, duration: 1000 }} out:fade>
    {title} {description} {color}
</div>
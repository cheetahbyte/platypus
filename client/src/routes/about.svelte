<script lang="ts">
  import TypeScript from "../../assets/ts-logo-128.svg";
  import Python from "../../assets/python.svg";
</script>

<center>
  <h1>Used techniques</h1>
</center>
<div
  style="display: flex; flex-direction: row; width: 100%; justify-content: center; align-items: center;"
>
  <a href="https://svelte.dev">
    <img
      src="https://raw.githubusercontent.com/sveltejs/branding/master/svelte-logo.svg"
      alt="Svelte"
      class="icon"
    />
  </a>
  <a href="/">
    <img src={TypeScript} alt="Typescript" class="icon" />
  </a>
  <a href="https://www.python.org">
    <img src={Python} alt="Python" class="icon" />
  </a>

  <a href="https://fastapi.tiangolo.com">
    <img
      src="https://media.discordapp.net/attachments/857979752991031296/928213769899872326/fastapi.png"
      alt="FastAPI"
      class="icon"
    />
  </a>
  <a href="https://min.io">
    <img
      src="https://min.io/resources/img/logo/MINIO_Bird.png"
      alt="MinIO"
      class="icon minio"
    />
  </a>
</div>

<style>
  .icon {
    width: 50px; 
    height: 50px;
    margin-right: 50px;
    filter: grayscale(100%);
    transition: ease-in-out all 0.3s;
  }
  .icon:hover {
    filter: none;
    cursor: pointer;
    width: 55px;
    height: 55px;
  }

  .minio {
    height: 50px !important;
    width: unset !important;
  }
</style>

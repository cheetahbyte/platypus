<script lang="ts">
  import Logo from "../components/logo.svelte";
  import Footer from "../components/footer.svelte";
  import Theme from "../components/themeswitch.svelte";
  import User from "../components/user.svelte";
  let file;
  let sourceDark = "../../assets/dark-add.svg";

  async function handleFormSubmit() {
    let uploadFile = file[0];
    const formData = new FormData();
    formData.append("file", uploadFile);
    const resp = await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });
    const fileId = await resp.json();
    window.location.href = "/share?id=" + fileId;
  }
</script>

<Logo />
<Theme />
<User />
<center>
  <form on:submit|preventDefault={handleFormSubmit} class="upload">
    <div
      style="cursor: pointer;height: 100%; width: 100%;display: flex; align-items: center; justify-content: center;background: url('{sourceDark}') no-repeat center;"
    >
      <input
        type="file"
        bind:files={file}
        style="width: 100%; height: 100%; opacity: 0;cursor: pointer;"
      />
    </div>
    {#if file}
      <button type="submit">Upload</button>
    {/if}
  </form>
</center>
<Footer />

<style>
  .upload {
    margin-top: 2.5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: inherit;
    left: 50%;
    height: 39vh;
    width: 59vw;
    background: #dcdde1;
    border-radius: 7px;
    border: #353b48 dashed 5px;
    z-index:3;
  }
</style>

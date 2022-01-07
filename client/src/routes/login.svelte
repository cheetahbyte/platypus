<script lang="ts">
  import Logo from "../components/logo.svelte";
  import Footer from "../components/footer.svelte";
  import Theme from "../components/themeswitch.svelte";
  import {GithubIcon} from "svelte-feather-icons"
  import { onMount } from "svelte";
  let email: string;
  let password: string;

  async function login(){
      if (email && password) {
        let backendUrl = import.meta.env.VITE_BACKEND + "/user/login";
        let response = await fetch(backendUrl, {
          method: "POST",
          headers: { 
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            email: email,
            password: password
          })
        });
      }
  }
</script>

<Logo />
<Footer />
<Theme />
<center style="margin-top: -40px;">
  <div class="loginform">
    <h1>Login</h1>
    <!-- TODO: method and action-->
    <form 
    style="display: flex; flex-direction: column; justify-content: center; align-items: center;" on:submit|preventDefault={login}>
      <input name="username" type="email" placeholder="platy@pus.sy" required bind:value={email}/>
      <input name="password" type="password" placeholder="password" required bind:value={password}/>
      <button class="login-btn">Login</button>
    </form>
    <p style="font-family: 'Roboto', sans-serif; font-weight: 600; letter-spacing: 3px;color: #dcdde1;">or</p>
    <div class="github-login">
      <GithubIcon class="gh-icon"/>
      <p style="color: #dcdde1;">Login with GitHub</p>
    </div>
    <div class="google-login" style="margin-top: 20px;">
      <img src="../../assets/icons/google.png" alt="Google"/>
      <p>Login with Google</p>
    </div>
  </div>
</center>

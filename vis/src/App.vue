<template>
  <div id="app">
    <div class="centered-container">
      <Main></Main>
    </div>
  </div>
</template>

<script>
import Main from "@/components/Main";

export default {
  name: "App",
  components: { Main },
};
</script>

<style lang="scss">
html {
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 0;
  font-family: "IBM Plex Sans";
  background: rgba(20,20,20,1);
  color: rgba(255,255,255,0.7);
}

.centered-container {
  max-width: 50rem;
  margin: 0 auto;
  padding: 2rem 1rem;
}
</style>

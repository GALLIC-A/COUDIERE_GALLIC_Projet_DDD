<template>
  <router-view></router-view> <!-- C’est ici que les composants routés s’affichent -->
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body{
  height: 100h;
  width: 100%;
  background-color: #4f6a84;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  gap: 50px;
}
</style>

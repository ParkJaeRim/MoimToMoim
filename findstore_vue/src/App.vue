<template>
  <v-app id='app'>
    <navbar />
    <router-view />
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: {
    Navbar
  },
};
</script>

<style scoped>
#app {
  width: 400px;
  height: 600px;
  margin-right: auto;
  margin-left: auto;
}
</style>
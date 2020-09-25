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
    Navbar,
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
*{
  font-family: 'Jua', sans-serif;
  font-size: 13px;
}
</style>
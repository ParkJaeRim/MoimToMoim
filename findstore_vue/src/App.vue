<template>
  <v-row>
    <v-col class="d-none d-sm-block p-0" sm="6">
      <v-img
        src="@/assets/img/mainimg.png"
        height="750"
      ></v-img>
    </v-col>
    <v-col class="p-0" align="center" cols="12" sm="6">
      <v-app class="phone">
        <navbar />
        <router-view />
      </v-app>
    </v-col>
  </v-row>
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
.phone {
  max-width: 400px;
  border: solid 1px rgba(0, 0, 0, 0.258);
}
</style>
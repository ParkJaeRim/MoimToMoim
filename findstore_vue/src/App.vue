<template>
  <v-row>
    <!-- <p>{{test}}</p> -->
    <v-col class="d-none d-sm-block p-0" sm="6">
      <v-img src="@/assets/img/mainimg.png" height="700"></v-img>
    </v-col>
    <v-col class="p-0" align="center" cols="12" sm="6">
      <v-app :class="controlSize">
        <v-btn color="deep-purple lighten-3" dark class="backBnt" fab small onclick="history.back()">
          <v-icon dark>mdi-arrow-left</v-icon>
        </v-btn>
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
  data() {
    return {
      controlSize: "phone1",
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      if (576 > window.innerWidth) {
        this.controlSize = "phone2"
      } else {
        this.controlSize = "phone1"
      }
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  font-size: 13px;
}
.phone1 {
  max-width: 400px;
  border: solid 1px rgba(0, 0, 0, 0.258);
  height: 700px;
  overflow: auto;
}
.phone2 {
  max-width: 400px;
  border: solid 1px rgba(0, 0, 0, 0.258);
}
.backBnt {
  position: fixed;
  margin:20px;
  bottom: 6vh;
  z-index:10;
}
</style>
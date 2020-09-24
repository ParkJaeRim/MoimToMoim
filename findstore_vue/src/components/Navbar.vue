<template>
  <v-bottom-navigation>
    <v-btn height="100%" :to="{name: 'meetinglist'}">
      <span>Moim</span>
      <v-icon>far fa-calendar-alt</v-icon>
    </v-btn>

    <v-btn height="100%" v-if="!isLoggedIn" :to="{name: 'home'}">
      <span>Login</span>
      <v-icon>fas fa-key</v-icon>
    </v-btn>

    <v-btn height="100%" v-if="isLoggedIn" :to="{name: 'detailmain'}">
      <span>MyPage</span>
      <v-icon>fas fa-user-circle</v-icon>
    </v-btn>

    <v-btn height="100%" v-if="isLoggedIn" @click.native="logout">
      <span>logout</span>
      <v-icon>fas fa-key</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import axios from "axios";
import constants from "../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  data() {
    return {
      isLoggedIn: false,
    };
  },
  created() {
    this.isLogin()
  },
  methods: {
    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(SERVER_URL + "/rest-auth/logout/", null, config)
        .catch((err) => console.log(err.response))
        .finally(() => {
          this.$cookies.remove("auth-token");
          this.$router.push({ name: "home" });
          this.isLogin()
        });
    },
    isLogin() {
      this.isLoggedIn = this.$cookies.isKey("auth-token");
      this.drawer = true;
    },
  },
};
</script>

<style scoped>
</style>

<template>
  <div class="overflow-hidden">
    <v-app-bar dense>
      <v-app-bar-nav-icon @click="isLogin" class="ml-auto"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class=" text--accent-4">
          <v-list-item :to="{name: 'meetinglist'}">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>모임리스트</v-list-item-title>
          </v-list-item>

          <!-- <v-list-item :to="{name: 'home'}">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item> -->

          <v-list-item v-if="!isLoggedIn" :to="{name: 'login'}">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="isLoggedIn" @click.native="logout">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{name: 'articlelist'}">
            <v-list-item-icon>
              <v-icon>fas fa-list</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Article</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      drawer: false,
      group: null,
      isLoggedIn: false,
    };
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
        });
    },
    isLogin() {
      this.isLoggedIn = this.$cookies.isKey("auth-token");
      this.drawer = true;
    },
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>

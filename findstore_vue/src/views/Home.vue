<template>
<v-container>
  <v-row justify="center">
    <v-col md="10" class="py-0">
      <v-img
        src="@/assets/img/mainimg.png"
        max-width="400"
        max-height="250"
      />
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
          </v-row>
        </template>
      <br />

      <v-container>
        <v-row justify="center">
          <v-col cols="8" md="4">
            <v-text-field
              v-model="loginData.username"
              :rules="nameRules"
              :counter="10"
              label="ID"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="8" md="4">
            <v-text-field
              v-model="loginData.password"
              :rules="passwordRules"
              :counter="12"
              :type="show1 ? 'text' : 'password'"
              label="Password"
              hint="At least 8 characters"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <br />
        <br/>
        <div class="d-flex justify-space-between">
          <v-btn text color="primary" :to="{name: 'signup'}">Join</v-btn>
          <v-btn text color="primary" @click="login">login</v-btn>
        </div>
      </v-container>
    </v-col>
  </v-row>
</v-container>
</template>



<script>
import axios from "axios";
import constants from "../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "Home",
  data() {
    return {
      show1: false,
      valid: false,
      loginData: {
        username: "",
        password: "",
      },
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 10 || "Name must be less than 10 characters",
      ],
      passwordRules: [
        (value) => !!value || "Required.",
        (v) => v.length >= 8 || "Min 8 characters",
      ],
    };
  },
  created() {
    this.isLogin()
  },
  methods: {
    login() {
      axios
        .post(SERVER_URL + "/rest-auth/login/", this.loginData)
        .then((res) => {
          this.$cookies.set("auth-token", res.data.key);
          this.$router.go();
          this.isLogin();
        })
        .catch((err) => {
          console.log(err.response.data);
          alert("아이디와 비밀번호를 확인하고 다시 로그인 해주세요.");
        });
    },
    isLogin() {
      if (this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "meetinglist" });
      }
    },
  },
};
</script>

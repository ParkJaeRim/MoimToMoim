<template>
  <div>
    <h1>Login</h1>

    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="loginData.username"
              :rules="nameRules"
              :counter="10"
              label="ID"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="loginData.password"
              :rules="passwordRules"
              :counter="10"
              :type="show1 ? 'text' : 'password'"
              label="Password"
              hint="At least 8 characters"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-btn rounded color="primary" dark @click="login">Submit</v-btn>
        <v-btn :to="{name: 'signup'}">Signup</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "Login",
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
  
  methods: {
    login() {
      axios
        .post(SERVER_URL + "/rest-auth/login/", this.loginData)
        .then((res) => {
          this.$cookies.set("auth-token", res.data.key);
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err.response.data);
          alert("아이디와 비밀번호를 확인하고 다시 로그인 해주세요.");
        });
    },
  },
};
</script>

<style>
</style>
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
      <v-form ref="form">
      <v-container>
        <v-row justify="center">
          
          <v-col cols="10" md="6">
            <v-text-field
              v-model="loginData.username"
              :rules="nameRules"
              :counter="10"
              label="아이디"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="10" md="6">
            <v-text-field
              v-model="loginData.password"
              :rules="passwordRules"
              :counter="12"
              :type="show1 ? 'text' : 'password'"
              label="비밀번호"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
          </v-col>
          
        </v-row>
        <br />
        <br/>
        <div class="d-flex justify-space-between">
          <v-btn text color="orange" :to="{name: 'signup'}">회원가입</v-btn>
          <v-btn text color="orange" @click="login">로그인</v-btn>
        </div>
      </v-container>
      </v-form>
    </v-col>
  </v-row>
</v-container>
</template>



<script>
import axios from "axios";
import constants from "../lib/constants";
import swal from "sweetalert2";

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
        (v) => !!v || "입력해주세요",
        (v) => v.length <= 10 || "10글자 초과",
      ],
      passwordRules: [
        (value) => !!value || "입력해주세요",
        (v) => v.length >= 8 || "8글자 미만",
      ],
    };
  },
  created() {
    this.isLogin()
  },
  methods: {
    login() {
      if (!this.$refs.form.validate()) return;
      axios
        .post(SERVER_URL + "/rest-auth/login/", this.loginData)
        .then((res) => {
          this.$cookies.set("auth-token", res.data.key, 60 * 60 * 12);
          this.$router.go();
          this.isLogin();
        })
        .catch((err) => {
          console.log(err.response.data);
          swal
            .fire({
            text: "아이디와 비밀번호를 확인해주세요",
            
            icon: "warning",
            showConfirmButton: false,
            timer: 1000,
          })
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

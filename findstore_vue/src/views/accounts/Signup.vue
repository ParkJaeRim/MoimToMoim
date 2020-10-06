<template>
  <v-container>
  <div>
    <br>
    <h1>회원가입</h1>

    <v-form v-model="valid" ref="form">
      <v-container>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.username"
              :rules="nameRules"
              :counter="10"
              label="아이디"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.email"
              :rules="emailRules"
              label="이메일"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.password"
              :rules="passwordRules"
              :counter="10"
              :type="show1 ? 'text' : 'password'"
              label="비밀번호"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.password2"
              :rules="passwordRules2"
              :counter="10"
              :type="show2 ? 'text' : 'password'"
              label="비밀번호 확인"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.nickname"
              :counter="10"
              :rules="nicknameRules"
              :type="show2 ? 'text' : 'nickname'"
              label="닉네임"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="signupData.age"
              :type="show2 ? 'text' : 'age'"
              :rules="ageRules"
              label="나이"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="8">
            <v-container fluid>
              <v-checkbox
                v-model="signupData.sex"
                :rules="sexRules"
                label="남자"
                value="1"
              ></v-checkbox>
              <v-checkbox
                v-model="signupData.sex"
                :rules="sexRules"
                label="여자"
                value="0"
              ></v-checkbox>
            </v-container>
          </v-col>
        </v-row>
        <v-btn text color = "orange" @click="signup">가입하기</v-btn>
      </v-container>
    </v-form>
  </div>
  </v-container>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "Signup",
  data() {
    return {
      show1: false,
      show2: false,
      valid: true,
      signupData: {
        username: "",
        email: "",
        password: "",
        password2: "",
        nickname: "",
        sex: "",
        age: "",
      },

      nameRules: [
        (v) => !!v || "입력해주세요",
        (v) => v.length <= 10 || "10글자 초과입니다",
      ],
      passwordRules: [
        (value) => !!value || "입력해주세요",
        (v) => v.length >= 8 || "8글자 미만입니다",
      ],
      passwordRules2: [
        (value) => !!value || "입력해주세요",
        (v) => v === this.signupData.password || "비밀번호가 다릅니다",
      ],
      emailRules: [
        (v) => !!v || "입력해주세요",
        (v) => /.+@.+/.test(v) || "이메일 형식이 다릅니다",
      ],
      nicknameRules: [
        (v) => !!v || "입력해주세요",
        (v) => v.length <= 10 || "10글자 초과입니다",
      ],
      ageRules: [
        (v) => !!v || "입력해주세요",
      ],
      sexRules: [
        (v) => !!v || "체크해주세요",
      ],
    };
  },

  created() {
    this.move();
  },

  methods: {
    signup() {
      if (!this.$refs.form.validate()) return;
      axios
        .post(SERVER_URL + "/accounts/register/", this.signupData)
        .then(() => {
          var loginData = {
            username: this.signupData.username,
            password: this.signupData.password,
          };
          axios
            .post(SERVER_URL + "/rest-auth/login/", loginData)
            .then((res) => {
              this.$cookies.set("auth-token", res.data.key);
              this.createIndv(res.data.key);
              this.$router.go();
            })
            .catch(() => {
              alert("아이디와 비밀번호를 확인하고 다시 로그인 해주세요.");
            });
        })
        .catch((err) => {
          if(err.response.data.username) {
            if(err.response.data.username[0] == "해당 사용자 이름은 이미 존재합니다.") {
              alert(err.response.data.username[0]);
            } else {
              alert("정보를 확인해주세요");
            }
          } else {
            alert("정보를 확인해주세요");
          }
        });
    },

    move() {
      if (this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "home" });
      }
    },

    createIndv(token) {

      const config = {
        headers: {
          Authorization: "Token " + token,
        },
      };

      const initmeeting = {
        title: "혼자놀기",
        avg_age: "30",
        ppl: "1",
        background_img: "http://asq.kr/nsfFB40GtBBr",
      };

      axios
        .post(SERVER_URL + "/meeting/create/", initmeeting, config)
        .then(() => {
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>

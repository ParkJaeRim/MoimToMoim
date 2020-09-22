<template>
  <div>
    <h1>회원가입</h1>

    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.username"
              :rules="nameRules"
              :counter="10"
              label="ID"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.email"
              :rules="emailRules"
              label="email"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.password"
              :rules="passwordRules"
              :counter="10"
              :type="show1 ? 'text' : 'password'"
              label="Password"
              hint="At least 8 characters"
              @click:append="show1 = !show1"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.password2"
              :rules="passwordRules"
              :counter="10"
              :type="show2 ? 'text' : 'password'"
              label="Password2"
              hint="At least 8 characters"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.nickname"
              :counter="10"
              :type="show2 ? 'text' : 'nickname'"
              label="nickname"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="signupData.age"
              :type="show2 ? 'text' : 'age'"
              label="age"
              @click:append="show2 = !show2"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-container fluid>
              <v-checkbox v-model="signupData.sex" label="Male" value="1"></v-checkbox>
              <v-checkbox v-model="signupData.sex" label="Female" value="0"></v-checkbox>
            </v-container>
          </v-col>

        </v-row>
        <v-btn rounded color="primary" dark @click="signup">Submit</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: "Signup",
  data() {
    return {
      show1: false,
      show2: false,
      valid: false,
      signupData: {
        username: "",
        email:"",
        password: "",
        password2: "",
        nickname:"",
        sex:"",
        age:""
      },
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 10 || "Name must be less than 10 characters",
      ],
      passwordRules: [
        (value) => !!value || "Required.",
        (v) => v.length >= 8 || "Min 8 characters",
      ],
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+/.test(v) || "E-mail must be valid",
      ]
    };
  },
  methods: {
    signup() {
      console.log(this.signupData)
      axios.post(SERVER_URL + '/accounts/register/', this.signupData)
        .then((res) => {
          this.$cookies.set('auth-token', res.data.key)
          this.$router.push({ name: 'home' })
        })
        .catch((err) => {
          // if (err.response.data[0] == "A user with that username already exists.") {
          //   alert('중복된 아이디가 존재합니다.')
          // } else if (err.response.data[0] == 'username') {
          //   alert('중복된 아이디가 존재합니다.')
          // }
          console.log(err.response.data);
        })
    },
  }
};
</script>

<style>
</style>
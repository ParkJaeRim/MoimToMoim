<template>
  <v-card class="mx-auto" max-width="400">
    <v-container>
      <div>
        닉네임 : {{form.nickname}}
        <br />
        나이 : {{form.age}}
        <br />
        <div v-if="1 === 'form.sex'">성별 : 남</div>
        <div v-else>성별 : 여</div>
        이메일 : {{form.email}}
        <br />
      </div>
      <!-- <v-text-field v-model="form.nickname" label="Nickname"></v-text-field>
            <v-text-field v-model="headers.age" label="Age"></v-text-field>
            <v-text-field v-model="form.sex" label="Sex"></v-text-field>
      <v-text-field v-model="form.email" label="Email"></v-text-field>-->
      <div class="d-flex justify-space-between">
        <v-btn @click="userUpdate">modify</v-btn>
        <v-btn @click="userDelete">delete</v-btn>
      </div>
    </v-container>
  </v-card>
</template>
<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "Detail",
  data: () => {
    return {
      headers: [
        { text: "nickname", value: "nickname" },
        { text: "email", value: "email" },
        { text: "sex", value: "sex" },
        { text: "age", value: "age" },
        { text: "username", value: "username" },
      ],
      form: {},
    };
  },
  created() {
    this.userData();
  },
  methods: {
    userUpdate() {
      axios
        .post(SERVER_URL + "/accounts/update/", this.updateData)
        .then((res) => {
          this.$cookies.remove("auth-token");
          const token = res.data.object;
          this.$cookies.set("auth-token", token);
          alert("수정 되었습니다.");
          // this.$router.go();
        })
        .catch((err) => {
          console.log(err.response.data.errors[0]);
          alert(err.response.data.errors[0].field + "를 확인해 주세요");
        });
    },
    userDelete() {
        axios
        .get(SERVER_URL + "/accounts/delete/" + this.form.username)
        .then(() => {
          this.$cookies.remove("auth-token");
          alert("회원탈퇴되었습니다.");
          this.$router.push({
          name: "home",
          });
        })
        .catch((err) => {
          alert("입력 정보를 호가인해주세요.");
          console.log(err);
        });
    },
    userData() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/accounts/user/", config)
        .then((res) => {
          this.form = res.data;
          // console.log(res.data);
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  },
};
</script>

<style>
</style>
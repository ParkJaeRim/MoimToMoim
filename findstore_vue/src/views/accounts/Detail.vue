<template>
  <v-card fluid>
      <v-layout column>
            <v-container>
                <v-div cols="12" sm="6" md="4">
                  <v-text-field v-model="form.nickname" label="Nickname"></v-text-field>
                </v-div>
                <br>
                <v-div cols="12" sm="6" md="4">
                  <v-text-field v-model="form.sex" label="Sex"></v-text-field>
                </v-div>
                <br>
                <v-div cols="12" sm="6" md="4">
                  <v-text-field v-model="form.age" label="Age"></v-text-field>
                </v-div>
            </v-container>
      </v-layout>
  </v-card>
</template>
<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "profile",
  data: () => {
    return {
      articles: [],
      headers: [
        { text: "nickname", value: "nickname" },
        { text: "email", value: "email" },
        { text: "sex", value: "sex" },
        { text: "age", value: "age" },
      ],
      form: {
        nickname: "",
        email: "",
        sex: "",
        age: "",
      },
      updateData: {
        email: "",
        passowrd: "",
        nickname: "",
        age: "",
      },
      deleteData: {
        nickname: "",
        email: "",
        passowrd: "",
      },
    };
  },
  methods: {
    userUpdate() {
      axios
        .post(SERVER_URL + "/accounts/update", this.updateData)
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
        .post(SERVER_URL + "/accounts/delete/", this.deleteData)
        // uid 추가해줘야됨, 어떻게 넣는지 모르겠슴
        .then((res) => {
          this.$cookies.remove("auth-token");
          const token = res.data.object;
          this.$cookies.set("auth-token", token);
          alert("회원탈퇴되었습니다.");
          // this.$router.go();
        })
        .catch((err) => {
          alert("입력 정보를 호가인해주세요.");
          console.log(err);
        });
    },
    save() {
      console.log(this.form);
      var tmp_url = "/acoounts/user/";
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(SERVER_URL + tmp_url, this.form, config)
        .then((res) => {
          console.log(res.data);
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
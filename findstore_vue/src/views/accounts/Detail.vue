<template>
  <v-container>
    <h1 class="my-5">{{ form.username }} 님</h1>
        <v-text-field
          v-model="form.nickname"
          :counter="10"
          :type="show2 ? 'text' : 'nickname'"
          label="nickname"
          @click:append="show2 = !show2"
          required
        ></v-text-field>

        <v-text-field
          v-model="form.email"
          :rules="emailRules"
          label="email"
          required
        ></v-text-field>

        <v-text-field
          v-model="form.age"
          :type="show2 ? 'text' : 'age'"
          label="age"
          @click:append="show2 = !show2"
          required
        ></v-text-field>

        <v-radio-group v-model="form.sex">
          <v-radio 
            class="left"
            label="남자"
            value="0"
            color="success"
          ></v-radio>
          <v-radio
            class="right"
            label="여자"
            value="1"
            color="success"
          ></v-radio>
        </v-radio-group>

        <div class="right">
          <v-btn @click="userDelete">회원탈퇴</v-btn>
          <v-btn @click="userUpdate">수정완료</v-btn>
          <v-btn @click="goBack">취소</v-btn>
        </div>
  </v-container>
</template>
<script>
import axios from "axios";
import constants from "../../lib/constants";
import swal from "sweetalert2";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "Detail",

  data: () => {
    return {
      show1: false,
      show2: false,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 10 || "Name must be less than 10 characters",
      ],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      form: {
        age: "",
        email: "",
        nickname: "",
        sex: "",
        username: "",
      },
    };
  },

  created() {
    this.userData();
  },

  methods: {
    goBack() {
      this.$router.push({
        name: "detailmain",
      });
    },

    userUpdate() {
      console.log(this.form);
      axios
        .put(SERVER_URL + "/accounts/update/", this.form, {
          headers: {
            Authorization: `Token ${this.$cookies.get("auth-token")}`,
          },
        })
        .then((res) => {
          this.form.nickname = res.data.nickname;
          this.form.username = res.data.username;
          this.form.age = res.data.age;
          this.form.email = res.data.email;
          this.form.sex = res.data.sex;

          swal
            .fire({
              text: "수정되었습니다",
            })
            .then(() => {
              this.$router.push({ name: "detailmain" });
            });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    userDelete() {
      swal
        .fire({
          title: "회원 탈퇴",
          text: "탈퇴하시겠습니까 ?",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "OK",
        })
        .then((res) => {
          if (res.isConfirmed) {
            axios
              .get(SERVER_URL + "/accounts/delete/" + this.form.username)
              .then(() => {
                this.$cookies.remove("auth-token");
                this.$router.go();
              })
              .catch((err) => {
                alert("입력 정보를 확인해주세요.");
                console.log(err);
              });
          }
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
          this.form.nickname = res.data.nickname;
          this.form.username = res.data.username;
          this.form.age = res.data.age;
          this.form.email = res.data.email;
          this.form.sex = res.data.sex;
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
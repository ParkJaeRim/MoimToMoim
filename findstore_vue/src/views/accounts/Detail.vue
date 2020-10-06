<template>
  <v-container>
    <v-form ref="check">
      <h1 class="my-5">{{ form.username }} 님</h1>

      <v-text-field
        v-model="form.nickname"
        :counter="10"
        :rules="nicknameRules"
        :type="show2 ? 'text' : 'nickname'"
        label="닉네임"
        @click:append="show2 = !show2"
        required
      ></v-text-field>

      <v-text-field
        v-model="form.email"
        :rules="emailRules"
        label="이메일"
        required
      ></v-text-field>

      <v-text-field
        v-model="form.age"
        :type="show2 ? 'text' : 'age'"
        label="나이"
        :rules="ageRules"
        @click:append="show2 = !show2"
        required
      ></v-text-field>

      <v-checkbox
        v-model="form.sex"
        :rules="sexRules"
        label="남자"
        value="1"
        color="orange"
      ></v-checkbox>
      <v-checkbox
        v-model="form.sex"
        :rules="sexRules"
        label="여자"
        color="orange"
        value="0"
      ></v-checkbox>

      <div class="right">
        <v-btn text style="font-size: 16px; color: orange" @click="userDelete"
          >회원탈퇴</v-btn
        >
        <v-btn text style="font-size: 16px; color: orange" @click="userUpdate"
          >수정완료</v-btn
        >
      </div>
    </v-form>
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
      form: {
        age: "",
        email: "",
        nickname: "",
        sex: "",
        username: "",
      },
      emailRules: [
        (v) => !!v || "입력해주세요",
        (v) => /.+@.+/.test(v) || "이메일 형식이 다릅니다",
      ],
      nicknameRules: [
        (v) => !!v || "입력해주세요",
        (v) => v.length <= 10 || "10글자 초과입니다",
      ],
      ageRules: [(v) => !!v || "입력해주세요"],
      sexRules: [(v) => !!v || "체크해주세요"],
    };
  },

  created() {
    this.move();
    if (this.$cookies.isKey("auth-token")) {
      this.userData();
    }
  },

  methods: {
    userUpdate() {
      if (!this.$refs.check.validate()) return;
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
              title: "수정되었습니다",
              icon: "success",
              showConfirmButton: false,
              timer: 1000,
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
          title: "탈퇴하시겠습니까?",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "orange",
          cancelButtonColor: "orange",
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

    move() {
      if (!this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "home" });
      }
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
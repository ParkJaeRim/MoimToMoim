<template>
  <div>
    <v-container class="d-flex justify-space-between" max-width="400">
      <v-row>
        <div>
          <v-responsive
            class="text-center yellow lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3"
            height="64"
            width="64"
          ></v-responsive>
        </div>
        <v-row align="center">
          <h1>...{{headers.nickname}}</h1>
        </v-row>
        <v-row align="center" justify="center">
          <v-icon>fas fa-cog</v-icon>
        </v-row>
      </v-row>
    </v-container>
    <br />

    <div class="d-flex justify-space-between" max-width="400">
      <v-row align="center" justify="center">
        <v-col class="text-center" col="6">
          <div>
            <v-btn text color="primary" style ="font-size: 25px">3</v-btn>
          </div>
          <div>
            <v-btn text  style ="font-size: 19px" >내 약속</v-btn>
          </div>
        </v-col>
      </v-row>

      <v-row align="center" justify="center">
        <v-col class="text-center" col="6">
          <div>
            <v-btn text color="primary" style ="font-size: 25px">1</v-btn>
          </div>
          <div>
            <v-btn text style ="font-size: 19px">완료</v-btn>
          </div>
        </v-col>
      </v-row>
    </div>
    <br>
    <v-container>
        
    </v-container>

  </div>
</template>




<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "DetailMain",
  data: () => {
    return {
      headers: [
        { text: "nickname", value: "nickname" },
        { text: "email", value: "email" },
        { text: "sex", value: "sex" },
        { text: "age", value: "age" },
        { text: "username", value: "username" },
      ],
    };
  },
  created() {
    this.userData();
  },
  methods: {
    userData() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/accounts/user/", config)
        .then((res) => {
          this.headers = res.data;
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
.v-text-field input {
    font-size: 2.0em;
  }
.btnn { 
}
</style>
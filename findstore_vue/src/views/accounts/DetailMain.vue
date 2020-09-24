<template>
  <div>
    <v-container>
      <div>
        <v-row dense class="each-row mx-auto" align="center" justify="center">
          <v-col align="center" justify="center">
            <v-responsive
              class="text-center deep-purple lighten-4 rounded-circle d-inline-flex ma-3"
              height="64"
              width="64"
            ></v-responsive>
          </v-col>
          <v-col class="mx-auto">
            <h1>{{headers.nickname}}</h1>
          </v-col>
          <v-col class="each-row mx-auto" align="end">
            <v-icon>fas fa-cog</v-icon>
          </v-col>
        </v-row>
      </div>

      <div class="d-flex justify-space-between" max-width="400">
        <v-row align="center" justify="center">
          <v-col class="text-center" col="6">
            <div>
              <v-btn text color="primary" style="font-size: 25px">{{promiseListIsfinish0.length}}</v-btn>
            </div>
            <div>
              <v-btn text style="font-size: 19px">내 약속</v-btn>
            </div>
          </v-col>
        </v-row>

        <v-row align="center" justify="center">
          <v-col class="text-center" col="6">
            <div>
              <v-btn text color="primary" style="font-size: 25px">{{promiseListIsfinish1.length}}</v-btn>
            </div>
            <div>
              <v-btn text style="font-size: 19px">완료</v-btn>
            </div>
          </v-col>
        </v-row>
      </div>
    <br/>
    <div v-for="item in promiseList" :key="item.id">
      <v-row class="each-row mx-auto">
        <v-col cols="9" class="pr-0 pb-0">
          <p class="text-truncate" style="font-size : 15px"> {{item.title}} / {{item.date.substring(2,4)}}.{{item.date.substring(5,7)}}.{{item.date.substring(8,10)}} / {{item.meeting.title}}</p>
        </v-col>
        <v-col cols="3" class="pt-1 pl-0 pb-0">
          <!-- p는 패딩 m은 마진 t b l r (top, bottom, left, right) x축 y축 auto 자동 /  -->
          <v-btn text color="primary" style="font-size : 15px">완료</v-btn>
        </v-col>
      </v-row>

      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" :style="style">
            <table>
              <tbody>
                <tr>
                  <img
                    src="https://mp-seoul-image-production-s3.mangoplate.com/added_restaurants/104601_1490349745059944.jpg"
                    width="100px"
                    height="100px"
                  />
                </tr>
                <tr class="storename">{{item.name}}</tr>
              </tbody>
            </table>
          </slideritem>
        </slider>
      </v-row>
      <br/>
    </div>

    </v-container>
  </div>
</template>




<script>
import axios from "axios";
import { slider, slideritem } from "vue-concise-slider";

import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;
export default {
  name: "promiseList",
  data: () => {
    return {
      promiseList: {},
      headers: [
        { text: "nickname", value: "nickname" },
        { text: "email", value: "email" },
        { text: "sex", value: "sex" },
        { text: "age", value: "age" },
        { text: "username", value: "username" },
      ],
      likes: [
        { name: "열혈쭈꾸미", img: "" },
        { name: "스트라다로스터스", img: "" },
        { name: "커피식탁", img: "" },
        { name: "야상해", img: "" },
        { name: "아빠손칼국수", img: "" },
        { name: "그린브라우니", img: "" },
      ],
      options: {
        pagination: false,
        currentPage: 0,
        tracking: false,
        slidesToScroll: 1,
        loop: false,
      },
      style: {
        width: "31.5%",
        "margin-right": "2%",
        "font-size": "15px",
      },
      promiseListIsfinish1: [],
      promiseListIsfinish0: [],
    };
  },
  components: {
    slider,
    slideritem,
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
          this.promiseData();
          // console.log(res.data);
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    promiseData() {
      axios
        .get(SERVER_URL +"/promise/" + this.headers.username + "/list/")
        .then((res) => {
          this.promiseList = res.data;
          console.log(res.data);

          this.promiseListIsfinish1 = this.promiseList.filter(
            (item) => item.isfinish == 1
          );

          this.promiseListIsfinish0 = this.promiseList.filter(
            (item) => item.isfinish == 0
          );
        })
        .catch((err) => console.log(err.res));
    },
  },
};
</script>




<style>
.storename {
  color: black;
}
.each-row {
  vertical-align: middle;
}
</style>
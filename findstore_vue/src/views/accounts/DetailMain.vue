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
            <h1>{{ headers.nickname }}</h1>
          </v-col>
          <v-col class="each-row mx-auto" align="end">
            <v-icon @click="goDetail">fas fa-cog</v-icon>
          </v-col>
        </v-row>
      </div>

      <div class="d-flex justify-space-between" max-width="400">
        <v-row align="center" justify="center">
          <v-col class="text-center" col="6">
            <div>
              <v-btn
                text
                color="primary"
                style="font-size: 25px"
                @click="promiseList.isfinish = 0"
                >{{ promiseListIsfinish0.length }}</v-btn
              >
            </div>
            <div>
              <v-btn
                text
                style="font-size: 19px"
                @click="promiseList.isfinish = 0"
                >내 약속</v-btn
              >
            </div>
          </v-col>
        </v-row>

        <v-row align="center" justify="center">
          <v-col class="text-center" col="6">
            <div>
              <v-btn
                text
                color="primary"
                style="font-size: 25px"
                @click="promiseList.isfinish = 1"
                >{{ promiseListIsfinish1.length }}
              </v-btn>
            </div>
            <div>
              <v-btn
                text
                style="font-size: 19px"
                @click="promiseList.isfinish = 1"
                >완료</v-btn
              >
            </div>
          </v-col>
        </v-row>
      </div>
      <!-- 
        <div v-if = !promiseList.isfinish>
          promiseList = promiseListIsfinish0
        </div>
        <div v-if = promiseList.isfinish>
          promiseList = promiseListIsfinish1
        </div> -->
      <div v-for="item in promiseList" :key="item.id">
        <br /><br />
        <v-row>
          <v-col cols="9" class="pr-0 pb-0">
            <p class="text-truncate" style="font-size: 15px">
              {{ item.title }} / {{ item.date.substring(2, 4) }}.{{
                item.date.substring(5, 7)
              }}.{{ item.date.substring(8, 10) }} / {{ item.meeting.title }}
            </p>
          </v-col>
          <v-col cols="3" class="pt-1 pl-0 yb-0">
            <!-- p는 패딩 m은 마진 t b l r (top, bottom, left, right) x축 y축 auto 자동 /  -->
            <v-btn text color="primary" style="font-size: 15px">완료</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <slider ref="slider" :options="options">
            <slideritem
              v-for="(item2, i) in item.reslist"
              :key="i"
              :style="styleRecom"
            >
              <v-img
                v-if="item2.img !== null"
                class="white--text"
                :src="item2.img"
                width="120px"
                height="150px"
                @click="goStoreDetail(item2.id)"
              >
                <div class="transbox white--text">
                  <div class="store_name">{{ item2.name }}</div>
                </div>
              </v-img>
              <v-img
                v-if="item2.img == null"
                class="white--text one"
                src="http://asq.kr/JNlr0nxp6EQN"
                width="170px"
                height="170px"
                @click="goStoreDetail(item2.id)"
              >
                <div class="transbox white--text">
                  <div class="store_name">{{ item2.name }}</div>
                </div>
              </v-img>
            </slideritem>
          </slider>
        </v-row>
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
      storeInfos: [],
      headers: [],
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
      promiseListIsfinish1: {},
      promiseListIsfinish0: {},

      styleRecom: {
        width: "31.5%",
        "margin-right": "2%",
        "font-size": "13px",
      },
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
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    promiseData() {
      axios
        .get(SERVER_URL + "/promise/" + this.headers.username + "/list/")
        .then((res) => {
          this.promiseList = res.data;

          console.log(this.promiseList);
          // this.storeInfos = this.promiseList[1].reslist;
          // console.log(this.storeInfos);
          this.promiseListIsfinish1 = res.data.filter(
            (item) => item.isfinish == 1
          );

          this.promiseListIsfinish0 = res.data.filter(
            (item) => item.isfinish == 0
          );
          console.log("dddddd");
          console.log(this.promiseListIsfinish0);
        })
        .catch((err) => console.log(err.res));
    },
    goStoreDetail(s_id) {
      this.$router.push({
        name: "storedetail",
        params: {
          p_id: 0,
          s_id: s_id,
        },
      });
    },
    goDetail() {
      this.$router.push({
        name: "detail",
      });
    }
  },
};
</script>




<style scoped>
.each-row {
  vertical-align: middle;
  margin-top: 30px;
}

.promise {
  color: black;
}
.transbox {
  text-align: center;
  background-color: rgba(118, 126, 154, 0.4);
  height: 100%;
}

.store_name {
  font-size: 14px;
  font-weight: 400;
  padding-top: 50%;
}
</style>
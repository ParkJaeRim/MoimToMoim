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
                color="deep-purple lighten-2"
                style="font-size: 25px"
                @click="cnt = 0"
              >
                {{ infoZero[0] }}
              </v-btn>
            </div>
            <div>
              <v-btn text style="font-size: 19px" @click="cnt = 0"
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
                color="deep-purple lighten-2"
                style="font-size: 25px"
                @click="cnt = 1"
              >
                {{ infoZero[1] }}
              </v-btn>
            </div>
            <div>
              <v-btn text style="font-size: 19px" @click="cnt = 1">완료</v-btn>
            </div>
          </v-col>
        </v-row>
      </div>

      <div v-for="(item, k) in promiseList" :key="item.id">
        <div v-if="item.isfinish == cnt">
          <br /><br />
          <v-row>
            <v-col cols="9" class="pr-0 pb-0">
              <p v-on:click="goCourse(item.id)" class="text-truncate" style="font-size: 15px">
                {{ item.title }} / {{ item.date.substring(2, 4) }}.{{
                  item.date.substring(5, 7)
                }}.{{ item.date.substring(8, 10) }} / {{ item.meeting.title }}
                <v-badge
                inline
                color="deep-purple lighten-4"
                icon="mdi-lead-pencil"
              ></v-badge>
              </p>
            </v-col>

            <v-col cols="3" class="pt-1 pl-0 yb-0">
              <!-- p는 패딩 m은 마진 t b l r (top, bottom, left, right) x축 y축 auto 자동 /  -->

              <v-dialog
                v-model="dialog"
                max-width="290px"
                align="center"
                justify="center"
              >
                <template v-slot:activator="{ on }">
                  <v-btn
                    v-if="item.isfinish == 0"
                    text
                    color="primary"
                    style="font-size: 15px"
                    v-on="on"
                    >완료</v-btn
                  >
                </template>

                <v-card>
                  <v-card-title>
                    <span class="headline">리뷰를 남겨주세요.</span>
                  </v-card-title>

                  <v-container>
                    <v-card>
                      <v-row>
                        <v-col>
                          <v-card-text>
                            {{ item.reslist[y].name }}
                            <v-img
                              v-if="item.reslist[y].img !== null"
                              class="white--text"
                              :src="item.reslist[y].img"
                              width="270px"
                              height="150px"
                            ></v-img>

                            <br /><br />
                            <v-rating
                              v-model="reviewdata.rating"
                              background-color="orange lighten-3"
                              color="orange"
                              large
                            ></v-rating>
                            <br />
                            <v-text-field
                              v-model="reviewdata.review"
                              label="리뷰를 작성해주세요."
                              required
                            >
                            </v-text-field>
                          </v-card-text>
                        </v-col>
                      </v-row>
                    </v-card>
                  </v-container>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      v-if="y > 0"
                      color="purple lighten-1"
                      text
                      @click="y--"
                    >
                      이전
                    </v-btn>
                    <v-btn
                      v-if="y < item.reslist.length - 1"
                      color="purple lighten-1"
                      text
                      @click="
                        pushReviewData(item.reslist[y], item.meeting.id);
                        y++;
                      "
                      >다음</v-btn
                    >
                    <v-btn
                      v-else
                      color="purple lighten-1"
                      text
                      @click="
                        isfinish(k);
                        reviewfinish(item.reslist[y], item.meeting.id);
                        save();
                      "
                      >완료</v-btn
                    >
                    <v-btn color="purple lighten-1" text @click="close"
                      >취소</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-col>
          </v-row>
          <v-row class = "mx-4">
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
              </slideritem>
            </slider>
          </v-row>
        </div>
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
      dialog: false,
      reviews: [],
      defaultreview: {
        res_id: "",
        res_name: "",
        user_name: "",
        rating: 0,
        review: "",
      },
      reviewdata: {
        res_id: "",
        res_name: "",
        user_name: "",
        rating: 0,
        review: "",
      },
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
      cnt: 0,
      y: 0,
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

  computed: {
    infoZero: function () {
      var tmp0 = 0;
      var tmp1 = 0;
      for (let index = 0; index < this.promiseList.length; index++) {
        if (this.promiseList[index].isfinish == 0) {
          tmp0++;
        } else {
          tmp1++;
        }
      }
      return [tmp0, tmp1];
    },
  },

  created() {
    this.move();
    this.userData();
  },
  methods: {
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
    },
    goCourse(id) {
      this.$router.push({
        name: "courseEdit",
        params: { p_id: id },
      });
    },
    reviewfinish(storeInfos, id) {
      this.pushReviewData(storeInfos, id);
      axios
        .post(SERVER_URL + "/api/store/review2/create/", this.reviews)
        .then(() => {})
        .catch((err) => console.log(err));
    },
    isfinish(k) {
      const promiseData = this.promiseList[k];
      promiseData.isfinish = 1;
      axios
        .post(SERVER_URL + "/promise/update/" + promiseData.id, promiseData)
        .then(() => {
          this.promiseData();
        })
        .catch((err) => console.log(err));
    },
    pushReviewData(storeInfos, id) {
      this.reviewdata.res_id = storeInfos.id;
      this.reviewdata.res_name = storeInfos.name;
      this.reviewdata.user_name = id;
      this.reviews.push(this.reviewdata);
      this.reviewdata = Object.assign({}, this.defaultreview);
    }, // 리뷰 데이터를 reviews에 넣는 작업 과정 과 초기화 과정을 여기서 해주는거다.
    // res_id 와 res_name , user_id 이거 더 채워주는 작업을 해줘야할듯?? 위에 쓴거중 3-1번과 3-2번 과정임  Success
    save() {
      this.dialog = false;
      this.y = 0;
    },
    close() {
      this.dialog = false;
    },
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
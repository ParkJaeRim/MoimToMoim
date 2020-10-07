<template>
  <div>
    <v-container>
      <div>
        <v-row dense class="each-row m-0 mx-auto" align="center" justify="center">
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
          <v-col align="center" justify="center">
            <v-icon @click="goDetail">fas fa-cog</v-icon>
          </v-col>
        </v-row>
      </div>
      <div class="d-flex justify-space-between" max-width="400" height="100">
        <v-row align="center" justify="center">
          <v-col class="text-center py-0" col="6">
            <div>
              <v-btn
                text
                color="primary"
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
          <v-col class="text-center py-0" col="6">
            <div height="100">
              <v-btn
                text
                color="primary"
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
    <hr>

      <div v-for="(item, k) in promiseList" :key="item.id">
        <div v-if="item.isfinish == cnt">
          <v-row>
            <v-col cols="9" class="pr-0 pb-0">
              <p v-on:click="goCourse(item.id)" class="text-truncate" style="font-size: 15px">
                {{ item.title }} / {{ item.date.substring(2, 4) }}.{{
                  item.date.substring(5, 7)
                }}.{{ item.date.substring(8, 10) }} / {{ item.meeting.title }}
                <v-badge v-if='item.isfinish==0'
                inline
                color="deep-purple lighten-4"
                icon="mdi-lead-pencil"
              ></v-badge>
                <v-badge v-if='item.isfinish!=0'
                inline
                color="deep-purple lighten-4"
                icon="mdi-eye"
              >보기</v-badge>
              </p>
            </v-col>
            <v-col v-if="item.reslist.length==0" cols="3" class="pt-1 pl-0 yb-0">
                <template>
                  <v-btn
                    v-if="item.isfinish == 0"
                    text
                    color="orange"
                    style="font-size: 15px"
                    @click="deletePromise(item.id)"
                    >삭제</v-btn
                  >
                </template>
            </v-col>

            
            <v-col v-if="item.reslist.length!=0" cols="3" class="pt-1 pl-0 yb-0">
              <v-dialog
                v-model="dialog"
                max-width="320px"
                width="auto"
                align="center"
                justify="center"
                :retain-focus="false"
              >
                <template v-slot:activator="{ on }">
                  <v-btn
                    v-if="item.isfinish == 0"
                    text
                    color="orange"
                    style="font-size: 15px"
                    v-on="on"
                    @click="setreview(k)"
                    >완료</v-btn
                  >
                </template>

                <v-card>
                  <v-container>
                    <v-card>
                      <v-row>
                        <v-col>
                          <v-card-text class="h4">
                            
                            {{ promiseList[reviewid].reslist[y].name }}
                            
                            <v-img
                              v-if="promiseList[reviewid].reslist[y].img !== null"
                              class="white--text"
                              :src="promiseList[reviewid].reslist[y].img"
                              width="270px"
                              height="120px"
                            ></v-img>

                            <br />
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
                    <!-- <v-btn
                      v-if="y > 0"
                      color="orange"
                      text
                      @click="y--"
                    >
                      이전
                    </v-btn> -->
                    <v-btn
                      v-if="y < item.reslist.length - 1"
                      color="orange"
                      text
                      @click="
                        pushReviewData(promiseList[reviewid].reslist[y], promiseList[reviewid].meeting.id);
                        y++;
                      "
                      >다음</v-btn
                    >
                    <v-btn
                      v-else
                      color="orange"
                      text
                      @click="
                        isfinish(reviewid);
                        reviewfinish(promiseList[reviewid].reslist[y], promiseList[reviewid].meeting.id);
                        save();
                      "
                      >완료</v-btn
                    >
                    <v-btn color="orange" text @click="close"
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
                  height="120px"
                  @click="goCourse(item.id)"
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
      reviewid: 0,
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
        store_id:"",
      },
      reviewdata: {
        res_id: "",
        res_name: "",
        user_name: "",
        rating: 0,
        review: "",
        store_id:"",
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
    this.userData();
  },
  methods: {
    setreview(item){
      this.reviewid = item
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
          this.headers = res.data;
          this.promiseData();
        })
        .catch((error) => {
          console.log(error.resposne);
        });
    },
    promiseData() {
      axios
        .get(SERVER_URL + "/promise/" + this.headers.username + "/list/")
        .then((res) => {
          this.promiseList = res.data;
        })
        .catch((err) => console.log(err.resposne));
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
        .catch((err) => console.log(err.resposne));
    },

    deletePromise(id){
      axios.post(SERVER_URL+"/promise/delete/"+id).then(()=>{
        this.promiseData();
      }).catch((err)=>console.log(err.resposne));
    },

    isfinish(k) {
      const promiseData = this.promiseList[k];
      promiseData.isfinish = 1;
      axios
        .post(SERVER_URL + "/promise/update/" + promiseData.id, promiseData)
        .then(() => {
          this.promiseData();
        })
        .catch((err) => console.log(err.resposne));
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
      this.y=0;
      this.reviewid = 0;
      this.reviews =[];
      this.reviewdata = Object.assign({}, this.defaultreview);
      this.dialog = false;
      // this.$router.go();
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
<template>
  <div>
    <v-container>
      <div>
        <v-row dense class="each-row m-0 mx-auto" align="center" justify="center">
          <v-col align="center" justify="center">
            <img
              height="64"
              width="64"
              class="text-center lighten-4 rounded-circle d-inline-flex ma-3"
               src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+PGxpbmVhckdyYWRpZW50IGlkPSJhIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDEgMCAwIC0xIDAgLTEyMTQ2KSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwIiB4Mj0iNTEyIiB5MT0iLTEyNDAyIiB5Mj0iLTEyNDAyIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMzMWQ4ZmYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZjgwZmYiLz48L2xpbmVhckdyYWRpZW50PjxwYXRoIGQ9Im01MTIgMjU2YzAgMTQxLjM4NjcxOS0xMTQuNjEzMjgxIDI1Ni0yNTYgMjU2cy0yNTYtMTE0LjYxMzI4MS0yNTYtMjU2IDExNC42MTMyODEtMjU2IDI1Ni0yNTYgMjU2IDExNC42MTMyODEgMjU2IDI1NnptMCAwIiBmaWxsPSJ1cmwoI2EpIi8+PGcgZmlsbD0iI2ZmZiI+PHBhdGggZD0ibTMwMC42MzI4MTIgMjI1Ljk3NjU2MmMyMC4wOTM3NS0xNi4zNzEwOTMgMzIuOTUzMTI2LTQxLjI5Njg3NCAzMi45NTMxMjYtNjkuMTcxODc0IDAtNDkuMTgzNTk0LTQwLjAxNTYyNi04OS4xOTUzMTMtODkuMTk1MzEzLTg5LjE5NTMxMy00OS4xODM1OTQgMC04OS4xOTUzMTMgNDAuMDExNzE5LTg5LjE5NTMxMyA4OS4xOTUzMTMgMCAyNy44NzUgMTIuODU5Mzc2IDUyLjgwNDY4NyAzMi45NTMxMjYgNjkuMTcxODc0LTYyLjQ2ODc1IDIyLjk3MjY1Ny0xMDcuMTQ4NDM4IDgzLjA3NDIxOS0xMDcuMTQ4NDM4IDE1My40MTAxNTcgMCA4LjI4NTE1NiA2LjcxODc1IDE1IDE1IDE1aDI5Ni43ODEyNWM4LjI4MTI1IDAgMTUtNi43MTQ4NDQgMTUtMTUgMC03MC4zMzU5MzgtNDQuNjc5Njg4LTEzMC40Mzc1LTEwNy4xNDg0MzgtMTUzLjQxMDE1N3ptLTExNS40Mzc1LTY5LjE3MTg3NGMwLTMyLjY0MDYyNiAyNi41NTQ2ODgtNTkuMTk1MzEzIDU5LjE5NTMxMy01OS4xOTUzMTNzNTkuMTk1MzEzIDI2LjU1NDY4NyA1OS4xOTUzMTMgNTkuMTk1MzEzYzAgMzIuNjQwNjI0LTI2LjU1ODU5NCA1OS4xOTUzMTItNTkuMTk1MzEzIDU5LjE5NTMxMi0zMi42NDA2MjUgMC01OS4xOTUzMTMtMjYuNTU0Njg4LTU5LjE5NTMxMy01OS4xOTUzMTJ6bS03My4zNTU0NjggMjA3LjU4MjAzMWM3LjQ3MjY1Ni02Ni41MTk1MzEgNjQuMDY2NDA2LTExOC4zOTA2MjUgMTMyLjU1MDc4MS0xMTguMzkwNjI1czEyNS4wNzgxMjUgNTEuODcxMDk0IDEzMi41NTA3ODEgMTE4LjM5MDYyNXptMCAwIi8+PHBhdGggZD0ibTM5MC40ODQzNzUgMjMzLjI5Mjk2OWMtNy45Mzc1LTcuOTQxNDA3LTE2LjQ5MjE4Ny0xNS4yMjI2NTctMjUuNTM1MTU2LTIxLjc0NjA5NCA3Ljc4OTA2Mi0xNy4xMjUgMTEuODU1NDY5LTM1Ljc5Njg3NSAxMS44NTU0NjktNTQuNzQyMTg3IDAtOC4yODUxNTctNi43MTQ4NDQtMTUtMTUtMTUtOC4yODUxNTcgMC0xNSA2LjcxNDg0My0xNSAxNSAwIDE4LjIwMzEyNC00Ljg1NTQ2OSAzNi4wODIwMzEtMTQuMDQ2ODc2IDUxLjcyMjY1Ni00LjI1IDYuNzUtMi40NjQ4NDMgMTUuNjgzNTk0IDQuMTAxNTYzIDIwLjI4MTI1LjI1NzgxMy4xNzk2ODcuNTE5NTMxLjM1MTU2Mi43ODUxNTYuNTExNzE4IDExLjM3ODkwNyA3LjEwNTQ2OSAyMi4wMTk1MzEgMTUuNTc4MTI2IDMxLjYyODkwNyAyNS4xODc1IDMzLjM1NTQ2OCAzMy4zNTU0NjkgNTEuNzI2NTYyIDc3LjcwNzAzMiA1MS43MjY1NjIgMTI0Ljg3ODkwNyAwIDguMjg1MTU2IDYuNzE4NzUgMTUgMTUgMTUgOC4yODUxNTYgMCAxNS02LjcxNDg0NCAxNS0xNSAwLTU1LjE4MzU5NC0yMS40ODgyODEtMTA3LjA3MDMxMy02MC41MTU2MjUtMTQ2LjA5Mzc1em0wIDAiLz48L2c+PC9zdmc+" />          </v-col>
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
              ></v-badge>
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
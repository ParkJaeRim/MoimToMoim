<template>
  <div>
    <v-container>
      <div align="center" justify="center">
        <v-row dense class="each-row mx-auto">
          <v-col cols="8" md="8" sm="4" style="font-size: 20px">
            <v-badge inline color="deep-purple lighten-4" lighten-5 icon="mdi-lead-pencil" >
               <a href="#" @click.stop="ModifyDialog = true" class="h3">{{
                meetingDetail.title
              }} </a></v-badge
            >의 <br />
            약속을 준비하세요 !
          </v-col>
          <v-col col="4" md="4" sm="2">
            <v-btn
              color="deep-purple lighten-4"
              fab
              large
              dark
              @click="makePromise(meetingDetail.id)"
            >
              <v-icon large>mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </div>

      <v-row class="each-row mx-auto" align="center" justify="center">
        <slider ref="slider" :options="options">
          <slideritem
            v-for="(item, i) in dueday"
            :key="i"
            class="promise deep-purple lighten-5"
            style="font-size : 18px; border-radius: 25px;"
          >
            <v-col cols="5" @click="goPromise(promise[dueday[i].idx].id)">
              <v-responsive
                class="font-weight-bold h3 text-center d-inline-flex align-center justify-center ma-3 orange--text"
                height="80"
                width="80"
              >D-{{ dueday[i].remain }}
               
              </v-responsive>
            </v-col>
            <v-col cols="7" @click="goPromise(promise[dueday[i].idx].id)">
              <v-row> {{  promise[dueday[i].idx].title }} </v-row>
              <v-row> {{ promise[dueday[i].idx].storelist }} </v-row>
              <v-row>
                <v-icon >mdi-calendar </v-icon>
                 {{  promise[dueday[i].idx].date.substring(5, 7) }}월
                {{  promise[dueday[i].idx].date.substring(8, 10) }}일
              </v-row>
                <v-row><v-icon >mdi-pin </v-icon>  {{ promise[dueday[i].idx].gu }} {{ promise[dueday[i].idx].dong }}</v-row
              >
            </v-col>
          </slideritem>
        </slider>
      </v-row>
      <hr />
      <v-row class="h5 each-row mx-auto">취향 추천</v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item, i) in searchStoreList" :key="i" :style="styleRecom">
            <v-img
              v-if="item.img !== null"
              class="white--text"
              :src="item.img"
              width="120px"
              height="150px"
              @click="goStoreDetail(item.id)"
            >
              <div class="transbox white--text">
                <div class="store_name">{{ item.name }}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>
      </v-row>
      <hr />
      <!--                 핫플레이스 추천                           -->
      <v-row class="h5 each-row mx-auto">핫플레이스 추천</v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem
            v-for="(item, i) in hotplace"
            :key="i"
            :style="styleRecom"
          >
            <v-img
              v-if="item.img !== null"
              class="white--text"
              :src="item.img"
              width="120px"
              height="150px"
              @click="goStoreDetail(item.id)"
            >
              <div class="transbox white--text">
                <div class="store_name">{{ item.name }}</div>
              </div>
            </v-img>
            <v-img
              v-if="item.img == null"
              class="white--text one"
              src="http://asq.kr/JNlr0nxp6EQN"
              width="170px"
              height="170px"
              @click="goStoreDetail(item.id)"
            >
              <div class="transbox white--text">
                <div class="store_name">{{ item.name }}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>
      </v-row>
      <!-- Modify Dialog -->
      <v-dialog v-model="ModifyDialog" calss max-width="500px">
        <v-card>
          <v-card-title>
            <span class="h3">모임 수정</span>
          </v-card-title>

          <v-card-text>
            <v-container>
              <v-row align="center" justify="center">
                <v-col cols="5" sm="4" md="5"> 모임 이름 :</v-col>
                <v-col cols="7" sm="4" md="7">
                  <v-text-field v-model="modifyItem.title"></v-text-field>
                </v-col>
              </v-row>
              <v-row align="center" justify="center">
                <v-col cols="5" sm="4" md="5"> 대표 이미지 :</v-col>
                <v-col cols="7" sm="4" md="7">
                  <v-file-input
                    label="이곳을 눌러주세요"
                    @change="onChangeImages"
                  ></v-file-input>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="purple lighten-1" text @click="save">수정</v-btn>
            <v-btn color="purple lighten-1" text @click="close">취소</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import { slider, slideritem } from "vue-concise-slider";

import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "MeetingDetail",
  data() {
    return {
      meetingDetail: {},
      promise: {},
      hotplace: {},
      likes: {},
      options: {
        pagination: false,
        currentPage: 0,
        tracking: false,
        deviation: "200",
        slidesToScroll: 1,
        loop: false,
      },
      styleRecom: {
        width: "31.5%",
        "margin-right": "2%",
        "font-size": "13px",
      },
      ModifyDialog: false,
      modifyItem: {
        title: "",
        background_img: "",
      },
      defaultItem: {
        title: "",
        background_img: "",
      },
      dueday: [],
      searchData: {
        gu: "",
        dong: "",
        selected: "가게명",
        keyword: "",
      },
      searchStoreList: {},
      };
  },
  components: {
    slider,
    slideritem,
  },

  created() {
    this.detailData();
  },

  methods: {
    makePromise(m_id) {
      this.$router.push({
        name: "makepromise1",
        params: {
          m_id: m_id,
        },
      });
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

    goModify() {
      this.$router.push({
        name: "",
      });
    },

    detailData() {
      axios
        .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
        .then((res) => {
          this.meetingDetail = res.data;
          this.promiseData();
          this.gethotplace();
          this.searchStore();
        })
        .catch((err) => console.log(err.res));
    },


    promiseData() {
      axios
        .get(SERVER_URL + "/promise/" + this.$route.params.m_id)
        .then((res) => {
          this.promise = res.data;

          for (let i = 0; i < this.promise.length; i++) {
            var object={};
            var today = new Date();
            today.setHours(0, 0, 0, 0);
            var count = new Date(this.promise[i].date);
            count.setHours(0, 0, 0, 0);
            var dday = Math.floor((count - today) / 1000 / 24 / 60 / 60);
            if (dday == 0) {
              object.store_id= this.promise[i].id;
              object.remain = "Day";
              object.idx = i;
              this.dueday.push(object);
            } else if (dday > 0) {
              object.store_id= this.promise[i].id;
              object.remain = dday;
              object.idx = i;
              this.dueday.push(object);
            }

            var arr= this.promise[i].storelist.split("/")
            arr = arr.slice(0, arr.length-1);
            console.log(arr)
            // 여기서 이제 코스 뽑아줘야합니다....But how...?
          }
          this.dueday.sort(function (a,b){
            if(a.remain=="Day")
              return -1;
            else if(b.remain=="Day")
              return 1;
            return a.remain-b.remain;
          });

        })
        .catch((err) => console.log(err.res));
    },

    searchStore() {
      axios
        .post(
          SERVER_URL + "/api/store/storerecommend/eating/" + this.$route.params.m_id, this.searchData
        )
        .then((res) => {
          console.log(res.data)
          this.searchStoreList = res.data;
        })
        .catch((err) => console.log(err.response));
    },

    gethotplace() {
      axios
        .get(
          SERVER_URL + "/api/store/firstrecommend/" + this.$route.params.s_id
        )
        .then((res) => {
          this.hotplace = res.data;
        })
        .catch((err) => console.log(err.res));
    },

    goPromise(p_id) {
      this.$router.push({
        name: "courseEdit",
        params: {
          p_id: p_id,
        },
      });
    },

    save() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(
          SERVER_URL + "/meeting/modify/" + this.$route.params.m_id,
          this.modifyItem,
          config
        )
        .then(() => {
          this.detailData();
          this.close();
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },

    close() {
      this.ModifyDialog = false;
      this.$nextTick(() => {
        this.modifyItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    onChangeImages(e) {
      const selectedImage = e;
      this.createBase64Image(selectedImage);
    },
    createBase64Image(fileObject) {
      this.modifyItem.background_img = new Image();
      const reader = new FileReader();
      reader.onload = (e) => {
        this.modifyItem.background_img = e.target.result;
      };
      reader.readAsDataURL(fileObject);
    },

    removeImage() {
      this.modifyItem.background_img = "";
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
a {
  color: #BA68C8;
  text-decoration: underline;
}
</style>

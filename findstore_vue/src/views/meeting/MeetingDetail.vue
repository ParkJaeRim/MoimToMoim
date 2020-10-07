<template>
  <div>
    <v-container>
      <div align="center" justify="center">
        <v-row dense class="each-row mx-auto">
          <v-col cols="8" md="8" sm="4" style="font-size: 20px">
            <v-badge
              inline
              color="deep-purple lighten-4"
              lighten-5
              icon="mdi-lead-pencil"
            >
              <a href="#" @click.stop="ModifyDialog = true" class="h3"
                >{{ meetingDetail.title }}
              </a></v-badge
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

      <v-row
        v-if="dueday.length != 0"
        class="each-row mx-auto"
        align="center"
        justify="center"
      >
        <slider ref="slider" :options="options">
          <slideritem
            v-for="(item, i) in dueday"
            :key="i"
            height="200px"
            class="promise deep-purple lighten-5"
            style="font-size : 18px; border-radius: 25px; text-align:left;"
          >
            <v-col
              v-if="promise[item.idx].isfinish == 0"
              class="ml-1 mr-2"
              cols="4"
              @click="goPromise(promise[item.idx].id)"
            >
              <v-row>
                <v-responsive
                  v-if="item.remain != 'Day'"
                  class="font-weight-bold h3 text-center d-inline-flex align-center justify-center ma-3 deep-purple--text"
                  width="80"
                  >D-{{ item.remain }}
                </v-responsive>
                <v-responsive
                  v-if="item.remain == 'Day'"
                  class="font-weight-bold h3 text-center d-inline-flex align-center justify-center ma-3 dday"
                  width="80"
                  >D-{{ item.remain }}
                </v-responsive>
              </v-row>
              <v-row align="center" justify="center">
                {{ promise[item.idx].gu }}
                {{ promise[item.idx].dong }}</v-row
              >
            </v-col>

            <v-col
              v-if="promise[item.idx].isfinish == 0"
              cols="7"
              @click="goPromise(promise[item.idx].id)"
            >
              <v-row class="h4 mt-1"> {{ promise[item.idx].title }} </v-row>
              <v-row v-if="promise[item.idx].reslist.length != 0 & promise[item.idx].reslist[0].name.length > 5" class="mt-1">
                <v-icon  color="deep-purple">mdi-heart </v-icon> 모이는 곳 : {{ promise[item.idx].reslist[0].name.substring(0,5) }} ...
              </v-row>
                  <v-row v-else-if="promise[item.idx].reslist.length != 0" class="mt-1">
                <v-icon  color="deep-purple">mdi-heart </v-icon> 모이는 곳 : {{ promise[item.idx].reslist[0].name}}
              </v-row>
              <v-row class="mt-1">
                <v-icon  color="deep-purple">mdi-calendar </v-icon>
                {{ promise[item.idx].date.substring(5, 7) }}월
                {{ promise[item.idx].date.substring(8, 10) }}일
              </v-row>
            </v-col>

            <v-col v-if="promise[item.idx].isfinish == 1">
              <v-row align="center" justify="center" class="mt-1"
                ><img
                  height="50px"
                  width="50px"
                  src="data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEyIDUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnIGlkPSJYTUxJRF8xNjAzXyI+PHBhdGggaWQ9IlhNTElEXzE1ODRfIiBkPSJtMTAgMTYyaDQ5MnYzNDBoLTQ5MnoiIGZpbGw9IiNmZmYiLz48cGF0aCBpZD0iWE1MSURfMTYwMl8iIGQ9Im02NiAyMThoOTUuMTI3djc2aC05NS4xMjd6IiBmaWxsPSIjZmZjZDY5Ii8+PHBhdGggaWQ9IlhNTElEXzI1MjRfIiBkPSJtNjYgMzcwaDk1LjEyN3Y3NmgtOTUuMTI3eiIgZmlsbD0iIzdkZDljMiIvPjxwYXRoIGlkPSJYTUxJRF8yNTI1XyIgZD0ibTI1Ni4xMjcgMzcwaDk1LjEyN3Y3NmgtOTUuMTI3eiIgZmlsbD0iIzdkZDljMiIvPjxnIGZpbGw9IiNmZjdkOTciPjxwYXRoIGlkPSJYTUxJRF8yNTIxXyIgZD0ibTY2IDI5NGg5NS4xMjd2NzZoLTk1LjEyN3oiLz48cGF0aCBpZD0iWE1MSURfMjUyMl8iIGQ9Im0xNjEuMTI3IDI5NGg5NS4xMjd2NzZoLTk1LjEyN3oiLz48cGF0aCBpZD0iWE1MSURfMjUyM18iIGQ9Im0zNTEuMTI3IDI5NGg5NS4xMjd2NzZoLTk1LjEyN3oiLz48L2c+PHBhdGggaWQ9IlhNTElEXzI1MjBfIiBkPSJtMjU2LjEyNyAyMThoOTUuMTI3djc2aC05NS4xMjd6IiBmaWxsPSIjZmZjZDY5Ii8+PHBhdGggaWQ9IlhNTElEXzEwOTlfIiBkPSJtMTAgNTBoNDkydjExMmgtNDkyeiIgZmlsbD0iIzAwY2NmMiIvPjxnIGlkPSJYTUxJRF85OTFfIiBmaWxsPSIjZTJlOWVlIj48cGF0aCBpZD0iWE1MSURfMTUzNV8iIGQ9Im0zOTYgNzZ2LTQ0YzAtMTIuMTUgOS44NS0yMiAyMi0yMiAxMi4xNSAwIDIyIDkuODUgMjIgMjJ2NDRjMCAxMi4xNS05Ljg1IDIyLTIyIDIyLTEyLjE1IDAtMjItOS44NS0yMi0yMnoiLz48cGF0aCBpZD0iWE1MSURfMTUzM18iIGQ9Im0yODggNzZ2LTQ0YzAtMTIuMTUgOS44NS0yMiAyMi0yMiAxMi4xNSAwIDIyIDkuODUgMjIgMjJ2NDRjMCAxMi4xNS05Ljg1IDIyLTIyIDIyLTEyLjE1IDAtMjItOS44NS0yMi0yMnoiLz48cGF0aCBpZD0iWE1MSURfMTQ4OF8iIGQ9Im0xODAgNzZ2LTQ0YzAtMTIuMTUgOS44NS0yMiAyMi0yMiAxMi4xNSAwIDIyIDkuODUgMjIgMjJ2NDRjMCAxMi4xNS05Ljg1IDIyLTIyIDIyLTEyLjE1IDAtMjItOS44NS0yMi0yMnoiLz48cGF0aCBpZD0iWE1MSURfOTkzXyIgZD0ibTcyIDc2di00NGMwLTEyLjE1IDkuODUtMjIgMjItMjIgMTIuMTUgMCAyMiA5Ljg1IDIyIDIydjQ0YzAgMTIuMTUtOS44NSAyMi0yMiAyMi0xMi4xNSAwLTIyLTkuODUtMjItMjJ6Ii8+PC9nPjxnIGlkPSJYTUxJRF8xNjM5XyI+PHBhdGggaWQ9IlhNTElEXzE3NDFfIiBkPSJtNTAyIDQwaC01MnYtOGMwLTE3LjY0NS0xNC4zNTUtMzItMzItMzJzLTMyIDE0LjM1NS0zMiAzMnY4aC00NHYtOGMwLTE3LjY0NS0xNC4zNTUtMzItMzItMzJzLTMyIDE0LjM1NS0zMiAzMnY4aC00NHYtOGMwLTE3LjY0NS0xNC4zNTUtMzItMzItMzJzLTMyIDE0LjM1NS0zMiAzMnY4aC00NHYtOGMwLTE3LjY0NS0xNC4zNTUtMzItMzItMzJzLTMyIDE0LjM1NS0zMiAzMnY4aC01MmMtNS41MjMgMC0xMCA0LjQ3Ny0xMCAxMHY0NTJjMCA1LjUyMyA0LjQ3NyAxMCAxMCAxMGg0OTJjNS41MjMgMCAxMC00LjQ3NyAxMC0xMHYtNDUyYzAtNS41MjMtNC40NzctMTAtMTAtMTB6bS05Ni04YzAtNi42MTcgNS4zODMtMTIgMTItMTJzMTIgNS4zODMgMTIgMTJ2NDRjMCA2LjYxNy01LjM4MyAxMi0xMiAxMnMtMTItNS4zODMtMTItMTJ6bS0xMDggMGMwLTYuNjE3IDUuMzgzLTEyIDEyLTEyczEyIDUuMzgzIDEyIDEydjQ0YzAgNi42MTctNS4zODMgMTItMTIgMTJzLTEyLTUuMzgzLTEyLTEyem0tMTA4IDBjMC02LjYxNyA1LjM4My0xMiAxMi0xMnMxMiA1LjM4MyAxMiAxMnY0NGMwIDYuNjE3LTUuMzgzIDEyLTEyIDEycy0xMi01LjM4My0xMi0xMnptLTEwOCAwYzAtNi42MTcgNS4zODMtMTIgMTItMTJzMTIgNS4zODMgMTIgMTJ2NDRjMCA2LjYxNy01LjM4MyAxMi0xMiAxMnMtMTItNS4zODMtMTItMTJ6bS02MiA0NjB2LTMyMGgxOTFjNS41MjMgMCAxMC00LjQ3NyAxMC0xMHMtNC40NzctMTAtMTAtMTBoLTE5MXYtOTJoNDJ2MTZjMCAxNy42NDUgMTQuMzU1IDMyIDMyIDMyczMyLTE0LjM1NSAzMi0zMnYtMTZoNDR2MTZjMCAxNy42NDUgMTQuMzU1IDMyIDMyIDMyczMyLTE0LjM1NSAzMi0zMnYtMTZoNDR2MTZjMCAxNy42NDUgMTQuMzU1IDMyIDMyIDMyczMyLTE0LjM1NSAzMi0zMnYtMTZoNDR2MTZjMCAxNy42NDUgMTQuMzU1IDMyIDMyIDMyczMyLTE0LjM1NSAzMi0zMnYtMTZoNDJ2OTJoLTE5MWMtNS41MjMgMC0xMCA0LjQ3Ny0xMCAxMHM0LjQ3NyAxMCAxMCAxMGgxOTF2MzIweiIvPjxwYXRoIGlkPSJYTUxJRF8xOTM5XyIgZD0ibTQ0NiAyMDhoLTM4MGMtNS41MjMgMC0xMCA0LjQ3Ny0xMCAxMHYyMjhjMCA1LjUyMyA0LjQ3NyAxMCAxMCAxMGgzODBjNS41MjMgMCAxMC00LjQ3NyAxMC0xMHYtMjI4YzAtNS41MjMtNC40NzctMTAtMTAtMTB6bS0zNzAgOTZoNzUuMTI3djU2aC03NS4xMjd6bTk1LjEyNyAwaDc1djU2aC03NXptNzUtMjBoLTc1di01Nmg3NXptMjAtNTZoNzV2NTZoLTc1em0tMjAgMTUydjU2aC03NXYtNTZ6bTIwIDBoNzV2NTZoLTc1em0wLTIwdi01Nmg3NXY1NnptOTUtNTZoNzQuODczdjU2aC03NC44NzN6bTc0Ljg3My0yMGgtNzQuODczdi01Nmg3NC44NzN6bS0yODQuODczLTU2djU2aC03NS4xMjd2LTU2em0tNzUuMTI3IDE1Mmg3NS4xMjd2NTZoLTc1LjEyN3ptMjg1LjEyNyA1NnYtNTZoNzQuODczdjU2eiIvPjxwYXRoIGlkPSJYTUxJRF8xOTcwXyIgZD0ibTI1NiAxNzJjMi42MyAwIDUuMjEtMS4wNyA3LjA3LTIuOTNzMi45My00LjQ0IDIuOTMtNy4wNy0xLjA3LTUuMjEtMi45My03LjA3LTQuNDQtMi45My03LjA3LTIuOTMtNS4yMSAxLjA3LTcuMDcgMi45My0yLjkzIDQuNDQtMi45MyA3LjA3IDEuMDcgNS4yMSAyLjkzIDcuMDcgNC40NCAyLjkzIDcuMDcgMi45M3oiLz48L2c+PC9nPjwvc3ZnPg=="
              /></v-row>
            </v-col>
          </slideritem>
        </slider>
      </v-row>
      <hr />
      <!--                 핫플레이스 추천                           -->
      <v-row class="each-row mx-auto">
        <v-row class="mx-auto">
          <v-chip
            small
            class="white--text"
            color="pink"
            v-if="hotplacesite[0] > 12"
          >
            오후 {{ hotplacesite[0] - 12 }}시
          </v-chip>
          <v-chip
            small
            class="white--text"
            color="pink"
            v-else-if="(hotplacesite[0] == 12)"
          >
            낮 12시
          </v-chip>
          <v-chip small class="white--text" color="pink" v-else>
            오전 {{ hotplacesite[0] }}시
          </v-chip>
          <span class="mr-1"></span><span class=" h5">핫플레이스 추천 </span>
        </v-row>
        <span v-for="(dong, di) in hotplacesite" :key="di">
          <div v-if="(di == 1) & (dong.length <= 3)">
            {{ dong.substring(0, 2) }}
          </div>
          <div v-if="(di == 1) & (dong.length > 3)">
            /{{ dong.substring(0, 3) }}
          </div>
          <div v-if="(di >= 2) & (dong.length <= 3)">
            /{{ dong.substring(0, 2) }}
          </div>
          <div v-if="(di >= 2) & (dong.length > 3)">
            /{{ dong.substring(0, 3) }}
          </div>
        </span>
      </v-row>

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
      <hr />

      <v-row class="h5 each-row mx-auto ma-2">취향 추천

        <span v-for="(dong, di) in hotplacesite" :key="di">
          <div v-if="(di == 1) & (dong.length <= 3)">
            {{ dong.substring(0, 2) }}
          </div>
          <div v-if="(di == 1) & (dong.length > 3)">
            /{{ dong.substring(0, 3) }}
          </div>
          <div v-if="(di >= 2) & (dong.length <= 3)">
            /{{ dong.substring(0, 2) }}
          </div>
          <div v-if="(di >= 2) & (dong.length > 3)">
            /{{ dong.substring(0, 3) }}
          </div>
        </span>

      </v-row>

      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem
            v-for="(item, i) in searchStoreList"
            :key="i"
            :style="styleRecom"
          >
            <v-img
              v-if="item.img !== null"
              class="white--text"
              :src="item.img"
              width="120px"
              height="150px"
              @click="goStoreDetail(item.res_id)"
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
            <v-btn color="orange" text @click="save">수정</v-btn>
            <v-btn color="orange" text @click="close">취소</v-btn>
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
      hotplacesite: {},
      likes: {},
      meetingUser: "",
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
    this.move();
  },

  methods: {
    move() {
      if (!this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "home" });
      }
    },
    isUser() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/rest-auth/user/", config)
        .then((res) => {
          if (res.data.username != this.meetingDetail.user.username) {
            this.$router.push({
              name: "meetinglist",
            });
          }
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
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
          this.isUser();
          this.searchStore();
          this.promiseData();
          this.gethotplace();
        })
        .catch((err) => console.log(err.response));
    },

    promiseData() {
      axios
        .get(SERVER_URL + "/promise/" + this.$route.params.m_id)
        .then((res) => {
          this.promise = res.data;
          console.log(this.promise);
          this.meetingUser = res.data[0].user.username;
          for (let i = 0; i < this.promise.length; i++) {
            var object = {};
            var today = new Date();
            today.setHours(0, 0, 0, 0);
            var count = new Date(this.promise[i].date);
            count.setHours(0, 0, 0, 0);
            var dday = Math.floor((count - today) / 1000 / 24 / 60 / 60);
            if (dday == 0) {
              object.store_id = this.promise[i].id;
              object.remain = "Day";
              object.idx = i;
              this.dueday.push(object);
            } else if (dday > 0) {
              object.store_id = this.promise[i].id;
              object.remain = dday;
              object.idx = i;
              this.dueday.push(object);
            }

            var arr = this.promise[i].storelist.split("/");
            arr = arr.slice(0, arr.length - 1);
            // 여기서 이제 코스 뽑아줘야합니다....But how...?
          }
          this.dueday.sort(function(a, b) {
            if (a.remain == "Day") return -1;
            else if (b.remain == "Day") return 1;
            return a.remain - b.remain;
          });
        })
        .catch(() => {});
    },

    searchStore() {
      axios
        .post(
          SERVER_URL +
            "/api/store/storerecommend/eating/" +
            this.$route.params.m_id,
          this.searchData
        )
        .then((res) => {
          this.searchStoreList = res.data;
        })
        .catch((err) => console.log(err.response));
    },

    gethotplace() {
      // const m_id = this.$route.params.m_id
      var today = new Date().getHours();
      const placeData = {
        sex: this.meetingDetail.user.sex,
        avg_age: this.meetingDetail.avg_age,
        time: today,
        ppl: this.meetingDetail.ppl,
      };
      axios
        .post(SERVER_URL + "/api/hotplace/", placeData)
        .then((res) => {
          const tmp = res.data.length;
          console.log(tmp);
          this.hotplace = res.data.slice(0, tmp - 1);
          this.hotplacesite = res.data.slice(tmp - 1)[0];
        })
        .catch((err) => {
          console.log(err.response);
        });
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
          console.log(error.response);
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
  margin-top: 23px;
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
  color: #ba68c8;
  text-decoration: underline;
}
.slider-container {
  height: 130px;
}

.dday {
  color: #d63c0d;
}
</style>

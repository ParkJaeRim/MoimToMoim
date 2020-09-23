<template>
  <div>
    <v-container>
      <div align="center" justify="center">
        <v-row dense class="each-row mx-auto">
          <v-col cols="8" md="8" sm="4" style="font-size: 25px">
            "{{meetingDetail.title}}"의
            <br />약속을 준비하세요 !
          </v-col>
          <v-col col="4" md="4" sm="2">
            <v-btn color="deep-purple lighten-4" fab large dark @click="goMakePromise">
              <v-icon large>mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </div>
      <v-row class="each-row mx-auto" align="center" justify="center">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" class="storename" style="font-size : 15px">
            <v-col cols="5">
              <v-responsive
                class="text-center grey lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3"
                height="80"
                width="80"
              >연남동</v-responsive>
            </v-col>
            <v-col cols="7">
              <v-row>웅이와 함께 춤을</v-row>
              <v-row>20년 10월 20일 (화)</v-row>
              <v-row>코스 : 밥 -> 카페 -> PC방</v-row>
              <v-row class="font-weight-bold blue--text">D-4</v-row>
            </v-col>
          </slideritem>
        </slider>
      </v-row>
      <v-row class="each-row mx-auto">취향 추천</v-row>
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
      <!--                 핫플레이스 추천                           -->
      <v-row class="each-row mx-auto">핫플레이스 추천</v-row>
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
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import { slider, slideritem } from "vue-concise-slider";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "MeetingDetail",
  data() {
    return {
      meetingDetail: {},
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
        slidesToScroll: 2,
        loop: false,
      },
      style: {
        width: "31.5%",
        "margin-right": "2%",
        "font-size": "15px",
      },
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
    detailData() {
      axios
        .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
        .then((res) => {
          this.meetingDetail = res.data;
        })
        .catch((err) => console.log(err.res));
    },
    goMakePromise() {
      const m_id = this.$route.params.m_id;
      this.$router.push({
        name: "makepromise1",
        params: { m_id: m_id },
      });
    },
  },
};
</script>

<style scoped>
.each-row {
  vertical-align: middle;
  margin-top: 30px;
}

.storename {
  color: black;
}
</style>
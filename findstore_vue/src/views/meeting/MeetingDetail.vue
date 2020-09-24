<template>
  <div>
    <v-container>
      <div align="center" justify="center">
        <v-row dense class="each-row mx-auto" >
          <v-col cols="8"  md="8" sm="4" style ="font-size: 20px" >
          "{{meetingDetail.title}}"의 <br> 약속을 준비하세요 !
          </v-col>
          <v-col col ="4" md="4" sm = "2" >
            <v-btn color="deep-purple lighten-4" fab large dark @click="makePromise(meetingDetail.id)">
              <v-icon large >mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </div>
      <v-row class="each-row mx-auto" align="center" justify="center">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in promise" :key="i" class="promise deep-purple lighten-5" style="font-size : 18px; border-radius: 25px;">
            <v-col cols ="5">
              <v-responsive class="font-weight-bold text-center grey lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3" height="80" width="80">
                {{item.dong}}
              </v-responsive>
            </v-col>
            <v-col  cols="7">
              <v-row> {{item.title}} </v-row>
              <v-row> {{item.date.substring(2,4)}}년 {{item.date.substring(5,7)}}월 {{item.date.substring(8,10)}}일  </v-row>
              <v-row> {{item.storelist}} </v-row>
              <v-row class="font-weight-bold red--text">D-{{countday[i]}}</v-row>
             </v-col>
          </slideritem>
        </slider>      
      </v-row>
      <hr>
      <v-row class="each-row mx-auto">취향 추천</v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" :style="styleRecom" >
            <v-img v-if="item.img!==null" class="white--text" :src="item.img" width="120px" height="150px" @click="goStoreDetail(item.id)">
              <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
            <v-img v-if="item.img==null" class="white--text one" src="http://asq.kr/JNlr0nxp6EQN" width="170px" height="170px" @click="goStoreDetail(item.id)">
                  <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>
      </v-row>
      <hr>
      <!--                 핫플레이스 추천                           -->
      <v-row class="each-row mx-auto">핫플레이스 추천</v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
         <slideritem v-for="(item,i) in hotplace" :key="i" :style="styleRecom">
            <v-img v-if="item.img!==null" class="white--text" :src="item.img" width="120px" height="150px" @click="goStoreDetail(item.id)">
              <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
            <v-img v-if="item.img==null" class="white--text one" src="http://asq.kr/JNlr0nxp6EQN" width="170px" height="170px" @click="goStoreDetail(item.id)">
                  <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>      
      </v-row>
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
      promise:{},
      hotplace: {},
      countday:{},
      likes:[   
        {id: 1,name: "롸카두들내쉬빌핫치킨",img: "https://mp-seoul-image-production-s3.mangoplate.com/400192/1272653_1570588239901_12322"},
      {id: 2,name: "마띠아바자르",img: "https://mp-seoul-image-production-s3.mangoplate.com/399290/439642_1597548133594_6110"},
        {id : 3, name: "비전스트롤",img: "https://mp-seoul-image-production-s3.mangoplate.com/1105479_1596164462459216.jpg"}, 
      {id: 4,name: "오늘의 위로",img: "https://mp-seoul-image-production-s3.mangoplate.com/21015_1496393429425221.jpg"},
      {id: 5,name: "아메노히커피점",img: "https://mp-seoul-image-production-s3.mangoplate.com/added_restaurants/104601_1490349745059944.jpg"},
      {id: 6,name: "비로소커피",img: "https://mp-seoul-image-production-s3.mangoplate.com/added_restaurants/565213_1466144085926374.jpg"},
      ],
      options: {
        pagination: false,  
        currentPage: 0,
        tracking: false,
        deviation: '200',
        slidesToScroll: 1,
        loop: false
     },
      styleRecom: {
        'width': '31.5%',
        'margin-right': '2%',
        'font-size' : '13px'
      }
    }
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
        name : "makepromise1",
        params: {
          m_id: m_id,
        },
      });    
    },

    goStoreDetail(s_id){
      this.$router.push({
        name : "storedetail",
        params:{
          s_id : s_id,
        }
      });
    },
    
    detailData() {
      axios
        .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
        .then((res) => {
          this.meetingDetail = res.data;
          this.promiseData()
          this.gethotplace()
        })
        .catch((err) => console.log(err.res));
    },

    promiseData(){
      axios
      .get(SERVER_URL+"/promise/"+ this.$route.params.m_id)
      .then((res) => {
        this.promise = res.data;
        for (let i = 0; i < this.promise.length; i++) {       
          var today = new Date();
          today.setHours(0, 0, 0, 0);
          var count = new Date(this.promise[i].date);
          count.setHours(0, 0, 0, 0);
          var dday = Math.floor((count - today) / 1000 / 24 / 60 / 60);
          if (dday <= 0) {
            this.countday[i]="Day";
          } else {
            this.countday[i]=dday;
          }
        }
      })
      .catch((err) => console.log("?"+err.res));
    },

    gethotplace(){
      axios.get(SERVER_URL +"/api/store/firstrecommend/"+ this.$route.params.s_id)
      .then((res) => {
        this.hotplace = res.data;
      }).catch((err) => console.log(err.res));
    },
  },
};
</script>

<style scoped>

.each-row{
  vertical-align: middle;
  margin-top: 30px;
}

.promise{
  color: black;
}
.transbox{
    text-align:center;  
    background-color: rgba(118, 126, 154, 0.4);
    height:100%;

}

.store_name{
  font-size: 14px;
  font-weight: 400;
  padding-top : 50%;
  }

</style>
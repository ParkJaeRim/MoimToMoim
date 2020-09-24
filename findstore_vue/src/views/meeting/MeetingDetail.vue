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
      <v-row class="each-row mx-auto" >
        취향 추천
      </v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" :style="styleRecom">
            <v-img v-if="item.img!==null" class="white--text" :src="item.img" width="120px" height="150px">
              <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
            <v-img v-if="item.img==null" class="white--text one" src="http://asq.kr/JNlr0nxp6EQN" width="170px" height="170px">
                  <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>                             
      </v-row>
      <hr>
      <!--                 핫플레이스 추천                           -->
      <v-row class="each-row mx-auto">
        핫플레이스 추천
      </v-row>    
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
         <slideritem v-for="(item,i) in likes" :key="i" :style="styleRecom">
            <v-img v-if="item.img!==null" class="white--text" :src="item.img" width="120px" height="150px">
              <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
            <v-img v-if="item.img==null" class="white--text one" src="http://asq.kr/JNlr0nxp6EQN" width="170px" height="170px">
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
import { slider, slideritem } from 'vue-concise-slider'

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "MeetingDetail",
  data() {
    return {
      meetingDetail: {},
      promise:{},
      likes: [
      {name: "열혈쭈꾸미",img: "https://img.siksinhot.com/place/1488649917463166.jpg?w=307&h=300&c=Y"}, 
      {name: "스트라다로스터스",img: "http://asq.kr/XSBD406YwxIP"},
      {name: "커피식탁",img: "http://asq.kr/WRWkki34BEFy"},
      {name: "야상해",img: ""},
      {name: "아빠손칼국수",img: ""},
      {name: "그린브라우니",img: ""},
      ],
      countday:{},
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
        name : "makePromise",
        params: {
          m_id: m_id,
        },
      });    
    },

    detailData() {
      axios
        .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
        .then((res) => {
          this.meetingDetail = res.data;
          this.promiseData()
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
    }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
*{
  font-family: 'Jua', sans-serif;
}
.each-row{
  vertical-align: middle;
  margin-top : 30px;
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
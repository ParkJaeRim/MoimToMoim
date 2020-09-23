<template>
  <div>
    <v-container>
      <div align="center" justify="center">
        <v-row dense class="each-row mx-auto" >
          <v-col cols="8"  md="8" sm="4" style ="font-size: 25px" >
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
          <slideritem v-for="(item,i) in likes" :key="i" class="storename" style="font-size : 15px" >
            <v-col cols ="5">
              <v-responsive class="text-center grey lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3" height="80" width="80">
                연남동
              </v-responsive>
            </v-col>
            <v-col  cols="7">
              <v-row> 웅이와 함께 춤을 </v-row>
              <v-row> 20년 10월 20일 (화) </v-row>
              <v-row> 코스 : 밥 -> 카페 -> PC방 </v-row>
              <v-row class="font-weight-bold blue--text">D-4</v-row>
             </v-col>
          </slideritem>
        </slider>      
      </v-row>
      <v-row class="each-row mx-auto">
        취향 추천
      </v-row>
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" :style="style">
            <v-img class="white--text" :src="item.img" width="150px" height="150px">
              <div class="transbox white--text">
                <div class="store_name">{{item.name}}</div>
              </div>
            </v-img>
          </slideritem>
        </slider>                             
      </v-row>
      <!--                 핫플레이스 추천                           -->
      <v-row class="each-row mx-auto">
        핫플레이스 추천
      </v-row>    
      <v-row class="each-row mx-auto">
        <slider ref="slider" :options="options">
          <slideritem v-for="(item,i) in likes" :key="i" :style="style">
            <v-img class="white--text" :src="item.img" width="150px" height="150px">
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
      likes: [
      {name: "열혈쭈꾸미",img: "https://img.siksinhot.com/place/1488649917463166.jpg?w=307&h=300&c=Y"}, 
      {name: "스트라다로스터스",img: ""},
      {name: "커피식탁",img: ""},
      {name: "야상해",img: ""},
      {name: "아빠손칼국수",img: ""},
      {name: "그린브라우니",img: ""},
      ],

      options: {
        pagination: false,  
        currentPage: 0,
        tracking: false,
        deviation: '200',
        slidesToScroll: 1,
        loop: false
     },
      style: {
        'width': '48%',
        'margin-right': '2%',
        'font-size' : '15px'
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
          console.log(this.meetingDetail)
        })
        .catch((err) => console.log(err.res));
    },
  },
};
</script>

<style scoped>

.each-row{
  vertical-align: middle;
  margin-top : 30px;
}

.storename{
  color: black;
}
.transbox{
    text-align:center;  
    background-color: rgba(118, 126, 154, 0.4);
    height:50%;

}

.store_name{
  font-size:20px;
  font-weight: bold;
  margin-top:70%;
}

</style>
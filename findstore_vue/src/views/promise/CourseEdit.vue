<template>
  <v-container fluid style="max-width: auto;">
    <v-img height="200">
      <div id="map" style="height:200px;"></div>
    </v-img>
    <template>
      <v-timeline dense clipped>
        <v-slide-x-transition group>
          <v-timeline-item
            v-for="(n, i) in storeInfos"
            :key="i"
            :src="n"
            color="deep-purple lighten-4"
            medium
          >
            <template v-slot:icon>
              <span height="200">{{i+1}}</span>
            </template>
            <v-row justify="space-between" @click="goDetail(n.name)">
              <v-col class="image-left" cols="5">
                <v-img :src="n.img"></v-img>
              </v-col>
              <v-col cols="7">
                <v-row class="headline" v-text="n.name"></v-row>
                <v-row v-text="n.category"></v-row>
              </v-col>
            </v-row>
            <v-row v-text="n.address"></v-row>
          </v-timeline-item>
        </v-slide-x-transition>
      </v-timeline>
    </template>
    <template>
      <div class="text-right">
        <v-btn class="ma-2" tile color="brown darken-1" dark>추가</v-btn>
        <v-btn class="ma-2" tile color="deep-orange lighten-1" dark>수정</v-btn>
        <v-btn class="ma-2" tile color="yellow darken-1" dark>삭제</v-btn>
      </div>
    </template>
  </v-container>
  
  
<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "courseEdit",

  data() {
    return {
      storeInfos: [],
      area: "강남구 신사동",
      level: 7,
    };
  },

  created() {
    this.getStoreInfo();
  },

  mounted() {
    setTimeout(() => {
      window.kakao && window.kakap.maps ? this.initMap() : this.addScript();
    }, 100);
  },

  methods: {
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: this.level,
      };
      var map = new kakao.maps.Map(container, options);

      var geocoder = new kakao.maps.services.Geocoder();
      var zoomControl = new kakao.maps.ZoomControl();

      map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

      var len = this.storeInfos.length;
      console.log(this.storeInfos);
      geocoder.addressSearch(this.area, function (result, status) {
        if (status === kakao.maps.services.Status.OK) {
          var coord = new kakao.maps.LatLng(result[0].y, result[0].x);
          map.setCenter(coord);
        }
      });

      for (let index = 0; index < len; index++) {
        geocoder.addressSearch(this.storeInfos[index].address, function (
          result,
          status
        ) {
          if (status === kakao.maps.services.Status.OK) {
            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
            var marker = new kakao.maps.Marker({
              map: map,
              position: coords,
            });
          }
        });
      }
    },

    addScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=e03da05ed9076293090e181433ecc1c4&libraries=services";
      document.head.appendChild(script);
    },

    getStoreInfo() {
      this.storeInfos = [
        {
          id: 1,
          name: "롸카두들내쉬빌핫치킨",
          address: "서울시 강남구 신사동 646-8",
          category: "브런치 / 버거 / 샌드위치",
          img:
            "https://mp-seoul-image-production-s3.mangoplate.com/400192/1272653_1570588239901_12322",
        },
        {
          id: 19,
          name: "시라카와",
          address: "서울시 강남구 신사동 664-24 1F",
          category: "이자카야 / 오뎅 / 꼬치",
          img:
            "https://mp-seoul-image-production-s3.mangoplate.com/513273_1598598343472200.jpg",
        },
        // {
        //   id: 2,
        //   name: "롸카두들내쉬빌핫치킨",
        //   address: "서울시 강남구 신사동 646-8",
        //   category: "브런치 / 버거 / 샌드위치",
        //   img:
        //     "https://mp-seoul-image-production-s3.mangoplate.com/400192/1272653_1570588239901_12322",
        // },
        // {
        //   id: 3,
        //   name: "시라카와",
        //   address: "서울시 강남구 신사동 664-24 1F",
        //   category: "이자카야 / 오뎅 / 꼬치",
        //   img:
        //     "https://mp-seoul-image-production-s3.mangoplate.com/513273_1598598343472200.jpg",
        // },
        // {
        //   id: 5,
        //   name: "시라카와",
        //   address: "서울시 강남구 신사동 664-24 1F",
        //   category: "이자카야 / 오뎅 / 꼬치",
        //   img:
        //     "https://mp-seoul-image-production-s3.mangoplate.com/513273_1598598343472200.jpg",
        // },
      ];
    },

    goDetail(i) {
      alert(i + " 상세정보로이동");
    },
  },
};
</script>
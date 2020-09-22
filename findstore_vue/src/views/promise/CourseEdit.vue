<template>
  <v-img height="200">
    <div id="map" style="height:200px;"></div>
  </v-img>
</template>

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "CourseEdit",

  data() {
    return {
      storeInfos: [],
    };
  },

  created() {
    this.getStoreInfo();
  },

  mounted() {
    window.kakao && window.kakap.maps ? this.initMap() : this.addScript();
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
      // console.log(this.storeInfos.length)

      var len = this.storeInfos.length
      for (let index = 0; index < len; index++) {
        geocoder.addressSearch(this.storeInfos[index].address, function (result, status) {
          if (status === kakao.maps.services.Status.OK) {
            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
            console.log("index" + coords)
            // console.log(coords.Ga)
            // has = has + coords.Ha
            // gas = gas + coords.Ga
            var marker = new kakao.maps.Marker({
              map: map,
              position: coords,
            });
            map.setCenter(coords);
          }
        });
      }
      
      map.setZoomable(true);

    },

    addScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=e03da05ed9076293090e181433ecc1c4&libraries=services";
      document.head.appendChild(script);
    },

    getStoreInfo() {
      this.storeInfos = [
        {
          "id": 1,
          "name": "롸카두들내쉬빌핫치킨",
          "address": "서울시 강남구 신사동 646-8",
          "category": "브런치 / 버거 / 샌드위치",
          "img": "https://mp-seoul-image-production-s3.mangoplate.com/400192/1272653_1570588239901_12322"
        },
        {
          "id": 19,
          "name": "시라카와",
          "address": "서울시 강남구 신사동 664-24 1F",
          "category": "이자카야 / 오뎅 / 꼬치",
          "img": "https://mp-seoul-image-production-s3.mangoplate.com/513273_1598598343472200.jpg"
        },
      ]
    },
  },
};
</script>
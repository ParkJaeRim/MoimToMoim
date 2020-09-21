<template>
  <v-card class="mx-auto">
    <v-carousel
      :continuous="true"
      :cycle="true"
      :show-arrows="false"
      hide-delimiter-background
      delimiter-icon="mdi-minus"
      height="200"
    >
      <v-carousel-item v-for="(image, i) in menuImg" :key="i" :src="image"></v-carousel-item>
    </v-carousel>

    <v-img class="white--text align-end" height="300">
      <div id="map" style="height:300px;"></div>
    </v-img>

    <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Whitehaven Beach</div>

      <div>Whitsunday Island, Whitsunday Islands</div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="orange" text>Share</v-btn>

      <v-btn color="orange" text>Explore</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "StoreDetail",
  data() {
    return {
      storeInfo: {},
      menuImg: [],
      level: 3
    };
  },
  created() {
    this.GetStoreInfo();
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript()
  },
  methods: {
    initMap() {
      var container = document.getElementById('map');
      var options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: this.level
      };
      var map = new kakao.maps.Map(container, options);
      
      var geocoder = new kakao.maps.services.Geocoder();

      var zoomControl = new kakao.maps.ZoomControl();
      map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

      geocoder.addressSearch(this.storeInfo.address, function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
          var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
          var marker = new kakao.maps.Marker({
            map: map,
            position: coords
          });
          map.setCenter(coords);
          map.setZoomable(false);
        } 
      });
    },
    addScript() {
      const script = document.createElement('script');
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=11745535a0ef52fd1ba5edbbea7765a9&libraries=services';
      document.head.appendChild(script);
    },

    GetStoreInfo() {
      axios
        .get(SERVER_URL + "/api/store/3")
        .then((res) => {
          this.storeInfo = res.data;
          // console.log(this.storeInfo);
          var images = res.data.img.split('|')
          for (let i = 0; i < images.length; i++) {
            this.menuImg.push(images[i])
            this.menuImg.push("https://mp-seoul-image-production-s3.mangoplate.com/400192/1272653_1570588239901_12322")
          }
        })
        .catch((err) => console.error(err.response));
    },
  },
};
</script>
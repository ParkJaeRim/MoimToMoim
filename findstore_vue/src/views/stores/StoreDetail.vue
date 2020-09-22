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
    <v-card-text class="text--primary">
      <span class="display-1">{{storeInfo.name}}</span>
      <v-chip class="ma-2" color="success" outlined small>
        {{storeInfo.rating}}
      </v-chip>
      <div>tel: {{storeInfo.tel}}</div>
    </v-card-text>
    <v-img class="white--text align-end" height="200">
      <div id="map" style="height:200px;"></div>
    </v-img>

    <v-card-text class="text--primary">
      <v-simple-table class="text-left">
        <thead>
          <tr>
            <th>메인메뉴</th>
            <th>{{storeInfo.main_mn}}</th>
          </tr>
        </thead>
        <thead>
          <tr>
            <th>가격대</th>
            <th>{{storeInfo.price}}</th>
          </tr>
        </thead>
        <thead>
          <tr>
            <th>메뉴</th>
            <th>
              <div v-for="(menu, i) in menus" :key="i">
                <!-- <p>{{i}}, {{menu}}</p> -->
                <div v-if="cnt_menu > i">{{menu}}</div>
              </div>
              <div class="text-right">
                <v-btn text small v-if="menu_full" color="primary" @click="cnt_menu = 100; menu_full=false">전체메뉴</v-btn>
                <v-btn text small v-if="!menu_full" color="primary" @click="cnt_menu = 3; menu_full=true">접기</v-btn>
              </div>
            </th>
          </tr>
        </thead>
      </v-simple-table>
    </v-card-text>

    <!-- <div v-for="(review, j) in reviews" :key="review.id">
      {{review}}
    </div> -->

    <!-- <v-card-actions>
      <v-btn color="orange" text>Share</v-btn>

      <v-btn color="orange" text>Explore</v-btn>
    </v-card-actions> -->
  </v-card>
</template>

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>

import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "StoreDetail",
  data() {
    return {
      storeInfo: {},
      menuImg: {},
      menus: {},
      reviews: {},
      level: 3,
      cnt_menu: 3,
      menu_full: true,
      cnt_review: 2,
    };
  },
  created() {
    this.GetStoreInfo();
    // this.GetReviews()
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
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
      geocoder.addressSearch(this.storeInfo.address, function (result, status) {
        if (status === kakao.maps.services.Status.OK) {
          var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
          var marker = new kakao.maps.Marker({
            map: map,
            position: coords,
          });
          map.setCenter(coords);
          map.setZoomable(false);
        }
      });
    },
    
    addScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=e03da05ed9076293090e181433ecc1c4&libraries=services";
      document.head.appendChild(script);
    },

    GetStoreInfo() {
      axios
        .get(SERVER_URL + "/api/store/5")
        .then((res) => {
          this.storeInfo = res.data;
          this.storeInfo.price = Number(res.data.price)
          this.menus = res.data.menu.split("//");
          // console.log(this.storeInfo);
          this.menuImg = res.data.img.split("|");
        })
        .catch((err) => console.error(err.response));
    },

    // GetReviews() {
    //   axios.get(SERVER_URL + "/api/store/reviews/5")
    //   .then((res) => {
    //     this.reviews = res.data
    //   })
    //   .catch((err) => console.log(err))
    // }
  },
};
</script>
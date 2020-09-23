<template>
  <v-card>
    <v-card-text class="text--primary">
      <span class="display-1">{{promiseList.title}}</span>
      <v-chip class="ma-2" color="success" outlined small>D-{{finalCheck}}</v-chip>
      <div>{{promiseList.date}}</div>
      <div>{{promiseList.gu}} {{promiseList.dong}}</div>
    </v-card-text>
    <v-row class="m-0">
      <v-col class="p-0" cols="6">
        <v-btn block color="blue-grey" dark>먹거리</v-btn>
      </v-col>
      <v-col class="p-0" cols="6">
        <v-btn block color="blue-grey" dark>놀거리</v-btn>
      </v-col>
    </v-row>
    <v-img class="white--text align-end" height="200">
      <div id="map" style="height:200px;"></div>
    </v-img>

    <v-row class="m-0">
      <v-col cols="4">
        <v-select :items="items" label="분류" dense outlined></v-select>
      </v-col>
      <v-col class="p-0" cols="6">
        <v-text-field placeholder="Placeholder"></v-text-field>
      </v-col>
      <v-col class="pt-5" cols="2">
        <v-icon>fas fa-search</v-icon>
      </v-col>
    </v-row>

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

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "makepromise2",
  data() {
    return {
      promiseList: {},
      address: "",
      items: ["카테고리", "가게명"],
    };
  },
  created() {
    this.GetPromise();
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },
  computed: {
    finalCheck() {
      var stday = this.promiseList.date;
      var today = new Date();
      var count = new Date(stday);
      var dday = Math.floor((count - today) / 1000 / 24 / 60 / 60);
      return dday;
    },
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
      geocoder.addressSearch(this.address, function (result, status) {
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
    GetPromise() {
      const p_id = this.$route.params.p_id;
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          this.promiseList = res.data;
          this.address = res.data.gu + " " + res.data.dong;
          console.log(this.promiseList);
        })
        .catch((err) => console.log(err.response));
    },
  },
};
</script>

<style>
</style>
<template>
  <v-card>
    <FooterList />
    <v-card-text class="text--primary text-left">
      <span class="h2">{{promiseList.title}}</span>
      <v-chip class="ma-2" color="success" outlined small>D-{{finalCheck}}</v-chip>
      <div>{{promiseList.date}}</div>
      <div>{{promiseList.gu}} {{promiseList.dong}}</div>
    </v-card-text>
    <v-row class="m-0">
      <v-col class="p-0" cols="6">
        <v-btn block color="deep-purple lighten-3" dark @click="choice = 'eating'; searchStore()">먹거리</v-btn>
      </v-col>
      <v-col class="p-0" cols="6">
        <v-btn block color="deep-purple lighten-3" dark @click="choice = 'playing'; searchStore()">놀거리</v-btn>
      </v-col>
    </v-row>
    <v-img class="white--text align-end" height="200">
      <div id="map" style="height:200px;"></div>
    </v-img>

    <v-row class="m-0">
      <v-col class="pb-0" cols="4">
        <v-select v-model="searchData.selected" :items="items" label="분류" dense outlined></v-select>
      </v-col>
      <v-col class="p-0" cols="6">
        <v-text-field v-model="searchData.keyword" placeholder="Placeholder"></v-text-field>
      </v-col>
      <v-col class="pt-5 pb-0" cols="2">
        <v-icon @click="searchStore">fas fa-search</v-icon>
      </v-col>
    </v-row>
    <v-card class="mb-3" v-for="(store, si) in searchStoreList" :key="store.id" color="grey lighten-2">
      <div v-if="si > -1">
        <v-btn @click="courseAdd(store.id)" small class="add" color="warning" dark>add</v-btn>
        <v-list-item @click="marker(store.address)">
          <v-img :src="store.img" class="mr-3" style="height:80px; max-width:80px"></v-img>
          <v-list-item-content>
            <v-list-item-title class="h4 mb-1">{{store.name}} <small>{{store.rating}}</small></v-list-item-title>
            <div>{{store.category}}</div>
            <v-list-item-subtitle>{{store.address}}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-icon @click="goStoreDetail(store.id)" class="float-right m-2" style="bottom:40px">fas fa-arrow-right</v-icon>
      </div>
    </v-card>
  </v-card>
</template>

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";
import FooterList from "../../components/FooterList"

const SERVER_URL = constants.ServerUrl;

export default {
  name: "makepromise2",
  components: {
    FooterList
  },
  data() {
    return {
      promiseList: {},
      address: "",
      items: ["가게명", "카테고리"],
      choice: "eating",
      searchData: {
        gu: "",
        dong: "",
        selected: "가게명",
        keyword: "",
      },
      searchStoreList: {},
    };
  },
  created() {
    this.getPromise();
  },
  mounted() {
    setTimeout(() => {
      window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
      this.searchStore();
    }, 200);
  },
  computed: {
    finalCheck() {
      var stday = this.promiseList.date;
      var today = new Date();
      today.setHours(0, 0, 0, 0);
      var count = new Date(stday);
      count.setHours(0, 0, 0, 0);
      var dday = Math.floor((count - today) / 1000 / 24 / 60 / 60);
      return dday;
    },
  },
  methods: {
    isUser() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/rest-auth/user/", config)
        .then((res) => {
          if (this.promiseList.user.username != res.data.username) {
            this.$router.push({
              name: "meetinglist"
            })
            alert("잘못된 접근입니다.")
          }
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
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
    getPromise() {
      const p_id = this.$route.params.p_id;
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          this.promiseList = res.data;
          this.isUser();
          this.address = res.data.gu + " " + res.data.dong;
        })
        .catch((err) => {
          if (err.response.status != 200) {
            this.$router.push({
              name: "meetinglist"
            })
            alert("잘못된 접근입니다.")
          }
        });
    },
    searchStore() {
      this.searchData.gu = this.promiseList.gu;
      this.searchData.dong = this.promiseList.dong;
      const m_id = this.promiseList.meeting.id
      axios
        .post(
          SERVER_URL + "/api/store/storerecommend/" + this.choice + "/" + m_id,
          this.searchData
        )
        .then((res) => {
          this.searchStoreList = res.data;
        })
        .catch((err) => console.log(err.response));
    },
    marker(ad) {
      this.address = ad
      this.initMap()
    },
    goStoreDetail(s_id) {
      this.$router.push({
        name: "storedetail",
        params: { p_id: this.$route.params.p_id, s_id: s_id }
      })
    },
    courseAdd(storeId) {
      this.promiseList.storelist += storeId + "/"
      const p_id = this.$route.params.p_id
      axios.post(SERVER_URL + "/promise/update/" + p_id, this.promiseList)
      .then(() => {})
      .catch(err => console.log(err.response))
    }
  },
};
</script>

<style scoped>
.add {
  position: absolute;
  z-index: 1;
  right: 0;
}
</style>
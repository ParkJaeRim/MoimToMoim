<template>
  <div>
    <v-card>
    <v-card-text class="text--primary">
      <span class="display-1">{{promiseList.title}}</span>
      <v-chip class="ma-1" color="success" outlined small>D-{{finalCheck}}</v-chip>
      <div>{{promiseList.date}}</div>
      <div>{{promiseList.gu}} {{promiseList.dong}}</div>
    </v-card-text>
      <v-img height="200">
        <div id="map" style="height: 200px"></div>
      </v-img>
    </v-card>

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
                <span height="200">{{ i + 1 }}</span>
              </template>
              <v-row justify="space-between" @click="goDetail(n.id)">
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
        <v-btn class="ma-2" tile color="brown darken-1" dark @click="courseAdd()">추가</v-btn>

        <v-dialog v-model="dialog" calss>
          <template v-slot:activator="{ on }">
            <v-btn
              class="ma-2"
              tile
              color="deep-orange lighten-1"
              dark
              v-on="on"
              >수정</v-btn
            >
          </template>

          <v-card>
            <v-card-title>
              <span class="headline">코스 순서 변경</span>
            </v-card-title>

            <v-container>
              <transition-group name="list" tag="div">
                <v-card
                  v-for="(item, index) in temp"
                  :key="item.id"
                  outlined
                  class="mt-3"
                >
                  <v-row>
                    <v-col>
                      <v-card-text>
                        {{ item.name }}
                        <slot :item="item" :index="index" />
                      </v-card-text>
                    </v-col>
                    <v-col class="right">
                      <v-btn
                        :disabled="index + 1 >= temp.length"
                        @click="down(index)"
                        icon
                      >
                        <v-icon> mdi-arrow-down </v-icon>
                      </v-btn>
                      <v-btn :disabled="index === 0" @click="up(index)" icon>
                        <v-icon> mdi-arrow-up </v-icon>
                      </v-btn>
                      <v-btn @click="remove(index)" icon>
                        <v-icon> mdi-close </v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-card>
              </transition-group>
            </v-container>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="purple lighten-1" text @click="save"
                >수정완료</v-btn
              >
              <v-btn color="purple lighten-1" text @click="close">취소</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-btn class="ma-2" tile color="yellow darken-1" dark @click="finishCourse()">완료</v-btn>
      </div>
    </template>
  </div>
</template>  

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "courseEdit",

  data() {
    return {
      promiseList: [],
      storeInfos: [],
      course: "",
      temp: [],
      area: "",
      level: 7,
      dialog: false,
      counter: 10,
    };
  },

  created() {
    this.getCourseOrder();
  },

  mounted() {
    setTimeout(() => {
      window.kakao && window.kakap.maps ? this.initMap() : this.addScript();
    }, 500);
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
  
  watch: {
    // 질문이 변경될 때 마다 이 기능이 실행됩니다.
    storeInfos: function () {
      this.course = "";
      for (let index = 0; index < this.storeInfos.length; index++) {
        const element = this.storeInfos[index];
        this.course += element.id + "/";
      }
    }
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

    getCourseOrder() {
      const p_id = this.$route.params.p_id;
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          this.promiseList = res.data;
          this.storeInfos = res.data.reslist;  
          this.temp = this.storeInfos.slice();
          this.area = res.data.gu + " " + res.data.dong;
        })
        .catch((err) => console.log(err.response));
    },

    courseAdd() {
      const p_id = this.$route.params.p_id;
      const newpromiseList = this.promiseList;
      newpromiseList.storelist = this.course;
      axios
        .post(SERVER_URL + "/promise/update/" + p_id, newpromiseList)
        .then(() => {})
        .catch((err) => console.log(err.response)
      );

      this.$router.push({
        name: "makepromise2",
        params: { p_id: this.$route.params.p_id },
      });
    },

    finishCourse() {
      const p_id = this.$route.params.p_id;
      const newpromiseList = this.promiseList;
      newpromiseList.storelist = this.course;
      axios
        .post(SERVER_URL + "/promise/update/" + p_id, newpromiseList)
        .then(() => {})
        .catch((err) => console.log(err.response)
      );
      alert("완료 페이지가 없슴");
    },

    goDetail(s_id) {
      this.$router.push({
        name: "storedetail",
        params: { p_id: this.$route.params.p_id, s_id: s_id }
      })
    },

    remove(index) {
      this.temp.splice(index, 1);
    },

    up(index) {
      var newValue = [];
      newValue = this.temp.slice();
      newValue[index] = this.temp[index - 1];
      newValue[index - 1] = this.temp[index];
      this.temp = newValue.slice();
    },

    down(index) {
      var newValue = [];
      newValue = this.temp.slice();
      newValue[index] = this.temp[index + 1];
      newValue[index + 1] = this.temp[index];
      this.temp = newValue.slice();
    },

    save() {
      this.storeInfos = this.temp.slice();
      this.initMap();
      this.dialog = false;
    },

    close() {
      this.dialog = false;
    },
  },
};
</script>

<style scoped>
.list-enter,
.list-leave-to {
  opacity: 0;
}

.list-enter-active,
.list-leave-active {
  transition: opacity 0.5s ease;
}

.list-move {
  transition: transform 0.5s ease-out;
}
</style>
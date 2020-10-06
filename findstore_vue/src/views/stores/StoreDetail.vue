<template>
  <v-card class="mx-auto">
    <FooterList v-if="pidCheck" />
    <v-carousel
      :continuous="true"
      :cycle="true"
      :show-arrows="false"
      hide-delimiter-background
      delimiter-icon="mdi-minus"
      height="200"
    >
      <v-carousel-item
        v-for="(image, i) in menuImg"
        :key="i"
        :src="image"
      ></v-carousel-item>
    </v-carousel>
    <v-card-text class="text--primary text-left">
      <v-btn
        @click="courseAdd(storeInfo.id)"
        small
        v-if="pidCheck"
        class="add"
        color="warning"
        dark
        >add</v-btn
      >
      <span class="display">{{ storeInfo.name }}</span>
      <v-chip class="ma-2" color="success" outlined small>{{
        Math.round( storeInfo.rating * 1e2 )/100
      }}</v-chip>
      <div>tel: {{ storeInfo.tel }}</div>
    </v-card-text>
    <v-img class="white--text align-end" height="200">
      <div id="map" style="height: 200px"></div>
    </v-img>

    <v-card-text class="text--primary">
      <v-simple-table class="text-left">
        <thead>
          <tr>
            <th width="25%">메인메뉴</th>
            <th>{{ storeInfo.main_mn }}</th>
          </tr>
        </thead>
        <thead>
          <tr>
            <th width="25%">가격대</th>
            <th>{{ storeInfo.price }}</th>
          </tr>
        </thead>
        <thead>
          <tr>
            <th width="25%">메뉴</th>
            <th>
              <br />
              <div v-for="(menu, i) in menus" :key="i">
                <div v-if="cnt_menu > i">{{ menu }}</div>
              </div>
              <div class="text-right">
                <v-btn
                  text
                  small
                  v-if="menu_full"
                  color="orange"
                  @click="
                    cnt_menu = 100;
                    menu_full = false;
                  "
                  >전체메뉴</v-btn
                >
                <v-btn
                  text
                  small
                  v-if="!menu_full"
                  color="orange"
                  @click="
                    cnt_menu = 3;
                    menu_full = true;
                  "
                  >접기</v-btn
                >
              </div>
            </th>
          </tr>
        </thead>
      </v-simple-table>
    </v-card-text>
  </v-card>
</template>

<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<script>
import axios from "axios";
import constants from "../../lib/constants";
import FooterList from "../../components/FooterList";
import swal from "sweetalert2";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "StoreDetail",
  components: {
    FooterList,
  },
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
      currentUser: " ",
    };
  },
  computed: {
    pidCheck() {
      if (this.$route.params.p_id == 0) {
        return false;
      } else {
        return true;
      }
    },
  },
  created() {
    this.isUser();
    this.GetStoreInfo();
  },
  mounted() {
    setTimeout(() => {
      window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
    }, 500);
  },
  methods: {
    isUser() {
      if (!this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "home" });
      } else {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get("auth-token")}`,
          },
        };
        axios
          .get(SERVER_URL + "/rest-auth/user/", config)
          .then((res) => {
            this.currentUser = res.data.username;
          })
          .catch((error) => {
            console.log(error.response.data);
          });
        const p_id = this.$route.params.p_id;
        axios
          .get(SERVER_URL + "/promise/detail/" + p_id)
          .then((res) => {
            const promiseList = res.data;
            if (promiseList.user.username != this.currentUser) {
              this.$router.push({
                name: "meetinglist",
              });
            }
            promiseList.storelist += storeId + "/";
            const p_id = this.$route.params.p_id;
            axios
              .post(SERVER_URL + "/promise/update/" + p_id, promiseList)
              .then(() => {})
              .catch((err) => console.log(err.response));
          })
          .catch((err) => console.log(err.response));
      }
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
      const store_id = this.$route.params.s_id;
      axios
        .get(SERVER_URL + "/api/store/" + store_id)
        .then((res) => {
          this.storeInfo = res.data;
          this.storeInfo.price = Number(res.data.price);
          this.menus = res.data.menu.split("//");
          this.menuImg = res.data.img.split("|");
        })
        .catch((err) => console.error(err.response));
    },
    courseAdd(storeId) {
      const p_id = this.$route.params.p_id;
            swal
        .fire({
          title: "코스가 추가되었습니다",
          text: "코스 버튼을 눌러 확인하세요",
          icon: "success",
          showConfirmButton: false,
          timer: 1000,
        })
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          const promiseList = res.data;
          if (promiseList.user.username != this.currentUser) {
            this.$router.push({
              name: "meetinglist",
            });
          }
          promiseList.storelist += storeId + "/";
          const p_id = this.$route.params.p_id;
          axios
            .post(SERVER_URL + "/promise/update/" + p_id, promiseList)
            .then(() => {})
            .catch((err) => console.log(err.response));
            
        })
        .catch((err) => console.log(err.response));
    },
  },
};
</script>

<style scoped>
.add {
  position: absolute;
  z-index: 1;
  right: 5px;
}

.display {
  font-family: "Jua", sans-serif;
  font-size: 25px;
}
</style>
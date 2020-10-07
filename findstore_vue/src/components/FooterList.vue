<template>
  <div class="point">
    <v-btn
      @click="
        sheet = !sheet;
        getList();
      "
      size="36"
      fab
      color="deep-purple lighten-3"
    >
      <v-icon>fas fa-route</v-icon>
    </v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="size">
        <v-row>
          <v-col cols="10">
            <slider ref="slider" :options="options">
              <slideritem
                v-for="(item, i) in course"
                :key="i"
                :style="styleRecom"
              >
                <v-img
                  v-if="item.img != ''"
                  class="white--text"
                  :src="item.img"
                  style="height: 80px; max-width: 80px"
                >
                  <div class="transbox white--text">
                    <div class="store_name">{{ item.name }}</div>
                  </div>
                </v-img>
                <v-img
                  v-else
                  class="one"
                  src="@/assets/img/defualt.png"
                  style="height: 80px; max-width: 80px"
                >
                  <div class="transbox">
                    <div class="store_name">{{ item.name }}</div>
                  </div>
                </v-img>
                <v-icon class="m-2">fas fa-arrow-right</v-icon>
              </slideritem>
            </slider>
          </v-col>
          <v-col cols="2">
            <v-icon @click="goCourse">fas fa-cogs</v-icon>
          </v-col>
        </v-row>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import axios from "axios";
import constants from "../lib/constants";
import { slider, slideritem } from "vue-concise-slider";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "footerlist",
  data() {
    return {
      sheet: false,
      course: {},
      options: {
        pagination: false,
        currentPage: 0,
        tracking: false,
        deviation: "200",
        slidesToScroll: 1,
        loop: false,
      },
      styleRecom: {
        width: "38%",
        "font-size": "15px",
      },
    };
  },
  components: {
    slider,
    slideritem,
  },
  methods: {
    getList() {
      const p_id = this.$route.params.p_id;
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          this.course = res.data.reslist;
        })
        .catch((err) => console.log(err.response));
    },
    goCourse() {
      this.$router.push({
        name: "courseEdit",
        params: { p_id: this.$route.params.p_id },
      });
    }
  },
};
</script>

<style scope>
.point {
  position: fixed;
  margin:10px;
  margin-left: 320px;
  z-index: 10;
}
.size {
  height: 100px;
}
</style>
<template>
  <div class="point">
    <v-btn @click="sheet = !sheet; getList()" size="36" fab color="deep-purple lighten-4">
      <v-icon>fas fa-route</v-icon>
    </v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="text-center" height="100px">
        
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import axios from "axios";
import constants from "../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "footerlist",
  data() {
    return {
      sheet: false,
    };
  },
  methods: {
    getList() {
      const p_id = this.$route.params.p_id;
      axios
        .get(SERVER_URL + "/promise/detail/" + p_id)
        .then((res) => {
          console.log(res.data);
          // this.promiseList = res.data;
          // this.address = res.data.gu + " " + res.data.dong;
        })
        .catch((err) => console.log(err.response));
    },
  },
};
</script>

<style scope>
.point {
  position: fixed;
  z-index: 1;
  right: 10px;
  top: 10px;
}
</style>
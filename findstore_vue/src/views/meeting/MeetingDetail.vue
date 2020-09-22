<template>
  <div>
    <v-container>
      <v-row dense class="each-row">
        <v-col cols="8"  md="8" sm="4">
        "{{meetingDetail.title}}"의 <br> 약속을 준비하세요 !
        </v-col>
        <v-col col ="4" md="4" sm = "2" >
          <v-btn class="ma-2" outlined large fab color="purple">
            <v-icon large >mdi-plus</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
      </v-row>
    </v-container>
   
  </div>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "MeetingDetail",
  data() {
    return {
      meetingDetail: {},
    };
  },

  computed: {
  },

  watch: {

  },
  created() {
    this.detailData();
  },
  methods: {
   detailData() {
      axios
        .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
        .then((res) => {
          this.meetingDetail = res.data;
        })
        .catch((err) => console.log(err.res));
    },
  },
};
</script>

<style scoped>
.each-row{
  margin-top : 30px;
}
</style>
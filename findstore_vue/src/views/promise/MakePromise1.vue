<template>
  <v-container>
    <v-row justify="center">
      <v-date-picker v-model="picker"></v-date-picker>
    </v-row>
    <v-text-field
      class="mx-10"
      v-model="promiseData.title"
      :counter="20"
      label="약속 이름을 입력해주세요."
      required
    ></v-text-field>
    <div class="text-center">
      <v-btn
        v-for="(gu, i) in guList"
        :key="i"
        class="mx-1"
        rounded
        @click="promiseData.gu = gu; gu_cnt = i; promiseData.dong=''"
      >{{gu}}</v-btn>
    </div>
    <div class="text-center">
      <hr />
      <v-btn
        v-for="(dong, i) in dongList[gu_cnt]"
        :key="i"
        class="m-1"
        rounded
        @click="promiseData.dong = dong"
      >{{dong}}</v-btn>
    </div>
    <hr />
    <div v-if="promiseData.dong && promiseData.title" class="d-flex justify-end">
      <v-btn color="blue-grey" class="white--text" small @click="makePromise">
        다음
      </v-btn>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "MakePromise1",
  data() {
    return {
      guList: ["마포구", "용산구", "성동구", "강남구"],
      dongList: [
        [
          "공덕동",
          "아현동",
          "도화동",
          "용강동",
          "대흥동",
          "염리동",
          "신수동",
          "서강동",
          "서교동",
          "합정동",
          "망원제1동",
          "망원제2동",
          "연남동",
          "성산재1동",
          "성산제2동",
          "상암동",
        ],
        [
          "남영동",
          "보광동",
          "서빙고동",
          "용문동",
          "용산2가동",
          "원효로제1동",
          "원효로제2동",
          "이촌제1동",
          "이촌제2동",
          "이태원제1동",
          "이태원제2동",
          "청파동",
          "한강로동",
          "한남동",
          "효창동",
          "후암동",
        ],
        [
          "금호1가동",
          "금호2.3가동",
          "금호4가동",
          "마장동",
          "사근동",
          "성수1가제1동",
          "성수1가제2동",
          "성수2가제1동",
          "성수2가제3동",
          "송정동",
          "옥수동",
          "왕십리도선동",
          "왕십리제2동",
          "용답동",
          "응봉동",
          "행당제1동",
          "행당제2동",
        ],
        [
          "개포1동",
          "개포2동",
          "개포4동",
          "논현1동",
          "논현2동",
          "대치1동",
          "대치2동",
          "대치4동",
          "도곡1동",
          "도곡2동",
          "삼성1동",
          "삼성2동",
          "세곡동",
          "수서동",
          "신사동",
          "압구정동",
          "역삼1동",
          "역삼2동",
          "일원1동",
          "일원2동",
          "일원본동",
          "청담동",
        ],
        [],
      ],
      gu_cnt: 4,
      promiseData: {
        title: "",
        date: "",
        gu: "",
        dong: "",
      },
      picker: new Date().toISOString().substr(0, 10),
    };
  },
  methods: {
    makePromise() {
      this.promiseData.date = this.picker;
      console.log(this.promiseData);
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(SERVER_URL + "/promise/1/create/", this.promiseData, config)
        .then(() => {
          this.$router.push({ name: 'makepromise2' })
        })
        .catch((err) => console.log(err.response));
    },
  },
};
</script>

<style>
</style>
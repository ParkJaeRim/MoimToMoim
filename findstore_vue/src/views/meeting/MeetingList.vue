<template>
  <div>
    <v-container>
      <v-row dense class="mx-auto">
        <v-col v-for="(meeting, i) in meetings" :key="i" cols="12">
          <v-card
            class="mx-auto"
            max-width="400"
            @click="meetingDetail(meeting.id)"
          >
            <v-img
              :src="meeting.background_img"
              class="white--text align-center text-center"
              height="200px"
            >
              <div class="transbox">
                <v-card-text>
                  <div class="meeting_title">{{ meeting.title }}</div>
                </v-card-text>
              </div>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-speed-dial
      v-model="fab"
      :top="top"
      :bottom="bottom"
      :right="right"
      :left="left"
      :direction="direction"
      :open-on-hover="hover"
      :transition="transition"
    >
      <template v-slot:activator>
        <v-btn v-model="fab" color="pink" dark large fab>
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-btn fab dark color="purple" @click.stop="dialog = true">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn fab dark color="red" @click.stop="deleteMeeting = true">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
    </v-speed-dial>

    <!-- DIALOG1 -->

    <v-dialog v-model="dialog" calss max-width="500px">
      <v-card>
        <v-card-title>
          <span class="h3">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-text-field
                  v-model="editedItem.title"
                  label="모임 이름"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-btn-toggle
                  v-model="editedItem.avg_age"
                  tile
                  color="purple lighten-1"
                  group
                >
                  <v-btn value="10">
                    10대
                  </v-btn>
                  <v-btn value="20">
                    20대
                  </v-btn>
                  <v-btn value="30">
                    30대
                  </v-btn>
                  <v-btn value="40">
                    40대
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-btn-toggle
                  v-model="editedItem.ppl"
                  tile
                  color="purple lighten-1"
                  group
                >
                  <v-btn value="2">
                    연인
                  </v-btn>
                  <v-btn value="3">
                    친구
                  </v-btn>
                  <v-btn value="4">
                    가족
                  </v-btn>
                  <v-btn value="5">
                    단체
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-file-input
                  label="Background_img"
                  @change="onChangeImages"
                ></v-file-input>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="purple lighten-1" text @click="save">생성</v-btn>
          <v-btn color="purple lighten-1" text @click="close">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- deleteItem DIALOG -->

    <v-dialog v-model="deleteMeeting" calss max-width="500px">
      <v-card>
        <v-card-title>
          <span class="h3">모임 삭제</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row class="mx-auto" v-for="(meeting, i) in meetings" :key="i">
              <input
                class="mr-3"
                type="checkbox"
                v-model="selected"
                :value="`${meeting.id}`"
                color="purple"
                name="rb"
              />
              <label class="radiolabel h5" :for="`${meeting.title}`">{{
                meeting.title
              }}</label>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="purple lighten-1" text @click="deleteItem">삭제</v-btn>
          <v-btn color="purple lighten-1" text @click="deleteMeeting = false">취소</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";

import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "MeetingList",
  data() {
    return {
      user:[],
      meetings: [],
      dialog: false,
      deleteMeeting: false,
      headers: [
        { text: "Title", value: "title" },
        { text: "연령대", value: "avg_age" },
        { text: "인원수", value: "ppl" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        title: "",
        avg_age: "",
        ppl: "",
        background_img: "",
      },
      defaultItem: {
        title: "",
        avg_age: "",
        ppl: "",
        background_img: "",
      },
      direction: "top",
      fab: false,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: true,
      bottom: true,
      left: false,
      transition: "slide-y-reverse-transition",
      chckbox: [],
      selected: [],
    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "모임 생성" : "모임 삭제";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  created() {
    this.move();
    this.GetMeeting();
  },
  methods: {
    move() {
      if (!this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "home" });
      }
    },
    GetMeeting() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/meeting/",config)
        .then((res) => {
          this.meetings = res.data;
          console.log(res.data)
        })
        .catch((err) => console.error(err.response));
    },

    editItem(item) {
      this.editedIndex = this.meetings.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },


    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    onChangeImages(e) {
      const selectedImage = e;
      this.createBase64Image(selectedImage);
    },
    createBase64Image(fileObject) {
      this.editedItem.background_img = new Image();
      const reader = new FileReader();
      reader.onload = (e) => {
        this.editedItem.background_img = e.target.result;
      };
      reader.readAsDataURL(fileObject);
    },

    removeImage() {
      this.editedItem.background_img = "";
    },

    save() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      var tmp_url = "/meeting/create/";
      axios
        .post(SERVER_URL + tmp_url, this.editedItem, config)
        .then(() => {
          this.GetMeeting();
          this.close();
          // this.$router.push({ name: 'articlelist' })
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },

    deleteItem() {
      axios
        .post(SERVER_URL + "/meeting/delete/" + this.selected[0], this.selected)
        .then(() => {
          this.deleteMeeting = false;
          this.GetMeeting();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    meetingDetail(m_id) {
      this.$router.push({
        name: "meetingDetail",
        params: {
          m_id: m_id,
        },
      });
    },
  },
};
</script>

<style scoped>

.transbox {
  text-align: center;
  height: 200px;
  background-color: rgba(118, 126, 154, 0.5);
}
.meeting_title {
  height: 200px;
  margin-top: 70px;
  font-size: 40px;
}
.fixed {
  position: fixed;
  right: 20px;
  bottom: 30px;
}

.v-speed-dial {
  position: absolute;
  right: 20px;
  bottom: 30px;
}

#create .v-btn--floating {
  position: relative;
}



</style>

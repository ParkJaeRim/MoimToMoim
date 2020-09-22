<template>
  <div>
    <v-container>
      <v-row dense>
        <v-col v-for="(meeting, i) in meetings" :key="i" cols="12">
          <v-card class="mx-auto" max-width="400" @click="meetingDetail(meeting.id)"> 
            <v-img
              :src="meeting.background_img"
              class="white--text align-center text-center"
              height="200px"
            >
            <div class="transbox">
              <v-card-text>
                  <div class="meeting_title">{{meeting.title}}</div>
                  <!-- <div>인원수 : {{meeting.ppl}}</div>
                  <div>평균연령 : {{meeting.avg_age}}</div> -->
              </v-card-text>
              <!-- <template v-slot:item="{ item }">
                <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
                <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
              </template>-->
            </div>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-dialog v-model="dialog" max-width="500px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="purple lighten-3" dark class="mb-2" v-bind="attrs" v-on="on">모임 생성</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline" >{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="12">
                <v-text-field v-model="editedItem.title" label="모임 이름"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
            <v-col cols="12" sm="6" md="12">
              <v-btn-toggle v-model="editedItem.avg_age"  tile color="purple lighten-1" group>
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
              <v-btn-toggle v-model="editedItem.ppl"  tile color="purple lighten-1" group>
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
                <v-file-input label="Background_img" @change="onChangeImages"></v-file-input>
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
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "MeetingList",
  data() {
    return {
      meetings: [],
      dialog: false,
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

    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "모임 생성" : "모임 수정";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  created() {
    this.GetMeeting();
  },
  methods: {
    GetMeeting() {
      axios
        .get(SERVER_URL + "/meeting/")
        .then((res) => {
          this.meetings = res.data;
        })
        .catch((err) => console.error(err.response));
    },

    editItem(item) {
      this.editedIndex = this.meetings.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
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
      //   if (this.editedIndex == -1) {
      //     var tmp_url = "/articles/create/"
      //   } else {
      //     var tmp_url = "/articles/" + this.editedItem.id + "/modify/"
      //   }
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

    meetingDetail(m_id) {
      this.$router.push({
        name : "meetingDetail",
        params: {
          m_id: m_id,
        },
      });    
    },
  },
};
</script>

<style scoped>
.transbox{
    text-align:center;  
    height: 200px;
    background-color: rgba(118, 126, 154, 0.5);
}
.meeting_title{
  height:200px;
  margin-top:70px;
  font-size:40px; 
  font-family:'Nanum Brush Script'
}
</style>
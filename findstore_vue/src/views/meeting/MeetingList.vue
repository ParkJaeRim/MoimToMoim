<template>
  <div>
    <v-container>
      <v-row dense>
        <v-col v-for="(meeting, i) in meetings" :key="i" cols="12">
          <v-card class="mx-auto" max-width="400">
            <v-img
              :src="meeting.background_img"
              class="white--text align-center text-center"
              height="200px"
            >
              <v-chip class="ma-2" label>
                <v-card-title>{{meeting.title}}</v-card-title>
              </v-chip>

              <!-- <v-card-subtitle class="pb-0">Number 10</v-card-subtitle> -->
              <v-card-text class="text--primary">
                <v-chip class="ma-2" label>
                  <div>인원수 : {{meeting.ppl}}</div>
                </v-chip>
                <v-chip class="ma-2" label>
                  <div>평균연령 : {{meeting.avg_age}}</div>
                </v-chip>
              </v-card-text>
              <!-- <template v-slot:item="{ item }">
                <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
                <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
              </template>-->
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-dialog v-model="dialog" max-width="500px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">New Item</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field v-model="editedItem.title" label="Title"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field v-model="editedItem.avg_age" label="연령대"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field v-model="editedItem.ppl" label="인원수"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-file-input label="Background_img" @change="onChangeImages"></v-file-input>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="save">Save</v-btn>
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
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
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
  },
};
</script>

<style scoped>
</style>
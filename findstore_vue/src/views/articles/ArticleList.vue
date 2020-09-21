<template>
  <div>
    <h1>ArticleList</h1>
    <v-data-table :headers="headers" :items="articles" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>My CRUD</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
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
                      <v-text-field v-model="editedItem.content" label="Content"></v-text-field>
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
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
      <!-- <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template> -->
    </v-data-table>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleList",
  data() {
    return {
      articles: [],
      dialog: false,
      headers: [
        { text: "Title", value: "title" },
        { text: "Content", value: "content" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        title: "",
        content: "",
      },
      defaultItem: {
        title: "",
        content: "",
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
    this.GetArticles()
  },
  methods: {
    GetArticles() {
      axios
        .get(SERVER_URL + "/articles/")
        .then((res) => {
          this.articles = res.data;
        })
        .catch((err) => console.error(err.response));
    },

    editItem (item) {
      this.editedIndex = this.articles.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      const index = this.desserts.indexOf(item)
      confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      var tmp_url = ''
      if (this.editedIndex == -1) {
        tmp_url = "/articles/create/"
      } else {
        tmp_url = "/articles/" + this.editedItem.id + "/modify/"
      }
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + tmp_url, this.editedItem, config)
      .then(res => { 
        console.log(res.data) 
        // this.$router.push({ name: 'articlelist' })
      })
      .catch(error => {
        console.log(error.response.data)
      })
      this.GetArticles()
      this.close();
    },
  },
};
</script>

<style>
</style>
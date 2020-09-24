<template>
  <div class="point">
    <v-btn @click="sheet = !sheet" size="36" fab color="deep-purple lighten-4">
      <v-icon>fas fa-route</v-icon>
    </v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="text-center" height="100px">
        
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  name: "footerlist",
  data() {
    return {
      sheet: false,
    };
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
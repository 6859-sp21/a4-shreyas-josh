<template>
  <div class="main">
    <h1>Who is actually getting COVID vaccines in MA?</h1>
    <div class="map-container">
      <Map :race="race" :date="date"></Map>
    </div>
    <div class="controls">
      <input type="radio" id="one" value="White" v-model="race" />
      <label for="one">White</label>
      <br />
      <input type="radio" id="two" value="Black" v-model="race" />
      <label for="two">Black</label>
      <br />
      <vue-slider v-model="date" :data="dates" :marks="true" />
    </div>
  </div>
</template>
<script>
import Map from "@/components/Map";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/antd.css";

export default {
  name: "Main",
  components: { Map, VueSlider },
  data() {
    return {
      race: "White",
      date: "April-1-2021",
      dates: [
        "March-11-2021",
        "March-18-2021",
        "March-25-2021",
        "April-1-2021",
      ],
    };
  },
};
</script>

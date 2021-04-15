<template>
  <div class="main">
    <h1>Who is actually getting COVID vaccines in MA?</h1>
    <div class="blurb">
      The US has vaccinated more people against COVID-19 than any country so
      far, but how equitable has the rollout been? Here we show the percent of
      population to receive at least a single dose by race.
    </div>

    <div id="color_code">
      <span style="position: relative; bottom: 7%; left: -4%"> Percent of demographic with at least one dose </span>
      <br />
      <div>
        <span class="ib gradient_labels" style="right: 2%;">0%</span>
        <div class="gradient ib"></div>
        <span class="ib gradient_labels" style="left: 2%;">100%</span>
      </div>
    </div>

    <div class="map-container">
      <Map :race="race" :date="date"></Map>
    </div>
    <div class="controls">
      <input type="radio" id="one" value="White" v-model="race" />
      <label for="one">White</label>
      &nbsp;
      <input type="radio" id="two" value="Black" v-model="race" />
      <label for="two">Black</label>
      &nbsp;
      <br />
      <br />
      <vue-slider v-model="date" :data="dates" :marks="true" />
    </div>
    <div class="sources">
      Data Sources:
      <a
        href="https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/saz5-9hgg"
        >CDC</a
      >,
      <a
        href="https://www.mass.gov/info-details/massachusetts-covid-19-vaccination-data-and-updates"
        >MA Government</a
      >,
      <a
        href="https://www.modernatx.com/covid19vaccine-eua/providers/vial-lookup"
        >Moderna</a
      >,
      <a href="https://data.census.gov/cedsci/table%3Fq=ACSDT5Y2012.B02001"
        >US Census</a
      >
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
<style scoped>
.blurb {
  margin-bottom: 4rem;
  color: #969696;
}

.ib {
  display: inline-block;
}

.gradient_labels{
  position: relative; 
  bottom: 25%;
}

.gradient {
  height: 25px;
  width: 150px;
  background-color: yellow; /* For browsers that do not support gradients */
  background-image: linear-gradient(to right, black , yellow);
}

.sources {
  margin-top: 5rem;
  color: #969696;
}

.sources a {
  color: #8e8ebd;
}
</style>

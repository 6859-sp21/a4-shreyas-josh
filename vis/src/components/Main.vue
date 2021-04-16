<template>
  <div class="main">
    <h1>Who is actually getting COVID vaccines in MA?</h1>
    <div class="blurb">
      The US has vaccinated more people against COVID-19 than any country so
      far, but how equitable has the rollout been? Here we show the percent of
      population to receive at least a single dose by race.
    </div>

    <div id="color_code">
      <span style="position: relative; bottom: 7%;"> % of demographic with ≥ 1 dose </span>
      <br />
      <div class="bar-container">
        <span class="ib gradient_labels">0%</span>
        <div class="gradient ib"></div>
        <span class="ib gradient_labels">100%</span>
      </div>
    </div>

    <div class="no-data">
      <div class="hatched-box crosshatch"></div>
      <div class="no-data-label"> = No Data</div>
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
      race: "Black",
      date: "April-15-2021",
      dates: [
        'March-11-2021', 'March-18-2021', 'March-25-2021', 'April-1-2021',
        'April-8-2021', 'April-15-2021',
      ],
    };
  },
};
</script>
<style scoped>
.blurb {
  margin-bottom: 2rem;
  color: #969696;
}

.ib {
  display: inline-block;
}

.gradient {
  height: 25px;
  width: 150px;
  background-color: yellow; /* For browsers that do not support gradients */
  background-image: linear-gradient(to right, black , yellow);
  margin: 0rem 0.5rem;
}

.sources {
  margin-top: 5rem;
  color: #969696;
}

input {
  cursor: pointer;
}

label {
  cursor: pointer;
}

.sources a {
  color: #8e8ebd;
}

.no-data {
  display: flex;
  align-items: center;
  margin-top: 0.3rem;
}

.hatched-box {
  width: 25px;
  height: 25px;
  margin-right: 0.4rem;
}

.crosshatch {
   color: white;
   background-image: linear-gradient(
      320deg, 
      rgba(255,255,255,0.2) 25%, 
      transparent 25%, 
      transparent 50%, 
      rgba(255,255,255,0.2) 50%, 
      rgba(255,255,255,0.2) 75%, 
      transparent 75%, 
      transparent
      );
   background-size: 10px 10px;
}

.bar-container {
  display: flex;
  margin-top: 0.5rem;
}
</style>

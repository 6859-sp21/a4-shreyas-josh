<template>
  <div class="map">
    <div class="spinner-box" v-if="loading">
      <Spinner theme="light" radius="50px"></Spinner>
    </div>
    <Tooltip :paused="tipPause" :visible="tipVisible" :data="tipData"></Tooltip>
    <div class="map-rel">
      <Button
        class="reset-button"
        @click="reset"
        v-if="agitated"
        :square="true"
      >
        <font-awesome-icon :icon="['far', 'compass']" />
      </Button>
      <div class="svg-container" v-once></div>
    </div>
  </div>
</template>
<script>
import Button from "./Button";
import Spinner from "./Spinner";
import Tooltip from "./Tooltip";
// import MapSVG from '@/assets/uszipcodemap.svg';
import * as d3 from "d3";
import combined from "@/assets/combined.json";

let svg;
let g;
let zoom;
let container;

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

const fdata = {};

for (let i = 0; i < combined.length; i++) {
  fdata[combined[i].zip] = {};
}

for (let i = 0; i < combined.length; i++) {
  fdata[combined[i].zip][combined[i].date] = combined[i];
}

window.fdata = fdata;
window.combined = combined;

function getRaceColor(race, date, zip) {
  const filtered = fdata[zip][date];
  const pop = `${race}Pop`;

  if (filtered[pop] < filtered[race]) {
    return NaN;
  }

  return filtered[race] / filtered[pop];
}

function getRacePop(race, date, zip) {
  const filtered = fdata[zip][date];
  const pop = `${race}Pop`;
  return filtered[pop];
}

export default {
  name: "Map",
  components: { Button, Spinner, Tooltip },
  props: {
    race: {
      type: String,
      default: "White",
    },
    date: {
      type: String,
      default: "April-1-2021",
    },
  },
  watch: {
    race() {
      this.draw();
    },
    date() {
      this.draw();

      if (this.tipVisible) this.updateTTNumbers();
    },
  },
  data() {
    return {
      agitated: false,
      loading: true,
      tipVisible: false,
      tipPause: false,
      tipData: {
        name: "",
        zip: "",
      }
    };
  },
  mounted() {
    d3.xml(require("@/assets/uszipcodemap.svg")).then((data) => {
      d3.select(".svg-container").node().append(data.documentElement);

      let currentZoomLevel = 1;

      svg = d3.select("svg.map-svg");
      container = svg.select("g");
      container
        .attr("id", "container")
        .attr("transform", "translate(0,0)scale(1,1)")
        .attr("stroke-width", 0.05);
      g = svg.select(".counties");
      g.selectAll("path:not([data-state='MA'])").remove();

      this.draw();

      // Set viewbox to be of whatever is left.
      const bbox = container.node().getBBox();
      svg.attr("viewBox", `${bbox.x} ${bbox.y} ${bbox.width} ${bbox.height}`);
      svg.attr("preserveAspectRatio", "xMidYMid meet");

      const clicked = (event) => {
        const { x, y, width, height } = event.target.getBBox();
        const gbox = bbox;
        const vx = gbox.x;
        const vy = gbox.y;
        const vw = gbox.width;
        const vh = gbox.height;

        const getTransform = (node, xScale) => {
          const b2 = node.getBBox();
          var bx = b2.x;
          var by = b2.y;
          var bw = b2.width;
          var bh = b2.height;
          var tx = -bx * xScale + vx + vw / 2 - (bw * xScale) / 2;
          var ty = -by * xScale + vy + vh / 2 - (bh * xScale) / 2;
          return { tx, ty };
        };

        let [x0, y0] = [x - bbox.x, y - bbox.y];
        let [x1, y1] = [x + width - bbox.x, y + height - bbox.y];

        let scale = Math.min(gbox.width / (x1 - x0), gbox.height / (y1 - y0));
        scale /= 2;

        const { tx, ty } = getTransform(event.target, scale);

        svg
          .transition()
          .duration(750)
          .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));

        this.tipPause = true;
        this.updateTT(event);

        event.stopPropagation();
      };

      document.addEventListener("mousemove", this.mm);

      g.selectAll("path").on("click", clicked);
      g.selectAll("path").on("mouseover", function () {
        d3.select(this).attr("stroke-width", 0.3 / currentZoomLevel);
      }).on("mouseout", function () {
        d3.select(this).attr("stroke-width", 0.05 / currentZoomLevel);
      })

      const zoomed = ({ transform }) => {
        currentZoomLevel = transform.k;
        container.attr("transform", transform);
        g.selectAll("path").attr("stroke-width", 0.05 / transform.k);
        this.agitated = !(transform === d3.zoomIdentity);
      };

      zoom = d3.zoom().scaleExtent([1, 40]).on("zoom", zoomed);

      svg.call(zoom);
      this.loading = false;
    });
  },
  destroyed() {
    document.removeEventListener("mousemove", this.mm);
  },
  methods: {
    mm(e) {
      if (this.tipPause) return;
      this.updateTT(e);
    },
    updateTT(e) {
      const tag = e.target.tagName;
      if (tag === "path") {
        const elem = d3.select(e.target);

        this.tipVisible = true;
        this.tipData = {
          name: elem.attr("data-name").toProperCase(),
          zip: elem.attr("data-zip"),
        }
        this.updateTTNumbers();
      } else {
        this.tipVisible = false;
      }
    },
    updateTTNumbers() {
      const dd = this.date;
      const zip = this.tipData.zip;

      const races = [];

      for (let r of ["Black", "White"]) {
        const pop = getRacePop(r, dd, zip);
        const p = getRaceColor(r, dd, zip);
        races.push({
          name: r.toProperCase(),
          val: (isNaN(p)) ? "-" : `${(p * 100).toFixed(2)}%`,
          pop: `${(numberWithCommas(pop))}`,
        })
      }

      this.tipData = {
        name: this.tipData.name,
        zip: zip,
        races: races,
      }
    },
    reset() {
      this.agitated = false;
      this.tipVisible = false;
      this.tipPause = false;
      svg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
    },
    draw() {
      const rr = this.race;
      const dd = this.date;
      g.selectAll("path")
        .transition()
        .delay(10)
        .style("fill", function () {
          const zip = this.getAttribute("data-zip");

          if (fdata[zip] !== undefined && fdata[zip][dd] !== undefined) {
            const d = getRaceColor(rr, dd, zip);

            if (!isNaN(d)) {
              return `rgba(255, 255, 0, ${d})`;
            } else {
              return "url(#diagonalHatch)";
            }
          }
          console.log(fdata[zip]);
          return "black";
        });
    },
  },
};
</script>
<style lang="scss">
svg.map-svg {
  width: 100%;
}

.map-rel {
  position: relative;
}

.reset-button {
  position: absolute;
  top: 2rem;
  right: 2rem;
  font-size: 1.2em;
  z-index: 2000;
}

svg.map-svg path {
  stroke: rgb(255 255 255 / 47%);
  // stroke-width: 0.04px;
  fill: black;
  cursor: pointer;
  // transform-box: fill-box;
}

svg.map-svg path:hover {
  fill: rgb(11, 2, 34);
  // stroke-width: 1%;
  // transform: scale(1.2);
  // transform-origin: center;
}

.spinner-box {
  display: flex;
  width: 100%;
  height: 26rem;
  justify-content: center;
  align-items: center;
}
</style>

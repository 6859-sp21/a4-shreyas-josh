<template>
  <div class="map">
    <div class="map-rel">
      <Button
        class="reset-button"
        @click="reset"
        v-if="agitated"
        :square="true"
      >
        <font-awesome-icon :icon="['far', 'compass']" />
      </Button>
      <!-- <MapSVG class="map-svg" v-once></MapSVG> -->
      <div class="svg-container" v-once></div>
    </div>
  </div>
</template>
<script>
import Button from "./Button";
// import MapSVG from '@/assets/uszipcodemap.svg';
import * as d3 from "d3";
import combined from "@/assets/combined.json";

let svg;
let g;
let zoom;
let container;

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
  return filtered[race] / filtered[pop];
}

export default {
  name: "Map",
  components: { Button },
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
    },
  },
  data() {
    return {
      agitated: false,
    };
  },
  mounted() {
    d3.xml(require("@/assets/uszipcodemap.svg")).then((data) => {
      d3.select(".svg-container").node().append(data.documentElement);

      svg = d3.select("svg.map-svg");
      container = svg.select("g");
      container
        .attr("id", "container")
        .attr("transform", "translate(0,0)scale(1,1)");
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

        event.stopPropagation();
      };

      g.selectAll("path").on("click", clicked);

      const zoomed = ({ transform }) => {
        container.attr("transform", transform);
        this.agitated = !(transform === d3.zoomIdentity);
      };

      zoom = d3.zoom().scaleExtent([1, 40]).on("zoom", zoomed);

      svg.call(zoom);
    });
  },
  methods: {
    reset() {
      this.agitated = false;
      svg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
    },
    draw() {
      const rr = this.race;
      const dd = this.date;
      g.selectAll("path")
        .transition()
        .delay(50)
        .style("fill", function () {
          const zip = this.getAttribute("data-zip");

          if (fdata[zip] !== undefined && fdata[zip][dd] !== undefined) {
            const d = getRaceColor(rr, dd, zip);
            return `rgba(255, 255, 0, ${d})`;
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
}

svg.map-svg path {
  stroke: rgb(255 255 255 / 47%);
  stroke-width: 0.04px;
  fill: black;
  cursor: pointer;
  // transform-box: fill-box;
}

svg.map-svg path:hover {
  fill: rgb(11, 2, 34);
  stroke-width: 0.3px;
  // transform: scale(1.2);
  // transform-origin: center;
}
</style>
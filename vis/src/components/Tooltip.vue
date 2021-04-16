<template>
  <div class="tooltip" :style="position" v-if="visible">
    <div class="inner-tip">
        <div class="tt">
            <strong>{{ data.name }}</strong> ({{ data.zip }})
        </div>
        <table class="tab">
            <thead>
                <th>Demographic</th>
                <th>% Vaccinated</th>
                <th>Population</th>
            </thead>
            <tbody>
                <tr v-for="r in data.races" :key="r.name">
                    <td>
                        {{r.name}}
                    </td>
                    <td>
                        {{r.val}}
                    </td>
                    <td>
                        {{r.pop}}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>
<script>
export default {
    name: "Tooltip",
    props: {
        data: {
            type: Object,
            required: true,
        },
        visible: {
            type: Boolean,
            required: false,
            default: true,
        },
        paused: {
            type: Boolean,
            required: false,
            default: false,
        }
    },
    data() {
        return {
            mouseX: 0,
            mouseY: 0,
        }
    },
    computed: {
        position() {
            return {
                "left": `${this.mouseX}px`,
                "top": `${this.mouseY}px`,
            }
        }
    },
    methods: {
        mouseMove(e) {
            if (this.paused) return;
            this.mouseX = e.pageX;
            this.mouseY = e.pageY;
        }
    },
    mounted() {
        document.addEventListener("mousemove", this.mouseMove, false);
    },
    destroyed() {
        document.removeEventListener("mousemove", this.mouseMove, false);
    }
}
</script>
<style lang="scss" scoped>
.tooltip {
  position: absolute;
  left: 0;
  top: 0;
  background: rgb(0, 0, 0, 0.8);
  border-radius: 10px;
  border: 3px solid rgb(133, 133, 133);
  color: white;
  padding: 1rem;
  transform: translate(-50%, -150%);
  z-index: 100;
}

.tt {
    color: #ffffff;
    margin-bottom: 0.5rem;
    font-size: 20px;
}

th {
    color: #b1b1b1;
    text-transform: uppercase;
    font-size: 11px;
    padding-right: 1rem;
}

.tab {
    margin-left: -2px;
    padding-left: 0px;
}
</style>

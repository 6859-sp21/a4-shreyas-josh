<template>
  <div class="spinner circle" :class="classDict()" :style="size"></div>
</template>

<script>
export default {
  name: 'Spinner',
  props: {
    theme: {
      type: String,
      default: 'light'
    },
    radius: {
      type: String,
      default: '20px'
    },
    thickness: {
      type: String,
      default: '3.5px'
    },
    speed: {
      type: String,
      default: 'fast'
    }
  },
  computed: {
    size () {
      return {
        width: this.radius,
        height: this.radius,
        borderWidth: this.thickness
      }
    }
  },
  methods: {
    classDict () {
      const obj = {}
      obj[this.theme] = true
      obj[this.speed] = true
      return obj
    }
  }
}
</script>

<style lang="scss">
.circle {
  box-sizing: border-box;
  border-radius: 100%;
  border: 10px solid rgba(0, 0, 0, 0.2);
}
.fast {
  animation: spin 0.7s infinite linear;
}
.slow {
  animation: spin 1.8s infinite linear;
}
.dark {
  border-top-color: rgba(0, 0, 0, 0.418);
}
.light {
  border-top-color: #fff;
}
@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}
</style>

<template>
  <div class="big-button" @click="$emit('click')" :class="classDict">
    <div class="button-grid-wrapper">
      <div class="button-slot-wrapper" :class="{'button-vanish': loading}">
        <slot></slot>
      </div>
      <div class="big-button-wrapper" :class="{'button-show': loading}">
        <Spinner theme="light"></Spinner>
      </div>
    </div>
  </div>
</template>

<script>
import Spinner from './Spinner.vue'

export default {
  name: 'Button',
  components: { Spinner },
  props: {
    color: {
      type: String,
      default: 'primary'
    },
    loading: {
      type: Boolean,
      default: false
    },
    square: {
      type: Boolean,
      default: false,
    }
  },
  data () {
    return {}
  },
  computed: {
    classDict () {
      const obj = {}
      obj[this.color] = true
      
      if (this.square) {
        obj.square = true;
      }

      return obj
    }
  }
}
</script>

<style>
.button-grid-wrapper {
  display: grid;
  grid-template-areas: "area";
  font-weight: 600;
}

.big-button {
  padding: 6px 1.3rem;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
  user-select: none;
}

.big-button.square {
  padding: 0.5rem 0.6rem;
}

.big-button:hover {
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.03), 0 1px 0 rgba(0, 0, 0, 0.05),
    0 1px 3px rgba(0, 0, 0, 0.1);
}

.big-button-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  grid-area: area;
  opacity: 0;
}

.primary {
    color: rgba(255, 255, 255, 0.61);
    background: rgb(103 103 103 / 92%);
}

.secondary {
    color: white;
    background: #B5B5B5;
}

.orange {
  color: white;
  background: #F2994A;
}

.button-vanish {
  opacity: 0;
}

.button-show {
  opacity: 1;
}

.button-slot-wrapper {
  grid-area: area;
  text-align: center;
}
</style>

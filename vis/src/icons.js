import Vue from 'vue'

import {
  library
} from '@fortawesome/fontawesome-svg-core'

import {
  faCompass
} from '@fortawesome/free-regular-svg-icons/faCompass'

import {
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

library.add(faCompass)

Vue.component('font-awesome-icon', FontAwesomeIcon)

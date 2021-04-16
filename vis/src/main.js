import Vue from "vue";
import App from "./App.vue";

import './icons'

String.prototype.toProperCase = function () {
  return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");

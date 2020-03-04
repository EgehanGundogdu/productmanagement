import Vue from "vue";
import Vuex from "vuex";
import product from "../store/product";
import trade from "../store/trade";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    product,
    trade
  }
});

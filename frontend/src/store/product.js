import { getAllProduct, addNewProduct } from "../api/product_api";

const state = {
  productList: []
};

const getters = {
  getProductList(state) {
    return state.productList;
  }
};
const mutations = {
  setProducts(state, payload) {
    state.productList = payload;
  },
  setNewProductToStore(state, payload) {
    state.productList.push(payload);
  }
};
const actions = {
  initProducts({ commit }) {
    getAllProduct()
      .then(res => {
        commit("setProducts", res.data);
      })
      .catch(err => console.log(err));
  },
  saveProduct({ commit }, payload) {
    addNewProduct(payload)
      .then(commit("setNewProductToStore", payload))
      .catch(err => console.log(err));
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};

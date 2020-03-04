import apiService from "./client";
const endPoint = "/api";
const getAllProduct = () => apiService.get(`${endPoint}/getproducts`);

const addNewProduct = payload =>
  apiService.post(`${endPoint}/add-product`, payload);

export { getAllProduct, addNewProduct };

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import ProductList from "../views/ProductList.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: Home,
    children: [
      {
        path: "",
        name: "ProductList",
        component: ProductList
      },
      {
        path: "/urun-ekle",
        name: "AddProduct",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import("../views/AddProduct.vue")
      },
      {
        path: "/urun-satisi",
        name: "SellProduct",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import("../views/SellProduct.vue")
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;

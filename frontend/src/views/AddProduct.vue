<template>
  <div class="container">
    <div class="row">
      <div class="col-6 offset-3 pt-3 card mt-5 shadow">
        <div class="card-body">
          <h3>Ürün İşlemleri</h3>
          <hr />
          <div class="form-group">
            <label>Ürün Adı</label>
            <input
              v-model="product.name"
              type="text"
              class="form-control"
              placeholder="Ürün adını giriniz.."
            />
          </div>
          <div class="form-group">
            <label>Adet</label>
            <input
              v-model="product.amount"
              type="text"
              class="form-control"
              placeholder="Ürün adetini giriniz.."
            />
          </div>
          <div class="form-group">
            <label>Fiyat</label>
            <input
              v-model="product.price"
              type="text"
              class="form-control"
              placeholder="Ürün fiyatı giriniz.."
            />
          </div>
          <div class="form-group">
            <label>Açıklama</label>
            <textarea
              v-model="product.caption"
              cols="30"
              rows="5"
              placeholder="Ürüne ait bir açıklama giriniz..."
              class="form-control"
            ></textarea>
          </div>
          <hr />
          <button @click="saveProduct(product)" class="btn btn-primary">
            Kaydet
          </button>
        </div>
      </div>
    </div>
    <br /><br /><br />
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      product: {
        name: "",
        caption: "",
        amount: 0,
        price: 0.0
      }
    };
  },
  methods: {
    ...mapActions(["saveProduct"])
  }
};
</script>

<style></style>

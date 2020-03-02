<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark"
    style="background-color: #563F7A"
  >
    <router-link class="navbar-brand" tag="a" to="/">Ürün Listesi</router-link>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <router-link tag="li" :to="{ name: 'AddProduct' }" class="nav-item">
          <a class="nav-link">Ürün İşlemleri</a>
        </router-link>
        <router-link tag="li" :to="{ name: 'SellProduct' }" class="nav-item">
          <a class="nav-link">Ürün Çıkışı</a>
        </router-link>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style></style>

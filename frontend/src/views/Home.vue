<template>
  <div class="home">
    <navigation></navigation>
    <transition name="fade" mode="out-in">
      <router-view></router-view
    ></transition>
    <bottom-nav></bottom-nav>
  </div>
</template>

<script>
// @ is an alias to /src
import BottomNav from "@/components/BottomNav.vue";
import Navigation from "@/components/Navigation.vue";

export default {
  name: "Home",
  components: {
    BottomNav,
    Navigation
  }
};
</script>

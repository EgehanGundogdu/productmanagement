<template>
  <div class="home">
    <navigation></navigation>
    <router-view></router-view>
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

<template>
  <div class="container">
    <Header />
    <!-- `<Nuxt />` is a component being used in the Vue template. It is likely a custom component or a -->
    <!-- component provided by the Nuxt.js framework. -->
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
export default {
  components: {
    Header,
    Footer,
  },
};
</script>

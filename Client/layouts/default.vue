<template>
  <div class="container">
    <Header />
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Header from "~/components/Header.vue";
import Footer from "~/components/Footer.vue";
export default {
  components: {
    Header,
    Footer,
  },
  // SEO
  head() {
    return {
      link: [
        {
          rel: 'canonical',
          href: `http://localhost:3000${this.$route.path}`
          // href: `${process.env.API_URL}${this.$route.path}`
        }
      ]
    };
  },
};
</script>

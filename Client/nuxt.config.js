export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: "static",

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "IT_Blog",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "UTF-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      // { hid: 'description', name: 'description', content: '' },
      // { name: 'format-detection', content: 'telephone=no' },
      {
        name: "description",
        content:
          "This project is a simple test Blog using such technologies: NuxtJS, Bootstrap, Django, Django Rest Framework, Webpack",
      },
      { name: "keywords", content: "Blog, Django, NuxtJS, Bootstrap" },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon/favicon_lg.png" },
    ],
    // Scripts
    script: [{}],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  // Bootstrap import is declared in index.scss
  css: ["~/assets/scss/index.scss"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: "~/plugins/bootstrap.js",
      mode: "client",
    },
    {
      src: "~/plugins/jquery.js",
      mode: "client",
    },
    {
      src: "~/plugins/js/index.js",
      mode: "client",
    },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    // "bootstrap-vue/nuxt",
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/axios",
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};

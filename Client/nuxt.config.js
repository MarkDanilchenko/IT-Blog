require("dotenv").config({ path: "../.env", override: true });

export default {
  // Target: https://go.nuxtjs.dev/config-target
  // target: "static",
  server: {
    host: "127.0.0.1",
    port: 3000,
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "IT_Blog",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "UTF-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        name: "description",
        content:
          "This project is a simple test Blog using such technologies as: Nuxt2 (NuxtJS), Bootstrap, Django, Django Rest Framework, Webpack, MySQL",
      },
      {
        name: "keywords",
        content:
          "Blog, Django, Django Rest Framework, Nuxt2 (NuxtJS), Bootstrap, MySQL",
      },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon/favicon_lg.png" },
    ],
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
    {
      src: "~/plugins/vuelidate.js",
    },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [["@nuxtjs/dotenv", { filename: ".env", path: "../" }]],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: ["@nuxtjs/axios", "@nuxtjs/auth-next"],

  auth: {
    strategies: {
      local: {
        scheme: "refresh",
        token: {
          property: "access",
          maxAge: 60 * 60,
          type: "Bearer",
        },
        refreshToken: {
          property: "refresh",
          maxAge: 60 * 60 * 24 * 2,
          data: "refresh",
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: "/api/token/", method: "post" },
          logout: false,
          refresh: { url: "/api/token_refresh/", method: "post" },
          user: { url: "/api/accounts/profile/", method: "get" },
        },
      },
    },
    redirect: {
      // if signIn is required
      login: "/accounts/signin/",
      // after signOunt
      logout: false,
      // after signIn
      home: "/",
    },
  },

  env: {
    API_URL:
      process.env.server_HostPort !== ""
        ? `http://${process.env.server_HostPort}`
        : "http://127.0.0.1:8000",
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  // BaseURL: for example, for auth (default it uses nuxtjs's localhost:3000)
  axios: {
    baseURL:
      process.env.server_HostPort !== ""
        ? `http://${process.env.server_HostPort}`
        : "http://127.0.0.1:8000",
  },

  loading: {
    color: "#000000",
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};

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
          "This project is a simple test IT_Blog using such technologies as: Nuxt2 (NuxtJS), Bootstrap5, Django5, DRF, Webpack, MySQL, Docker, Compose and NGINX.",
      },
      {
        name: "keywords",
        content:
          "IT_Blog, Django, Django Rest Framework, Nuxt2 (NuxtJS), Bootstrap5, MySQL, Django5, DRF, Webpack, Docker, Compose, NGINX",
      },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon/favicon_lg.png" },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  // Bootstrap import is declared in index.scss
  css: ["@/assets/scss/index.scss"],
  css: ["@/assets/scss/index.scss"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: "@/plugins/bootstrap.js",
      src: "@/plugins/bootstrap.js",
      mode: "client",
    },
    {
      src: "@/plugins/jquery.js",
      src: "@/plugins/jquery.js",
      mode: "client",
    },
    {
      src: "@/plugins/vuelidate.js",
      src: "@/plugins/vuelidate.js",
      mode: "client",
    },
    {
      src: "@/plugins/js/index.js",
      mode: "client",
      src: "@/plugins/js/index.js",
      mode: "client",
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
          maxAge: 5 * 60,
          maxAge: 5 * 60,
          type: "Bearer",
        },
        refreshToken: {
          property: "refresh",
          maxAge: 60 * 60 * 24 * 1,
          maxAge: 60 * 60 * 24 * 1,
          data: "refresh",
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: "/api/token/", method: "post" },
          logout: false,
          refresh: { url: "/api/token/refresh/", method: "post" },
          refresh: { url: "/api/token/refresh/", method: "post" },
          user: { url: "/api/accounts/profile/", method: "get" },
        },
      },
    },
    redirect: {
      // if signIn is required
      login: "/api/accounts/signin/",
      // after signOut
      logout: "/api/accounts/signin/",
      // after signIn
      home: "/",
    },
  },

  /* The `env` property in the Nuxt.js configuration is used to define environment variables that can
  be accessed within your application. */
  /* The `env` property in the Nuxt.js configuration is used to define environment variables that can
  be accessed within your application. */
  env: {
    API_URL: `http://${process.env.server_HostPort_1}`,
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  /* This part of the configuration is setting the base URL for Axios requests in your Nuxt.js
  application. */
  /* This part of the configuration is setting the base URL for Axios requests in your Nuxt.js
  application. */
  axios: {
    baseURL: process.env.API_URL,
    baseURL: process.env.API_URL,
  },

  /* The `loading` property in the Nuxt.js configuration is used to customize the loading indicator
 color that appears when navigating between pages or when data is being fetched. In this case,
 `loading: { color: "#000000" }` sets the color of the loading indicator to black (#000000). */
  /* The `loading` property in the Nuxt.js configuration is used to customize the loading indicator
 color that appears when navigating between pages or when data is being fetched. In this case,
 `loading: { color: "#000000" }` sets the color of the loading indicator to black (#000000). */
  loading: {
    color: "#000000",
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};

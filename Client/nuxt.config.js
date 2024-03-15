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
          "This project is a simple IT_Blog using such technologies as: Nuxt2 (NuxtJS), Bootstrap5, Django5, DRF, Webpack, MySQL, Docker, Compose and NGINX.",
      },
      {
        name: "keywords",
        content:
          "IT_Blog, DRF, Nuxt2 (NuxtJS), Bootstrap5, MySQL, Django5, Webpack, Docker, Compose, NGINX",
      },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon/favicon_lg.png" },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  // Bootstrap import is declared in index.scss
  css: ["@/assets/scss/index.scss"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: "@/plugins/bootstrap.js",
      mode: "client",
    },
    {
      src: "@/plugins/jquery.js",
      mode: "client",
    },
    {
      src: "@/plugins/vuelidate.js",
      mode: "client",
    },
    {
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

  /* The `auth` section in the Nuxt.js configuration is used to define authentication strategies and
  settings for handling user authentication in the application. */
  auth: {
    strategies: {
      local: {
        scheme: "refresh",
        token: {
          property: "access",
          maxAge: 10,
        },
        refreshToken: {
          property: "refresh",
          data: "access",
          maxAge: 60 * 60 * 24 * 1,
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: "/api/token/", method: "post" },
          refresh: { url: "/api/token/refresh/", method: "post" },
          // do not used default logout function, because of necessity to blacklist refresh token manually
          logout: false,
          user: { url: "/api/accounts/profile/", method: "get" },
        },
      },
    },
    redirect: {
      // if signIn is required
      login: "/api/accounts/signin/",
      // after signOut do not redirect to other pages
      logout: false,
      // after signIn
      home: "/",
    },
  },

  /* The `env` property in the Nuxt.js configuration is used to define environment variables that can
  be accessed within your application. */
  env: {
    API_URL: `http://${process.env.server_HostPort_1}`,
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  /* This part of the configuration is setting the base URL for Axios requests in your Nuxt.js
  application. */
  axios: {
    baseURL: `http://${process.env.server_HostPort_1}`,
  },

  /* The `loading` property in the Nuxt.js configuration is used to customize the loading indicator
 color that appears when navigating between pages or when data is being fetched. In this case,
 `loading: { color: "#000000" }` sets the color of the loading indicator to black (#000000). */
  loading: {
    color: "#000000",
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};

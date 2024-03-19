require("dotenv").config({ path: "../.env", override: true });

export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: "static",
  server: {
    // host: "127.0.0.1",
    // host: "0.0.0.0",
    // port: 3000,
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
      // when page with vuelidate functions is loaded or refreshed cuelidate plugin should be loaded in both client and server!
      // mode: "client",
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
  modules: ["@nuxtjs/auth-next", "@nuxtjs/axios"],

  /* The `auth` section in the Nuxt.js configuration is used to define authentication strategies and
  settings for handling user authentication in the application. */
  middleware: ["auth"],
  auth: {
    strategies: {
      local: {
        scheme: "refresh",
        token: {
          property: "access",
          type: "Bearer",
          maxAge: 60,
          global: true,
        },
        refreshToken: {
          property: "refresh",
          data: "refresh",
          maxAge: 86400,
          global: true,
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: `/api/token/`, method: "post" },
          refresh: { url: `/api/token/refresh/`, method: "post" },
          user: { url: `/api/accounts/profile/`, method: "get" },
          // do not used default logout function, because of necessity to blacklist refresh token manually after logout
          // (API: path("api/token/blacklist/", TokenBlacklistView.as_view(), name="blacklist"),)
          logout: false,
        },
        /* The `autoLogout: true` configuration in the Nuxt.js auth strategy settings is used to
        automatically log out the user when their access token expires. When `autoLogout` is set to
        `true`, the user will be logged out as soon as their access token reaches its maximum age
        and expires. This helps ensure that the user is not able to access protected resources with
        an expired token and enforces the need for re-authentication to continue using the
        application securely. */
        autoLogout: false,
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
    // DEV
    API_URL: `http://${process.env.server_HostPort_1}`,
    // PROD
    // API_URL: ``,
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // DEV
    baseURL: `http://${process.env.server_HostPort_1}`,
    // PROD
    // baseURL: ``,
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

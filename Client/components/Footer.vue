<template>
  <section class="my-footer">
    <footer class="col-12 mt-3">
      <ul class="nav d-flex justify-content-center">
        <li class="nav-item">
          <nuxt-link to="/" class="nav-link px-2" title="Home page"><b>Home</b></nuxt-link>
        </li>
        <li>
          <nuxt-link to="#" class="nav-link px-2" title="Home page">&#9650; <b>Up</b></nuxt-link>
        </li>
      </ul>
      <hr class="my-1 offset-3" style="width: 50%" />
      <p class="text-center text-body-secondary pb-4">
        2024 MyHomeworks, &#123; &#125;
      </p>
    </footer>
  </section>
</template>

<script>
export default {
  name: "Footer",
};
</script>
<template>
  <section class="my-index">
    <!-- Carousel -->
    <!-- Carousel -->
    <!-- Carousel -->
    <Carousel />
    <!-- Posts -->
    <!-- Posts -->
    <!-- Posts -->
    <div class="all-posts">
      <div class="d-flex justify-content-center">
        <hr class="my-4" style="width: 50%" />
      </div>
      <div v-if="posts.length > 0">
        <h5 class="mb-3 mt-0 text-center lead"><b>Related posts</b></h5>
        <!-- Posts cards -->
        <!-- Posts cards -->
        <!-- Posts cards -->
        <div class="row d-flex justify-content-center">
          <div class="col-md-4 col-12" v-for="i in posts" :key="i.url">
            <div class="card mb-3 shadow">
              <div class="d-flex flex-column align-items-center justify-content-end">
                <img :src="`${i.image}`" class="img-fluid p-3 rounded CardsMainPage__img" :alt="`${i.h1}`"
                  :title="`${i.h1}`" />
                <div class="card-body">
                  <h3 class="card-title text-center">
                    <b>{{ i.h1 }}</b>
                  </h3>
                  <div class="card-text" v-html="i.description"></div>
                  <div class="d-flex flex-wrap">
                    <div v-for="j in i.tag" :key="j">
                      <nuxt-link :to="`/tags/${j}/`" class="badge bg-light rounded-pill nav-link me-1">#{{ j
                        }}</nuxt-link>
                    </div>
                  </div>
                  <div class="d-flex justify-content-between align-items-center mt-3">
                    <nuxt-link :to="`/posts/${i.url}/`" class="btn btn-sm btn-outline-secondary me-3">More</nuxt-link>
                    <span class="badge bg-secondary rounded-pill">{{ i.created_at }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- No posts -->
        <!-- No posts -->
        <!-- No posts -->
      </div>
      <div v-else>
        <h3 class="text-center lead my-5">No posts yet ...</h3>
      </div>
    </div>
    <!-- Pagination -->
    <!-- Pagination -->
    <!-- Pagination -->
    <Pagination :pageRange="pageRange" :CLIENT_API_URL="CLIENT_API_URL" @changePage="posts = $event" class="mt-3" />
  </section>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import Pagination from "@/components/Pagination.vue";
import axios from "axios";
export default {
  name: "Index",
  components: {
    Carousel,
    Pagination,
  },
  async asyncData({ isDev, route, store, env, params, query, req, res, redirect, error }) {
    const { data } = await axios.get(`${process.env.API_URL}/api/posts/`, {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    });
    const pageRange = (data.results && data.results.length > 0) ? Math.ceil(data.count / data.results.length) : 1;
    return {
      posts: data.results,
      pageRange: pageRange,
      CLIENT_API_URL: `${process.env.API_URL}/api/posts/`,
    };
  },
};
</script>
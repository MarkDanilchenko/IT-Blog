<template>
  <div>
    <Carousel />
    <section class="all-posts">
      <div class="d-flex justify-content-center">
        <hr class="my-4" style="width: 50%" />
      </div>
      <!-- {% if page_obj %} -->
      <div v-if="posts.length > 0">
        <h5 class="mb-3 mt-0 text-center text-muted"><i>Related posts</i></h5>
        <!-- cards -->
        <!-- cards -->
        <!-- cards -->
        <div class="row d-flex justify-content-center">
          <!-- {% for i in page_obj %} -->
          <div class="col-md-4" v-for="i in posts" :key="i.url">
            <div class="card mb-3 shadow">
              <div class="d-flex flex-column align-items-center justify-content-end">
                <img :src="i.image" class="img-fluid p-3 rounded" :alt="`${i.h1}`" :title="`${i.h1}`" />
                <div class="card-body">
                  <h3 class="card-title text-center">
                    <b>{{ i.h1 }}</b>
                  </h3>
                  <div class="card-text" v-html="i.description"></div>
                  <!-- {% for j in i.tag.all %} -->
                  <div class="d-flex flex-wrap">
                    <div v-for="j in i.tag">
                      <nuxt-link :to="`/tags/${j}/`" class="badge bg-light rounded-pill nav-link me-1">#{{ j
                      }}</nuxt-link>
                    </div>
                  </div>
                  <!-- {% endfor %} -->
                  <div class="d-flex justify-content-between align-items-center mt-3">
                    <nuxt-link :to="`/posts/${i.url}/`" class="btn btn-sm btn-outline-secondary me-3">More</nuxt-link>
                    <span class="badge bg-secondary rounded-pill">{{ i.created_at }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- {% endfor %} -->
        </div>
      </div>
      <!-- {% else %} -->
      <div v-else>
        <h3 class="text-center lead my-5">No posts yet ...</h3>
      </div>
      <!-- {% endif %} -->
    </section>
  </div>
</template>

<style></style>

<script>
import Carousel from "~/components/Carousel.vue";
import axios from "axios";
export default {
  name: "Index",
  components: {
    Carousel,
  },
  async asyncData({ params }) {
    const { data } = await axios.get("http://127.0.0.1:8000/api/posts/");
    return { posts: data.results };
  },
};
</script>

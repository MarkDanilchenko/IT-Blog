<template>
    <div>
        <Carousel />
        <section class="all-posts">
            <div class="mb-3 mt-5 text-center">
                <p class="lead"><b>Other #tags:</b></p>
                <div class="d-flex justify-content-center flex-wrap">
                    <!-- {% for i in common_tags %} -->
                    <div v-for="i in tags" :key="i.slug">
                        <nuxt-link :to="`/tags/${i.slug}/`" class="nav-link me-3">#{{ i.slug }}</nuxt-link>
                    </div>
                    <!-- {% endfor %} -->
                </div>
            </div>
            <div class="d-flex justify-content-center">
                <hr class="mb-4 mt-0" style="width: 50%" />
            </div>
            <!-- cards -->
            <!-- cards -->
            <!-- cards -->
            <div class="row d-flex justify-content-center">
                <!-- {% for i in page_obj %} -->
                <div class="col-md-4" v-for="i in posts" :key="i.url">
                    <div class="card mb-3 shadow">
                        <div class="d-flex flex-column align-items-center justify-content-end">
                            <img :src="`${i.image}`" class="img-fluid p-3 rounded" :alt="`${i.h1}`" :title="`${i.h1}`" />
                            <div class="card-body">
                                <h3 class="card-title text-center"><b>{{ i.h1 }}</b></h3>
                                <div class="card-text" v-html="i.description"></div>
                                <!-- {% for j in i.tag.all %} -->
                                <div class="d-flex flex-wrap">
                                    <div v-for="j in i.tag" :key="j">
                                        <nuxt-link :to="`/tags/${j}/`" class="badge bg-light rounded-pill nav-link me-1">#{{ j
                                        }}</nuxt-link>
                                    </div>
                                </div>
                                <!-- {% endfor %} -->
                                <div class="d-flex justify-content-between align-items-center mt-3">
                                    <nuxt-link :to="`/posts/${i.url}/`"
                                        class="btn btn-sm btn-outline-secondary">More</nuxt-link>
                                    <span class="badge bg-secondary rounded-pill">{{ i.created_at }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- {% endfor %} -->
            </div>
        </section>
    </div>
</template>

<script>
import axios from "axios";
import Carousel from "~/components/Carousel.vue";
export default {
    name: "PostByTag",
    components: {
        Carousel,
    },
    async asyncData({ params }) {
        const { data } = await axios.get(`http://127.0.0.1:8000/api/tags/${params.slug}/`);
        const tags = await axios.get(`http://127.0.0.1:8000/api/tags/`);
        return {
            posts: data.results,
            tags: tags.data
        }
    }
}
</script>
<template>
    <section class="my-postsByTag">
        <!-- Carousel -->
        <!-- Carousel -->
        <!-- Carousel -->
        <Carousel />
        <!-- Posts by tag -->
        <!-- Posts by tag -->
        <!-- Posts by tag -->
        <div class="all-posts">
            <div class="mb-3 mt-5 text-center">
                <!-- Other #tags row -->
                <!-- Other #tags row -->
                <!-- Other #tags row -->
                <p class="lead"><b>Other #tags:</b></p>
                <div class="d-flex justify-content-center flex-wrap">
                    <div v-for="i in tags" :key="i.slug">
                        <nuxt-link v-if="i.slug != $route.params.tag" :to="`/tags/${i.slug}/`"
                            class="nav-link me-3">#{{ i.slug }}</nuxt-link>
                        <nuxt-link v-if="i.slug == $route.params.tag" :to="`/tags/${i.slug}/`" class="nav-link me-3"
                            style="color: rgb(7, 151, 98) !important; font-weight: 700 !important;">#{{ i.slug
                            }}</nuxt-link>
                    </div>
                </div>
            </div>
            <div class="d-flex justify-content-center">
                <hr class="mb-4 mt-0" style="width: 50%" />
            </div>
            <!-- Post's details -->
            <!-- Post's details -->
            <!-- Post's details -->
            <div class="row d-flex justify-content-center">
                <div class="col-md-4" v-for="i in posts" :key="i.url">
                    <div class="card mb-3 shadow">
                        <div class="d-flex flex-column align-items-center justify-content-end">
                            <img :src="`${i.image}`" class="img-fluid p-3 rounded" :alt="`${i.h1}`"
                                :title="`${i.h1}`" />
                            <div class="card-body">
                                <h3 class="card-title text-center"><b>{{ i.h1 }}</b></h3>
                                <div class="card-text" v-html="i.description"></div>
                                <div class="d-flex flex-wrap">
                                    <div v-for="j in i.tag" :key="j">
                                        <nuxt-link :to="`/tags/${j}/`"
                                            class="badge bg-light rounded-pill nav-link me-1">#{{ j }}</nuxt-link>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-between align-items-center mt-3">
                                    <nuxt-link :to="`/posts/${i.url}/`"
                                        class="btn btn-sm btn-outline-secondary">More</nuxt-link>
                                    <span class="badge bg-secondary rounded-pill">{{ i.created_at }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Pagination -->
        <!-- Pagination -->
        <!-- Pagination -->
        <Pagination :pageRange="pageRange" :CLIENT_API_URL="CLIENT_API_URL" @changePage="posts = $event" class="mt-3" />
    </section>
</template>

<script>
import axios from "axios";
import Carousel from "@/components/Carousel.vue";
import Pagination from "@/components/Pagination.vue";
export default {
    name: "PostByTag",
    components: {
        Carousel,
        Pagination
    },
    async asyncData({ isDev, route, store, env, params, query, req, res, redirect, error }) {
        const { data } = await axios.get(`${process.env.API_URL}/api/posts/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            params: {
                tag: params.tag
            }
        });
        const tags = await axios.get(`${process.env.API_URL}/api/tags/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        });
        const pageRange = (data.results && data.results.length > 0) ? Math.ceil(data.count / data.results.length) : 1;
        return {
            posts: data.results,
            tags: tags.data,
            pageRange: pageRange,
            CLIENT_API_URL: `${process.env.API_URL}/api/posts/?tag=${params.tag}`,
        }
    }
}
</script>
<template>
    <section class="my-postSearch">
        <div class="row">
            <div class="col-10 offset-1">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">Search &#128270;</li>
                    </ol>
                </nav>
                <!-- Result search -->
                <!-- Result search -->
                <!-- Result search -->
                <div v-if="posts">
                    <p class="text-center lead mt-5">Posts found: {{ postsCount }}</p>
                    <div class="p-3">
                        <div v-for="i in posts" :key="i.url" class="mb-3 shadow-sm rounded-2 p-3">
                            <nuxt-link :to="`/posts/${i.url}/`" class="nav-link"><b>{{ i.h1 }}</b></nuxt-link>
                            <span class="text-muted text-small">Short description:</span>
                            <div v-html="i.description" class="text-start"></div>
                            <div class="d-flex justify-content-between text-muted text-small align-items-center">
                                <span class="text-center">Published: {{ i.created_at }}</span>
                                <span class="text-center">Author: {{ i.author }}</span>
                                <nuxt-link :to="`/posts/${i.url}/`" class="btn btn-sm btn-outline-success">Read
                                    more</nuxt-link>
                            </div>
                        </div>
                    </div>
                    <!-- Pagination -->
                    <!-- Pagination -->
                    <!-- Pagination -->
                    <Pagination :pageRange="pageRange" :CLIENT_API_URL="CLIENT_API_URL" @changePage="posts = $event"
                        class="mt-3" />
                </div>
                <!-- Empty search -->
                <!-- Empty search -->
                <!-- Empty search -->
                <div v-else class="postsNotFound text-center lead mt-5">Posts <span>
                        not found </span><br>&#128533;&#128533;&#128533;<br>Please, specify your request and try again.
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import Pagination from '@/components/Pagination.vue';
export default {
    name: "Search",
    components: {
        Pagination
    },
    // The `watchQuery: ["search"],` option in the Vue component is used to specify which query
    // parameters to watch for changes. In this case, it is watching for changes in the "search" query
    // parameter. When the "search" query parameter changes in the URL, the component will react and
    // update accordingly based on the new value of the "search" parameter. This allows the component
    // to dynamically fetch data based on the search query parameter in the URL.
    watchQuery: ["search"],
    async asyncData({ isDev, route, store, env, params, query, req, res, redirect, error }) {
        const { data } = await axios.get(`${process.env.API_URL}/api/search/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            params: {
                search: query.search,
            }
        });
        const pageRange = (data.results && data.results.length > 0) ? Math.ceil(data.count / data.results.length) : 1;
        return {
            posts: data.results,
            postsCount: data.count,
            pageRange: pageRange,
            CLIENT_API_URL: `${process.env.API_URL}/api/search/?search=${query.search}`,
        }
    },
}
</script>

<style scoped lang="scss">
@import "@/assets/scss/colors.scss";

.postsNotFound {
    font-size: 3rem;
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);

    span {
        color: $green_color;
    }
}
</style>
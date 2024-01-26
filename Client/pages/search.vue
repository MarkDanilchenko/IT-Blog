<template>
    <div class="my-post-detail">
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
                <!-- empty search result -->
                <!-- empty search result -->
                <!-- empty search result -->
                <div v-if="error" class="text-center lead mt-5">Posts found: 0<br><br>{{ error }}</div>
                <!-- search result -->
                <!-- search result -->
                <!-- search result -->
                <div v-else>
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
                        <div class="d-flex justify-content-center">
                            <hr style="width: 50%" />
                        </div>
                    </div>
                    <Pagination :pageRange="pageRange" :CLIENT_API_URL="CLIENT_API_URL" @changePage="posts = $event"  class="mt-3"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Pagination from '~/components/Pagination.vue';
export default {
    name: "Search",
    watchQuery: ["q"],
    components: {
        Pagination
    },
    async asyncData({ isDev, route, store, env, params, query, req, res, redirect, error }) {
        const { data } = await axios.get(`${process.env.API_URL}/api/search/?q=${encodeURIComponent(query.q)}`);
        const pageRange = (data.results && data.results.length > 0) ? Math.ceil(data.count / data.results.length) : 1;
        return {
            posts: data.results,
            postsCount: data.count,
            error: data.error,
            pageRange: pageRange,
            CLIENT_API_URL: `${process.env.API_URL}/api/search/`,
        }
    },
}
</script>
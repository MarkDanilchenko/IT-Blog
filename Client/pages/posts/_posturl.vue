<template>
    <section class="my-postDetails">
        <div class="row">
            <!-- Post detailes -->
            <!-- Post detailes -->
            <!-- Post detailes -->
            <div class="col-lg-8">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">Post: {{ post.h1 }}</li>
                    </ol>
                </nav>
                <!-- Post body -->
                <!-- Post body -->
                <!-- Post body -->
                <img :src="`${post.image}`" class="img-fluid rounded" :alt="`${post.h1}`" :title="`${post.h1}`" />
                <hr />
                <div class="text-center" v-html="post.content"></div>
                <div class="d-flex justify-content-end">
                    <div v-for="i in post.tag" :key="i">
                        <nuxt-link :to="`/tags/${i}/`" class="badge bg-light rounded-pill nav-link me-1">#{{ i
                            }}</nuxt-link>
                    </div>
                </div>
                <div class="d-flex justify-content-between mt-3">
                    <span>Author: <b>{{ post.author }}</b></span>
                    <span>Posted: <b>{{ post.created_at }}</b></span>
                </div>
                <hr />
                <!-- Comments' block -->
                <!-- Comments' block -->
                <!-- Comments' block -->
                <ClientOnly placeholder="Loading comments...">
                    <Comments :post="post.url" />
                </ClientOnly>
            </div>
            <!-- Sidebar with related posts -->
            <!-- Sidebar with related posts -->
            <!-- Sidebar with related posts -->
            <Sidebar :tags="tags" :asidedata="asidedata" class="col-lg-4" />
        </div>
    </section>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import Comments from "@/components/Comments.vue";
import axios from "axios";
export default {
    name: "PostDetail",
    components: {
        Sidebar,
        Comments
    },
    async asyncData({ isDev, route, store, env, params, query, req, res, redirect, error }) {
        const { data } = await axios.get(`${process.env.API_URL}/api/posts/${params.posturl}/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        const tags = await axios.get(`${process.env.API_URL}/api/tags/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        const asidedata = await axios.get(`${process.env.API_URL}/api/posts_aside/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            params: {
                exclude: data.url
            }
        })
        return {
            post: data,
            tags: tags.data,
            asidedata: asidedata.data,
        }
    },
}
</script>
<template>
    <!-- {% extends 'base.html' %} {% load static %} -->
    <!-- blokc title -->
    <!-- {% block title %}Post details{% endblock %} -->
    <!-- block content -->
    <!-- {% block content %} -->
    <section class="my-post-detail">
        <div class="row">
            <div class="col-lg-8">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">Post: <b>{{ post.h1 }}</b></li>
                    </ol>
                </nav>
                <!-- Post body -->
                <img :src="post.image" class="img-fluid rounded" :alt="`post.h1`" :title="`post.h1`" />
                <hr />
                <div class="text-center" v-html="post.content"></div>
                <div class="d-flex justify-content-end">
                    <!-- {% for i in post.tag.all %} -->
                    <div v-for="i in post.tag">
                        <nuxt-link :to="`/tags/${i}/`" class="badge bg-light rounded-pill nav-link me-1">#{{ i
                        }}</nuxt-link>
                    </div>
                    <!-- {% endfor %} -->
                </div>
                <div class="d-flex justify-content-between mt-3">
                    <span>Author: <b>{{ post.author }}</b></span>
                    <span>Posted: <b>{{ post.created_at }}</b></span>
                </div>
                <hr />
                <!-- Comment block -->
                <!-- {% include './blocks/comments.html' %} -->
                <Comments />
            </div>
            <!-- Sidebar -->
            <!-- {% include './blocks/sidebar.html' %} -->
            <Sidebar :tags="tags"/>
        </div>
    </section>
    <!-- {% endblock %} -->
</template>

<script>
import Sidebar from "~/components/Sidebar.vue";
import Comments from "~/components/Comments.vue";
import axios from "axios";
export default {
    name: "PostDetail",
    components: {
        Sidebar,
        Comments
    },
    async asyncData({ params }) {
        const post = await axios.get(`http://127.0.0.1:8000/api/posts/${params.url}/`);
        const tags = await axios.get(`http://127.0.0.1:8000/api/tags/`)
        // currentPostUrl - to exclude from the Sidebar
        // let currentPostUrl = post.data.url;
        // const { sidedata } = await axios.get(`http://127.0.0.1:8000/api/aside/${currentPostUrl}`)
        return {
            post: post.data,
            tags: tags.data,
            // sidedata: sidedata
        }
    },
}
</script>
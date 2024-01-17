<template>
    <!-- {% extends 'base.html' %} {% load static %} -->
    <!-- blokc title -->
    <!-- {% block title %}Search{% endblock %} -->
    <!-- block content -->
    <!-- {% block content %} -->
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
                <!-- {% if notFound %} -->
                <div v-if="notFound" class="text-center lead mt-5">Posts found: 0<br><br>{{ notFound }}</div>
                <!-- <p class="text-center lead">Posts found: 0<br />{{ notFound | safe }}</p> -->
                <div v-else-if="emptyQuery" class="text-center lead mt-5">Posts found: 0<br><br>{{ emptyQuery }}</div>
                <!-- {% else %} -->
                <div v-else>
                    <p class="text-center lead mt-5">Posts found: {{ postsCount }}</p>
                    <div class="p-3">
                        <!-- {% for i in page_obj %} -->
                        <div v-for="i in posts" :key="i.url" class="mb-3 shadow-sm rounded-2 p-3">
                            <nuxt-link :to="`/posts/${i.url}/`" class="nav-link"><b>{{ i.h1 }}</b></nuxt-link>
                            <span class="text-muted text-small">Short description:</span>
                            <div v-html="i.description" class="text-start"></div>
                            <div class="d-flex justify-content-between text-muted text-small align-items-center">
                                <span class="text-center">Published: {{ i.created_at }}</span>
                                <span class="text-center">Author: {{ i.author }}</span>
                                <nuxt-link :to="`/posts/${i.url}/`" class="btn btn-sm btn-outline-success">Read more</nuxt-link>
                            </div>
                        </div>
                        <div class="d-flex justify-content-center">
                            <hr style="width: 50%" />
                        </div>
                    </div>
                    <!-- {% endfor %} -->
                </div>
                <!-- {% endif %} -->
            </div>
        </div>
    </div>
    <!-- {% endblock %} -->
</template>

<script>
import axios from 'axios'
export default {
    name: "Search",
    watchQuery: ["q"],
    async asyncData({ query }) {
        const { data } = await axios.get(`http://127.0.0.1:8000/api/search/?q=${encodeURIComponent(query.q)}`);
        return {
            posts: data.results,
            postsCount: data.count,
            notFound: data.notFound,
            emptyQuery: data.emptyQuery
        }
    },
}
</script>
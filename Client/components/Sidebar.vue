<template>
    <!-- {% load static %} -->
    <div class="col-lg-4">
        <!-- Tags -->
        <div class="card my-3">
            <h5 class="card-header">Tags</h5>
            <div class="card-body">
                <div class="d-flex flex-wrap justify-content-end">
                    <!-- {% for i in common_tags %} -->
                    <div v-for="i in tags" :key="i.slug">
                        <nuxt-link :to="`/tags/${i.slug}/`" class="badge bg-light rounded-pill nav-link me-1 mb-1">#{{
                            i.slug }}</nuxt-link>
                    </div>
                    <!-- {% endfor %} -->
                </div>
            </div>
        </div>
        <!-- Last posts -->
        <div class="card my-3">
            <h5 class="card-header">View last posts</h5>
            <!-- {% for i in last_posts %} -->
            <div class="card-body pb-0 mb-3" v-for="(i, counter) in asidedata" :key="i.url">
                <nuxt-link :to="`/posts/${i.url}/`" class="nav-link text-center">
                    <h5 class="card-title">{{ i.h1 }}</h5>
                </nuxt-link>
                <img :src="`${i.image}`" :alt="`${i.h1}`" :title="`${i.h1}`" class="img-fluid rounded shadow mb-3" />
                <div v-html="i.description" class="text-center text-small"></div>
                <div class="d-flex justify-content-end">
                    <nuxt-link :to="`/posts/${i.url}/`" class="nav-link">Show more</nuxt-link>
                </div>
                <div v-if="counter < 2">
                    <hr class="mb-0" />
                </div>
            </div>
            <!-- {% if forloop.last %} -->
            <!-- <hr /> -->
            <!-- {% else %} -->
            <!-- <hr /> -->
            <!-- {% endif %} {% endfor %} -->
        </div>
    </div>
</template>

<script>
export default {
    name: "Sidebar",
    props: ['tags', 'asidedata',]
}
</script>
<template>
    <section class="my-sidebar">
        <!-- Tags -->
        <!-- Tags -->
        <!-- Tags -->
        <div class="card my-3">
            <h5 class="card-header">Tags</h5>
            <div class="card-body">
                <div class="d-flex flex-wrap justify-content-end">
                    <div v-for="i in tags" :key="i.slug">
                        <nuxt-link :to="`/tags/${i.slug}/`" class="badge bg-light rounded-pill nav-link me-1 mb-1">#{{
                        i.slug }}</nuxt-link>
                    </div>
                </div>
            </div>
        </div>
        <!-- Sidebar posts -->
        <!-- Sidebar posts -->
        <!-- Sidebar posts -->
        <div class="card my-3">
            <h5 class="card-header">Other posts</h5>
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
        </div>
    </section>
</template>

<script>
export default {
    name: "Sidebar",
    props: {
        tags: {
            type: Array
        },
        asidedata: {
            type: Array
        }
    }
}
</script>
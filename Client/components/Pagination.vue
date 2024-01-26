<template>
    <section class="my-pagination">
        <nav aria-label="Page navigation">
            <ul class="pagination d-flex justify-content-center">
                <li class="page-item" v-if="currentPage > 1">
                    <button class="page-link" aria-label="Previous" tabindex="-1" @click.prevent="changePage(prevPage)">
                        <span aria-hidden="true">&laquo;</span>
                    </button>
                </li>
                <li class="page-item disabled" v-else>
                    <nuxt-link class="page-link" to="#" aria-label="Previous" tabindex="-1">
                        <span aria-hidden="true">&laquo;</span>
                    </nuxt-link>
                </li>
                <div v-for="i in pageRange" :key="i">
                    <li v-if="currentPage == i" class="page-item active">
                        <button class="page-link" @click.prevent="changePage(i)">{{ i }}</button>
                    </li>
                    <li v-else class="page-item">
                        <button class="page-link" @click.prevent="changePage(i)">{{ i }}</button>
                    </li>
                </div>
                <li class="page-item" v-if="currentPage < pageRange">
                    <button class="page-link" aria-label="Next" tabindex="-1" @click.prevent="changePage(nextPage)">
                        <span aria-hidden="true">&raquo;</span>
                    </button>
                </li>
                <li class="page-item disabled" v-else>
                    <nuxt-link class="page-link" to="#" aria-label="Next" tabindex="-1">
                        <span aria-hidden="true">&raquo;</span>
                    </nuxt-link>
                </li>
            </ul>
        </nav>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: "Pagination",
    props: ['pageRange', 'CLIENT_API_URL'],
    methods: {
        async changePage(page) {
            // check, if query is from search.vue page with ?q=
            if (this.$route.query.q) {
                const { data } = await axios.get(`${this.CLIENT_API_URL}?q=${this.$route.query.q}&page=${page}`);
                this.$emit('changePage', data.results);
                this.$router.push(`?q=${this.$route.query.q}&page=${page}`);
            } else {
                const { data } = await axios.get(`${this.CLIENT_API_URL}?page=${page}`);
                this.$emit('changePage', data.results);
                this.$router.push(`?page=${page}`);
            }
        },
    },
    computed: {
        prevPage() {
            return Number(this.$route.query.page) - 1;
        },
        nextPage() {
            return this.$route.query.page ? Number(this.$route.query.page) + 1 : 2;
        },
        currentPage() {
            return this.$route.query.page ? Number(this.$route.query.page) : 1;
        }
    }
}
</script>
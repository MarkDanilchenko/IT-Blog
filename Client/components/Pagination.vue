<template>
    <section class="my-pagination">
        <nav aria-label="Page navigation">
            <ul class="pagination d-flex justify-content-center">
                <!-- {% if page_obj.has_previous %} -->
                <li class="page-item" v-if="currentPage > 1">
                    <button class="page-link" aria-label="Previous" tabindex="-1" @click.prevent="changePage(prevPage)">
                        <span aria-hidden="true">&laquo;</span>
                    </button>
                </li>
                <!-- {% else %} -->
                <li class="page-item disabled" v-else>
                    <nuxt-link class="page-link" to="#" aria-label="Previous" tabindex="-1">
                        <span aria-hidden="true">&laquo;</span>
                    </nuxt-link>
                </li>
                <!-- {% endif %}  -->
                <!-- {% for i in page_obj.paginator.page_range %} {% if page_obj.number == i %} -->
                <div v-for="i in pageRange" :key="i">
                    <li v-if="currentPage == i" class="page-item active">
                        <button class="page-link" @click.prevent="changePage(i)">{{ i }}</button>
                    </li>
                    <!-- <li class="page-item active">
                    <nuxt-link class="page-link" to="">-</nuxt-link>
                </li> -->
                    <!-- {% else %} -->
                    <li v-else class="page-item">
                        <button class="page-link" @click.prevent="changePage(i)">{{ i }}</button>
                    </li>
                </div>
                <!-- <li class="page-item">
                    <nuxt-link class="page-link" to="">-</nuxt-link>
                </li> -->
                <!-- {% endif %} {% endfor %}  -->
                <!-- {% if page_obj.has_next %} -->
                <li class="page-item" v-if="currentPage < pageRange">
                    <button class="page-link" aria-label="Next" tabindex="-1" @click.prevent="changePage(nextPage)">
                        <span aria-hidden="true">&raquo;</span>
                    </button>
                </li>
                <!-- {% else %} -->
                <li class="page-item disabled" v-else>
                    <nuxt-link class="page-link" to="#" aria-label="Next" tabindex="-1">
                        <span aria-hidden="true">&raquo;</span>
                    </nuxt-link>
                </li>
                <!-- {% endif %} -->
            </ul>
        </nav>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: "Pagination",
    props: ['pageRange', 'APIURL'],
    methods: {
        async changePage(page) {
            // check, if query is from search.vue page with ?q= parametr
            if (this.$route.query.q) {
                const { data } = await axios.get(`${this.APIURL}?q=${this.$route.query.q}&page=${page}`);
                this.$emit('changePage', data.results);
                this.$router.push(`?q=${this.$route.query.q}&page=${page}`);
            } else {
                const { data } = await axios.get(`${this.APIURL}?page=${page}`);
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
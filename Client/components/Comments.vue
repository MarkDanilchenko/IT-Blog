<template>
    <div>
        <!-- {% load static %} {% load crispy_forms_tags %} -->
        <!-- Comment block -->
        <div class="card mb-3 mt-5">
            <h5 class="card-header">Enter Your comment:</h5>
            <div class="card-body">
                <!-- {% if user.is_authenticated %} -->
                <div v-if="$auth.user">
                    <form>
                        <!-- {% csrf_token %} -->
                        <div class="form-group">
                            <textarea class="form-control" name="comment" id="comment" rows="5" cols="30"
                                placeholder="Your comment up to 1000 symbols." v-model="comment" required=""></textarea>
                        </div>
                        <button type="submit" class="btn btn-outline-success btn-sm mt-3" @click.prevent="submitCommentForm"
                            :disabled="!comment"> Comment!</button>
                    </form>
                </div>
                <!-- {% else %} -->
                <div v-else>
                    <h5 class="text-center lead">
                        Please,
                        <nuxt-link class="nav-link" to="/accounts/signin/">sign in</nuxt-link> or
                        <nuxt-link class="nav-link" to="/accounts/signup/">sign up</nuxt-link> to leave comments...
                    </h5>
                </div>
                <!-- {% endif %} -->
            </div>
        </div>
        <!-- Discussion (Users' comments) -->
        <!-- <div class="d-flex flex-column justify-content-center align-items-center my-4">
            <hr style="width: 50%" />
        </div> -->
        <!-- {% if post.post_comments.all %} -->
        <div class="card" v-if="postComments.length">
            <h5 class="card-header">Comments:</h5>
            <div class="card-body">
                <!-- {% if post.post_comments.all %} {% for i in post.post_comments.all %} -->
                <div class="d-flex col-10 offset-1 border-bottom border-end border-1 rounded rounded-2 shadow-sm mb-1 p-3"
                    v-for="(i, counter) in postComments" :key="i.id">
                    <div class="flex-shrink-0">
                        <img :src="``" class="rounded-circle" :alt="``" :title="``" />
                    </div>
                    <div class="flex-grow-1">
                        <div class="d-flex justify-content-between text-small text-muted">
                            <span class="me-3">&#128100; &nbsp;&nbsp;{{ i.user }}</span>
                            <span>&#128197; &nbsp;&nbsp;{{ i.created_at }}</span>
                        </div>
                        <div v-if="counter % 2 === 0">
                            <p class="text-end my-1 pe-5">{{ i.text }}</p>
                        </div>
                        <div v-else>
                            <p class="text-start my-1 ps-5">{{ i.text }}</p>
                        </div>
                    </div>
                </div>
                <!-- {% endfor %} {% endif %} -->
            </div>
        </div>
        <!-- {% else %} -->
        <div v-else class="mt-5">
            <h5 class="text-center lead"><b>No comments yet ...</b></h5>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center mt-4 mb-2">
            <hr style="width: 50%" />
        </div>
        <!-- {% endif %} -->

        <!-- Toast -->
        <div v-if="this.$auth.user" class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="5000">
                <div class="toast-header">
                    <strong class="me-auto">{{ this.$auth.user.username }}</strong>
                    <small class="text-body-secondary">&#60; 1 min ago</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Comments",
    props: ['postComments', 'post'],
    data() {
        return {
            comment: '',
        }
    },
    methods: {
        async submitCommentForm() {
            try {
                let response = await axios.post('http://127.0.0.1:8000/api/comments/', {
                    post: this.post.title,
                    text: this.comment,
                }, {
                    headers: {
                        Authorization: `Bearer ${this.$auth.strategy.token.get().split(' ')[1]}`
                    }
                });
                console.log(response.data.message);
                this.comment = '';
                // `this.postComments.unshift(response.data.comment_created_data)` is adding the newly
                // created comment to the beginning of the props `postComments` array.
                this.postComments.unshift(response.data.comment_created_data);

                // Toast appearance
                const { Toast } = await import('bootstrap');
                const toastLiveExample = document.getElementById('liveToast');
                let commentForToast = response.data.comment_created_data.text;
                toastLiveExample.querySelector('.toast-body').innerHTML = commentForToast;
                const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample);
                toastBootstrap.show();
            } catch (e) {
                console.log(e.message);
            }
        }
    },
}
</script>



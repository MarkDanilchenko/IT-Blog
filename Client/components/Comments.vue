<template>
    <div>
        <!-- Put a Comment block -->
        <!-- Put a Comment block -->
        <!-- Put a Comment block -->
        <div class="card mb-3 mt-5">
            <h5 class="card-header">Enter Your comment:</h5>
            <div class="card-body">
                <div v-if="$auth.user">
                    <form>
                        <div class="form-group">
                            <textarea class="form-control" name="comment" id="comment" rows="5" cols="30"
                                placeholder="Your comment up to 1000 symbols." v-model="comment"
                                @input="$v.comment.$touch()"></textarea>
                            <div v-if="!$v.comment.required">
                                <span class="text-small text-secondary">Leave your comment up to 1000 symbols.</span>
                            </div>
                            <div v-if="!$v.comment.maxLength">
                                <span class="text-small text-danger">Comment should not exceed 1000 symbols.</span>
                            </div>
                        </div>
                        <button type="submit" class="btn btn-outline-success btn-sm mt-3" @click.prevent="submitCommentForm"
                            :disabled="commentFilled"> Comment!</button>
                    </form>
                </div>
                <div v-else>
                    <h5 class="text-center lead">
                        Please,
                        <nuxt-link class="nav-link" to="/accounts/signin/">sign in</nuxt-link> or
                        <nuxt-link class="nav-link" to="/accounts/signup/">sign up</nuxt-link> to leave comments...
                    </h5>
                </div>
            </div>
        </div>
        <!-- Browse Comments block -->
        <!-- Browse Comments block -->
        <!-- Browse Comments block -->
        <div class="card" v-if="postComments.length">
            <h5 class="card-header">Comments:</h5>
            <div class="card-body">
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
            </div>
        </div>
        <div v-else class="mt-5">
            <h5 class="text-center lead"><b>No comments yet ...</b></h5>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center mt-4 mb-2">
            <hr style="width: 50%" />
        </div>

        <!-- Toast -->
        <!-- Toast -->
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
import { required, maxLength } from 'vuelidate/lib/validators'
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
                let response = await axios.post(`${process.env.API_URL}/api/comments/`, {
                    post: this.post.title,
                    text: this.comment,
                }, {
                    headers: {
                        Authorization: `Bearer ${this.$auth.strategy.token.get().split(' ')[1]}`
                    }
                });
                this.comment = '';
                // `this.postComments.unshift(response.data.comment_created_data)` is adding the newly
                // created comment to the beginning of the props `postComments` array.
                this.postComments.unshift(response.data.comment_created_data);

                // Toast appearance.
                const { Toast } = await import('bootstrap');
                const toastLiveExample = document.getElementById('liveToast');
                let commentForToast = response.data.comment_created_data.text;
                toastLiveExample.querySelector('.toast-body').innerHTML = commentForToast;
                const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample);
                toastBootstrap.show();
            } catch (e) {
                alert(e.message);
            }
        }
    },
    computed: {
        commentFilled() {
            return this.$v.comment.$invalid || this.comment == '' ? true : false
        }
    },
    validations: {
        comment: {
            required,
            maxLength: maxLength(1000)
        }
    }
}
</script>
<template>
    <section class="my-comments">
        <!-- Create Comment block -->
        <!-- Create Comment block -->
        <!-- Create Comment block -->
        <div class="card mb-3 mt-5">
            <h5 class="card-header">Enter Your comment:</h5>
            <div class="card-body">
                <div v-if="$auth.user">
                    <form id="commentForm" name="commentForm">
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
                        <button type="submit" class="btn btn-outline-success btn-sm mt-3"
                            @click.prevent="submitCommentForm" :disabled="commentFilled"> Comment!</button>
                    </form>
                </div>
                <div v-else>
                    <h5 class="text-center lead">
                        <nuxt-link class="nav-link" to="/accounts/signin/"><b>SignIn</b></nuxt-link> <span
                            class="text-small">to leave comments.</span>
                        <br><br>
                        <nuxt-link class="nav-link" to="/accounts/signup/"><b>SignUp</b></nuxt-link> <span
                            class="text-small">to create an account.</span>
                    </h5>
                </div>
            </div>
        </div>
        <!-- Browse Comments block -->
        <!-- Browse Comments block -->
        <!-- Browse Comments block -->
        <div v-if="postComments.length > 0" class="card">
            <h5 class="card-header">Comments:</h5>
            <div class="card-body">
                <div class="d-flex flex-column col-10 offset-1 border-bottom border-end border-1 rounded rounded-2 shadow-sm mb-3 p-3"
                    v-for="i in postComments" :key="i.id">
                    <div class="d-flex justify-content-between text-small text-muted">
                        <span class="me-3">&#128100; &nbsp;&nbsp;{{ i.user }}</span>
                        <span>&#128197; &nbsp;&nbsp;{{ i.created_at }}</span>
                    </div>
                    <div>
                        <p class="text-start my-1 pe-5">{{ i.text }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="mt-5">
            <h5 class="text-center lead"><b>No comments for this post yet...</b></h5>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center mt-4 mb-2">
            <hr style="width: 50%" />
        </div>
        <!-- Toast -->
        <!-- Toast -->
        <!-- Toast -->
        <div v-if="this.$auth.user" class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true"
                data-bs-delay="5000">
                <div class="toast-header">
                    <strong class="me-auto">{{ this.$auth.user.username }}</strong>
                    <small class="text-body-secondary">&#60; 1 min ago</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body"></div>
            </div>
        </div>
    </section>
</template>

<script>
import { maxLength, minLength, required, helpers } from 'vuelidate/lib/validators';
import axios from "axios";
export default {
    name: "Comments",
    props: {
        post: {
            type: String,
            default: () => ''
        }
    },
    data() {
        return {
            comment: '',
            postComments: [],
        }
    },
    validations: {
        comment: {
            required,
            maxLength: maxLength(1000)
        }
    },
    computed: {
        commentFilled() {
            return this.$v.comment.$invalid || this.comment == '' ? true : false
        }
    },
    mounted() {
        axios.get(`${process.env.API_URL}/api/comments/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            params: {
                post: this.post
            }
        }).then((response) => {
            this.postComments = [...response.data]
        }).catch((error) => {
            this.postComments = [];
            console.log(error.message);
        })
    },
    methods: {
        async submitCommentForm() {
            await axios.post(`${process.env.API_URL}/api/comments/`,
                {
                    post: this.post,
                    text: this.comment
                },
                {
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${this.$auth.strategy.token.get().split(' ')[1]}`
                    },

                }).then((response) => {
                    this.postComments.unshift(response.data.comment_details);
                    // const Toast = bootstrap.Toast;
                    const toastLiveExample = document.getElementById('liveToast');
                    let commentForToast = response.data.comment_details.text;
                    toastLiveExample.getElementsByClassName('toast-body').innerHTML = commentForToast;
                    const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample);
                    toastBootstrap.show();
                }).catch((error) => {
                    console.log(error.message)
                }).finally(() => {
                    this.comment = '';
                });
        }
    },
}


// import Toast from bootstrap:
// const toastLiveExample = document.getElementById('liveToast');
// let commentForToast = response.data.comment_details.text;
// toastLiveExample.getElementsByClassName('toast-body').innerHTML = commentForToast;
// const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample);
// toastBootstrap.show();
</script>

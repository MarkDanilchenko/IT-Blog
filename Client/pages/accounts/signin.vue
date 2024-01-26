<template>
    <div class="mt-3 row">
        <div class="d-flex flex-column align-items-center">
            <nav aria-label="breadcrumb" class="my-3">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item">
                        <nuxt-link to="/">Main</nuxt-link>
                    </li>
                    <li class="breadcrumb-item active" aria-current="page">Sign in</li>
                </ol>
            </nav>
            <form class="col-lg-4 col-6" enctype="multipart/form-data" id="form-signIn" name="form-signIn"
                @submit.prevent="signIn">
                <fieldset class="form-group">
                    <nuxt-link to="/" class="d-flex align-items-center justify-content-center mb-3">
                        <img src="/favicon/favicon_lg.png" width="50" height="50" alt="Home page logo" title="Home page" />
                    </nuxt-link>
                    <legend class="border-bottom mb-4 text-center"><b>Sign in</b></legend>
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" name="username" id="username" class="form-control" placeholder="Username"
                            aria-describedby="usernameHelp" v-model="form.username" required="">
                        <div id="usernameHelp" class="form-text text-small">Enter your username.</div>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" name="password" id="password" class="form-control" placeholder="Password"
                            aria-describedby="passwordHelp" v-model="form.password" required="">
                        <div id="passwordHelp" class="form-text text-small">Enter your password.</div>
                    </div>
                </fieldset>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-outline-success">Sign in!</button>
                </div>
            </form>
            <p class="text-danger mt-3" v-if="error">{{ error }}</p>
            <p class="text-center text-secondary mt-3" style="font-size: smaller">
                <i>After a successful authentication<br /> - redirected to home page.</i>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: "Signin",
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
            error: null
        };
    },
    methods: {
        async signIn() {
            await this.$auth.loginWith('local', {
                data: this.form
            }).catch((e) => {
                this.error = e.response.data.detail
            });
        }
    },
    mounted() {
        document.getElementById('form-signIn').username.focus();
    }
}
</script>
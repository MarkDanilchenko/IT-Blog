<template>
    <!-- {% extends 'base.html' %} {% load static %} {% block title %}Sign up{% endblock %} {% block content %} -->
    <div class="mt-3 row">
        <!-- {% load crispy_forms_tags %} -->
        <div class="d-flex flex-column align-items-center">
            <nav aria-label="breadcrumb" class="my-3">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item">
                        <nuxt-link to="/">Main</nuxt-link>
                    </li>
                    <li class="breadcrumb-item active" aria-current="page">Sign up</li>
                </ol>
            </nav>
            <form class="col-lg-4" id="form-signUp" name="form-signUp" @submit.prevent="signUp">
                <!-- {% csrf_token %} -->
                <fieldset class="form-group mb-3">
                    <nuxt-link to="/" class="d-flex align-items-center justify-content-center mb-3">
                        <img src="/favicon/favicon_lg.png" width="50" height="50" alt="Home page logo" title="Home page" />
                    </nuxt-link>
                    <legend class="border-bottom mb-4 text-center"><b>Sign up</b></legend>
                    <!-- {{ form | crispy }} -->
                    <div class="mb-3">
                        <label for="username" class="form-label">Username *</label>
                        <input type="text" name="username" id="username" class="form-control" placeholder="Username"
                            aria-describedby="usernameHelp" v-model="form.username">
                        <div id="usernameHelp" class="form-text text-small">150 characters or fewer. Letters,
                            digits and @/./+/-/_ only. <br>Required.</div>
                    </div>
                    <div class="mb-3">
                        <label for="first_name" class="form-label">First name</label>
                        <input type="text" name="first_name" id="first_name" class="form-control" placeholder="First name"
                            aria-describedby="first_nameHelp" v-model="form.first_name">
                        <div id="first_nameHelp" class="form-text text-small">Your first name.</div>
                    </div>
                    <div class="mb-3">
                        <label for="last_name" class="form-label">Last name</label>
                        <input type="text" name="last_name" id="last_name" class="form-control" placeholder="Last name"
                            aria-describedby="last_nameHelp" v-model="form.last_name">
                        <div id="last_nameHelp" class="form-text text-small">Your last name.</div>
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email address *</label>
                        <input type="email" name="email" id="email" class="form-control" placeholder="Email address"
                            aria-describedby="emailHelp" v-model="form.email">
                        <div id="emailHelp" class="form-text text-small">Enter a valid email address. <br>Required.</div>
                    </div>
                    <div class="mb-3">
                        <label for="phone" class="form-label">Phone number</label>
                        <input type="text" name="phone" id="phone" class="form-control" placeholder="Phone number"
                            aria-describedby="phoneHelp" v-model="form.phone">
                        <div id="phoneHelp" class="form-text text-small">Phone number must contain only 11 digits<br> in
                            format _(___)___-__-__.</div>
                    </div>
                    <div class="mb-3">
                        <label for="password1" class="form-label">Password *</label>
                        <input type="password" name="password1" id="password1" class="form-control" placeholder="Password"
                            aria-describedby="passwordHelp" v-model="form.password1">
                        <div id="passwordHelp" class="form-text text-small">Enter a valid password. <br>Required.</div>
                    </div>
                    <div class="mb-3">
                        <label for="password2" class="form-label">Password confirmation *</label>
                        <input type="password" name="password2" id="password2" class="form-control" placeholder="Password"
                            aria-describedby="password2Help" v-model="form.password2">
                        <div id="password2Help" class="form-text text-small">Confirm your password. <br>Required.</div>
                    </div>
                </fieldset>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-outline-success">Sign up!</button>
                </div>
                <p class="text-center text-secondary mt-3" style="font-size: smaller">
                    <i>After a successful registration<br />
                        - redirected to home page.</i>
                </p>
                <div class="text-end">
                    <small class="text-muted">
                        Already registered? <nuxt-link class="nav-link" to="/" title="Log in!"><b>Log
                                in!</b></nuxt-link>
                    </small>
                </div>
            </form>
        </div>
    </div>
    <!-- {% endblock %} -->
</template>

<script>
export default {
    name: "Signup",
    data() {
        return {
            form: {
                username: '',
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                password1: '',
                password2: '',
            }
        }
    },
}
</script>
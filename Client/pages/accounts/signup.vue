<template>
    <section class="my-signUp">
        <div class="mt-3 row">
            <div class="d-flex flex-column align-items-center">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">SignUp</li>
                    </ol>
                </nav>
                <!-- SignUp form -->
                <!-- SignUp form -->
                <!-- SignUp form -->
                <form class="col-lg-4 col-6" id="form-signUp" name="form-signUp">
                    <fieldset class="form-group mb-3">
                        <nuxt-link to="/" class="d-flex align-items-center justify-content-center mb-3">
                            <img src="/favicon/favicon_lg.png" width="50" height="50" alt="Home page logo"
                                title="Home page" />
                        </nuxt-link>
                        <legend class="border-bottom mb-4 text-center"><b>Sign up</b>
                        </legend>
                        <div class="mb-3">
                            <label for="username" class="form-label">Username *</label>
                            <input type="text" name="username" id="username" class="form-control" placeholder="Username"
                                aria-describedby="usernameHelp" v-model="form.username"
                                @input="$v.form.username.$touch()">
                            <div v-if="!$v.form.username.required">
                                <span class="text-small text-secondary">This field is required.</span>
                            </div>
                            <div v-if="!$v.form.username.maxLength">
                                <span class="text-small text-danger">Username should not exceed 100 symbols.</span>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="first_name" class="form-label">First name</label>
                            <input type="text" name="first_name" id="first_name" class="form-control"
                                placeholder="First name" aria-describedby="first_nameHelp" v-model="form.first_name"
                                @input="$v.form.first_name.$touch()">
                            <div v-if="!$v.form.first_name.onlyLetters">
                                <span class="text-small text-danger">First name should not contain any symbols except
                                    letters.</span>
                            </div>
                            <div v-else class="text-small text-secondary">Your first name.</div>
                        </div>
                        <div class="mb-3">
                            <label for="last_name" class="form-label">Last name</label>
                            <input type="text" name="last_name" id="last_name" class="form-control"
                                placeholder="Last name" aria-describedby="last_nameHelp" v-model="form.last_name"
                                @input="$v.form.last_name.$touch()">
                            <div v-if="!$v.form.last_name.onlyLetters">
                                <span class="text-small text-danger">Last name should not contain any symbols except
                                    letters.</span>
                            </div>
                            <div v-else class="text-small text-secondary">Your last name.</div>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email address *</label>
                            <input type="email" name="email" id="email" class="form-control" placeholder="Email address"
                                aria-describedby="emailHelp" v-model="form.email" @input.="$v.form.email.$touch()">
                            <div v-if="!$v.form.email.required">
                                <span class="text-small text-secondary">This field is required.</span>
                            </div>
                            <div v-if="!$v.form.email.email">
                                <span class="text-small text-danger">Enter a valid email address.</span>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="phone" class="form-label">Phone number</label>
                            <input type="text" name="phone" id="phone" class="form-control" placeholder="Phone number"
                                aria-describedby="phoneHelp" v-model="form.phone" @input="$v.form.phone.$touch()">
                            <div v-if="!$v.form.phone.validatePhone">
                                <span class="text-small text-danger">Phone number must contain only 11
                                    digits<br> in format _(___)___-__-__.</span>
                            </div>
                            <div v-else class="text-small text-secondary">Your phone nubmer <br> in format:
                                _(___)___-__-__</div>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password *</label>
                            <input type="password" name="password" id="password" class="form-control"
                                placeholder="Password" aria-describedby="passwordHelp" v-model="form.password"
                                @input="$v.form.password.$touch()">
                            <div v-if="!$v.form.password.required">
                                <span class="text-small text-secondary">This field is required.</span>
                                <ul class="text-small text-secondary ps-3 mt-1">
                                    <li>At least <b>8 characters</b>;</li>
                                    <li>At least <b>one digit</b>;</li>
                                    <li>At least <b>one uppercase</b> character;</li>
                                    <li>At least <b>one lowercase</b> character;</li>
                                    <li>At least <b>one special</b> character:<br> [!#$%&?_-" ]</li>
                                </ul>
                            </div>
                            <div v-if="!$v.form.password.validatePassword">
                                <ul class="text-small text-danger ps-3 mt-2">
                                    <li>At least <b>8 characters</b>;</li>
                                    <li>At least <b>one digit</b>;</li>
                                    <li>At least <b>one uppercase</b> character;</li>
                                    <li>At least <b>one lowercase</b> character;</li>
                                    <li>At least <b>one special</b> character:<br> [!#$%&?_-" ]</li>
                                </ul>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="password2" class="form-label">Password confirmation *</label>
                            <input type="password" name="password2" id="password2" class="form-control"
                                placeholder="Password" aria-describedby="password2Help" v-model="form.password2"
                                @input="$v.form.password2.$touch()">
                            <div v-if="!$v.form.password2.required">
                                <span class="text-small text-secondary">This field is required.</span>
                            </div>
                            <div v-if="!$v.form.password2.passwordEquality">
                                <span class="text-small text-danger">Passwords do not match!</span>
                            </div>
                        </div>
                    </fieldset>
                    <div class="d-flex justify-content-center">
                        <button type="submit" class="btn btn-outline-success" :disabled="formIsFilled"
                            @click.prevent="signUp">SignUp!</button>
                    </div>
                </form>
                <!-- Error -->
                <!-- Error -->
                <!-- Error -->
                <p class="text-danger mt-3" v-if="error">{{ error }}</p>
                <p class="text-center text-secondary mt-3" style="font-size: smaller">
                    <i>After a successful registration<br /> - redirected to home page.</i>
                </p>
                <div class="text-end mb-5">
                    <small class="text-muted">
                        Already registered? <nuxt-link class="nav-link" to="/accounts/signin/" title="SignIn">
                            <b>SignIn!</b></nuxt-link>
                    </small>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { required, maxLength, email, between, minLength, helpers, sameAs } from 'vuelidate/lib/validators';
const onlyLetters = (value) => !helpers.req(value) || helpers.regex('onlyLetters', /^\p{Letter}+$/gu)(value);
const validatePhone = (value) => !helpers.req(value) || helpers.regex('validatePhone', /\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}/)(value);
const validatePassword = (value) => !helpers.req(value) || helpers.regex('validatePassword', /^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&?_ \-"]).*$/)(value);
const passwordEquality = (value) => !helpers.req(value) || document.getElementById('form-signUp').password.value === value
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
                password: '',
                password2: '',
            },
            error: null
        }
    },
    validations: {
        form: {
            username: {
                required,
                maxLength: maxLength(150),
            },
            first_name: {
                onlyLetters
            },
            last_name: {
                onlyLetters
            },
            email: {
                required,
                email
            },
            phone: {
                validatePhone
            },
            password: {
                required,
                validatePassword
            },
            password2: {
                required,
                passwordEquality
            }
        }
    },
    mounted() {
        document.getElementById('form-signUp').username.focus();
    },
    computed: {
        formIsFilled() {
            return this.form.password != this.form.password2 || this.$v.form.$invalid ? true : false
        }
    },
    methods: {
        async signUp() {
            let signUpFormData = new FormData();
            signUpFormData.append('username', this.form.username);
            signUpFormData.append('first_name', this.form.first_name);
            signUpFormData.append('last_name', this.form.last_name);
            signUpFormData.append('email', this.form.email);
            signUpFormData.append('phone', this.form.phone);
            signUpFormData.append('password', this.form.password);
            await this.$axios.post(`${process.env.API_URL}/api/accounts/signup/`,
                signUpFormData,
                {
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    }
                })
                .then((response) => {
                    console.log(response.data.message);
                    this.$auth.loginWith('local', {
                        data: {
                            username: this.form.username,
                            password: this.form.password
                        }
                    })
                }).catch((error) => {
                    const errorParse = Object.entries(error.response.data);
                    this.error = errorParse.reduce((acc, curr) => acc + curr[0].toUpperCase() + ': ' + curr[1] + '\n', '');
                })
        }
    },
}
</script>
<template>
  <div class="row">
    <div class="col-lg-8 offset-lg-2 col-md-10 offset-md-1">
      <nav aria-label="breadcrumb" class="my-3">
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <nuxt-link to="/">Main</nuxt-link>
          </li>
          <li class="breadcrumb-item active" aria-current="page">Feedback</li>
        </ol>
      </nav>
      <p class="text-center lead mt-5">Have any questions or suggestions?<br>Feel free to leave us Your feedback:
      </p>
      <!-- {% if form.errors %} {% for field in form %} {% for error in field.errors %} -->
      <!-- <div class="alert alert-danger"> -->
      <!-- <strong>{{ error | escape }}</strong> -->
      <!-- </div> -->
      <!-- {% endfor %} {% endfor %} {% for error in form.non_field_errors %} -->
      <!-- <div class="alert alert-danger"> -->
      <!-- <strong>{{ error | escape }}</strong> -->
      <!-- </div> -->
      <!-- {% endfor %} {% endif %} -->
      <form name="feedback-form" id="feedback-form" class="col-10 offset-1 border border-2 rounded p-3 shadow">
        <!-- {% csrf_token %} -->
        <div class="row mb-3">
          <div class="col-6">
            <h3 class="lead">From</h3>
            <p>User: <b>{{ form.name }}</b><br>Email: <b>{{ form.email }}</b></p>
            <!-- <label for="name" class="form-label">Name:</label> -->
            <!-- {{ form.name }} -->
            <!-- <input type="text" name="name" id="name" class="form-control" placeholder="Your name" v-model="form.name"
              required=""> -->
          </div>
          <!-- <div class="col-6"> -->
          <!-- <label for="email" class="form-label">Email:</label> -->
          <!-- {{ form.email }} -->
          <!-- <input type="email" name="email" id="email" class="form-control" placeholder="Your email" v-model="form.email"
              required=""> -->
          <!-- </div> -->
        </div>
        <div class="row mb-3">
          <div class="col-12">
            <label for="theme" class="form-label">Theme:</label>
            <!-- {{ form.theme }} -->
            <input type="text" name="theme" id="theme" class="form-control" placeholder="Feedback theme"
              v-model="form.theme" @input="$v.form.theme.$touch()">
            <!-- <div v-if="$v.form.theme.$required" class="msg-error"><span>Theme is required.</span></div> -->
            <div v-if="!$v.form.theme.required">
              <span class="text-small text-secondary">This field is required.</span>
            </div>
            <div v-if="!$v.form.theme.maxLength">
              <span class="text-small text-danger">Theme should not exceed 150 symbols.</span>
            </div>
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-12">
            <label for="message" class="form-label">Message:</label>
            <!-- {{ form.message }} -->
            <textarea name="message" id="message" cols="30" rows="5" class="form-control"
              placeholder="Feedback up to 1000 symbols" v-model="form.message"
              @input="$v.form.message.$touch()"></textarea>
            <div v-if="!$v.form.message.required">
              <span class="text-small text-secondary">This field is required.</span>
            </div>
            <div v-if="!$v.form.message.maxLength">
              <span class="text-small text-danger">Feedback message should not exceed 1000 symbols.</span>
            </div>
            <!-- <div v-if="!$v.form.message.containLetter_a" class="msg-error">
              <span>Error A.</span>
            </div> -->
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" @click.prevent="submitFeedbackForm" :disabled="formIsFilled"
            class="btn btn-outline-success" id="submitFeedback__btn">Send!</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ENV from '~/assets/env.js';
import { required, maxLength, email, between, minLength, helpers } from 'vuelidate/lib/validators';
export default {
  name: "Feedback",
  data() {
    return {
      form: {
        name: this.$auth.user.username,
        email: this.$auth.user.email,
        theme: '',
        message: '',
        submitFeedbackFormStatus: null
      },
    }
  },
  methods: {
    submitFeedbackForm() {
      // if form check need to be done when submit btn clicked (instead of @input="..." on each input)
      // this.$v.$touch();
      if (this.$v.$invalid) {
        return
      } else {
        // submit btn modification after form submit
        this.submitFeedbackFormStatus = 'PENDING...';
        document.querySelector('#submitFeedback__btn').innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">${this.submitFeedbackFormStatus}</span>
        `;
        document.querySelector('#submitFeedback__btn').disabled = true;
        // submit form method after delay 2000ms
        setTimeout(() => {
          let feedbackFormData = new FormData();
          feedbackFormData.append('name', this.form.name);
          feedbackFormData.append('email', this.form.email);
          feedbackFormData.append('theme', this.form.theme);
          feedbackFormData.append('message', this.form.message);

          axios
            .post('http://127.0.0.1:8000/api/feedback/',
              feedbackFormData, {
              headers: {
                Authorization: `Bearer ${this.$auth.strategy.token.get().split(' ')[1]}`,
                'Content-Type': 'multipart/form-data'
              },
            }
            )
            .then((response) => {
              this.$router.push('/success/');
            })
            .catch((e) => {
              console.log(e)
            });
        }, 2000);
      }
    },
  },
  computed: {
    formIsFilled() {
      return this.$v.form.$invalid ? true : false
    }
  },
  validations: {
    form: {
      theme: {
        required,
        maxLength: maxLength(15),
      },
      message: {
        required,
        maxLength: maxLength(1000),
      }
    }
  }
};
</script>
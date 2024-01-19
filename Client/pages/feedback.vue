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
              v-model="form.theme" required="">
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-12">
            <label for="message" class="form-label">Message:</label>
            <!-- {{ form.message }} -->
            <textarea name="message" id="message" cols="30" rows="5" class="form-control"
              placeholder="Your feedback up to 1000 symbols." v-model="form.message" required=""></textarea>
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" @click.prevent="submitFeedbackForm" :disabled="!formIsFilled"
            class="btn btn-outline-success">Send!</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style></style>

<script>
import axios from "axios";
import ENV from '~/assets/env.js';
export default {
  name: "Feedback",
  data() {
    return {
      form: {
        name: this.$auth.user.username,
        email: this.$auth.user.email,
        theme: '',
        message: ''
      },
    }
  },
  methods: {
    submitFeedbackForm() {
      let feedbackFormData = new FormData();
      feedbackFormData.append('name', this.form.name);
      feedbackFormData.append('email', this.form.email);
      feedbackFormData.append('theme', this.form.theme);
      feedbackFormData.append('message', this.form.message);

      axios
        .post('http://127.0.0.1:8000/api/feedback/',
          // todo: detail: "Authentication credentials were not provided."
          // token: this.$auth.strategy.token.get().split(' ')[1],
          {data: JSON.stringify(Object.fromEntries(feedbackFormData))}
        )
        .then((response) => {
          this.$router.push('/success/');
        })
        .catch((error) => {
          alert('Feedback form submission error! Please, check the entered data and try again!');
        });
    },
  },
  computed: {
    formIsFilled() {
      return this.form.theme && this.form.message;
    }
  }
};
</script>
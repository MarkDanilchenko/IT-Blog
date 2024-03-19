<template>
  <section class="my-feedback">
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
        <!-- Feedback form -->
        <!-- Feedback form -->
        <!-- Feedback form -->
        <p class="text-center lead mt-5">Have any questions or suggestions?<br>Feel free to leave us Your feedback:
        </p>
        <form name="feedback-form" id="feedback-form" class="col-10 offset-1 border border-2 rounded p-3 shadow">
          <!-- Feedback from current SignedIn User -->
          <div class="row mb-3">
            <div class="col-12">
              <h3 class="lead">From</h3>
              <hr>
              <p>&#128100; - <b>{{ form.username }}</b><br>&#9993; - <b>{{ form.email }}</b></p>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12">
              <h3 class="lead">Feedback</h3>
              <hr>
              <label for="theme" class="form-label">Theme:</label>
              <input type="text" name="theme" id="theme" class="form-control" placeholder="Feedback theme"
                v-model="form.theme" @input="$v.form.theme.$touch()">
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
              <textarea name="message" id="message" cols="30" rows="5" class="form-control"
                placeholder="Feedback up to 1000 symbols" v-model="form.message"
                @input="$v.form.message.$touch()"></textarea>
              <div v-if="!$v.form.message.required">
                <span class="text-small text-secondary">This field is required.</span>
              </div>
              <div v-if="!$v.form.message.maxLength">
                <span class="text-small text-danger">Feedback message should not exceed 1000 symbols.</span>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button @click.prevent="submitFeedbackForm" :disabled="formIsFilled" class="btn btn-outline-success"
              id="submitFeedback__btn">Send!</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import { required, maxLength, email, between, minLength, helpers } from 'vuelidate/lib/validators';
export default {
  name: "Feedback",
  data() {
    return {
      form: {
        username: this.$auth.user ? this.$auth.user.profile.username : '',
        email: this.$auth.user ? this.$auth.user.profile.email : '',
        theme: '',
        message: '',
        submitFeedbackFormStatus: null
      },
    }
  },
  validations: {
    form: {
      theme: {
        required,
        maxLength: maxLength(150),
      },
      message: {
        required,
        maxLength: maxLength(1000),
      }
    }
  },
  computed: {
    formIsFilled() {
      return this.$v.form.$invalid ? true : false
    }
  },
  methods: {
    submitFeedbackForm() {
      // submitBtn (id="submitFeedback__btn") modification after form's submition
      this.submitFeedbackFormStatus = 'PENDING...';
      document.querySelector('#submitFeedback__btn').innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">${this.submitFeedbackFormStatus}</span>
        `;
      document.querySelector('#submitFeedback__btn').disabled = true;
      // submit form after delay == 2000ms
      setTimeout(() => {
        let feedbackFormData = new FormData();
        feedbackFormData.append('name', this.form.username);
        feedbackFormData.append('email', this.form.email);
        feedbackFormData.append('theme', this.form.theme);
        feedbackFormData.append('message', this.form.message);
        this.$axios.post(`${process.env.API_URL}/api/feedback/`, feedbackFormData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Accept: 'application/json',
            Authorization: `Bearer ${this.$auth.strategy.token.get()}`,
          },
        }).then((response) => {
          this.$router.push('/success/');
        }).catch((error) => {
          alert(error.response.data.error);
          window.location.reload();
        });
      }, 2000);
    },
  },
};
</script>
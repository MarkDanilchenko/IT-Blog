<template>
    <div>
        <!-- {% extends 'base.html' %} {% load static %} {% block title %}Feedback - Success{% endblock %} {% block content %} -->
        <div class="row">
            <div class="col-10 offset-1">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">Feedback</li>
                    </ol>
                </nav>
                <p class="text-center lead">Your request has been successfully sent! <br /><br>Thank you!</p>
            </div>
        </div>
        <!-- {% endblock %} -->

    </div>
</template>

<script>
export default {
    name: 'Success',
}
</script>
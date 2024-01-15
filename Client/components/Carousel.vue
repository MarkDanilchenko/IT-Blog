<template>
  <section class="my-carousel mt-3">
    <div
      class="carousel side"
      data-bs-ride="carousel"
      id="carouselExampleIndicators"
    >
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="carouselExampleIndicators"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="carouselExampleIndicators"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="carouselExampleIndicators"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5>Python 3.10.11</h5>
            <p>
              Backend is written in Python 3.10 with <br />Django and Django
              Rest Framework
            </p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5>NuxtJS</h5>
            <p>Frontend is written in JavaScript with <br />NuxtJS</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5>Bootstrap 5.3.2</h5>
            <p>HTML layout and CSS styles are based on Bootstrap.</p>
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </section>
</template>

<script>
export default {
  name: "Carousel",
};
</script>

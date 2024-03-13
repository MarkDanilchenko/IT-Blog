<template>
  <section class="my-carousel mt-3">
    <div class="carousel side" data-bs-ride="carousel" id="carouselExampleIndicators">
      <!-- <div class="carousel-indicators">
        <button type="button" data-bs-target="carouselExampleIndicators" data-bs-slide-to="0" class="active"
          aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="carouselExampleIndicators" data-bs-slide-to="1"
          aria-label="Slide 2"></button>
        <button type="button" data-bs-target="carouselExampleIndicators" data-bs-slide-to="2"
          aria-label="Slide 3"></button>
      </div> -->
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="mb-3">Python 3</h5>
            <p>
              API is builded on Python v3.10 with DRF.
            </p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="mb-3">NuxtJS 2</h5>
            <p>Frontend is builded on NuxtJS v2.15.</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="10000">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="mb-3">Bootstrap 5</h5>
            <p>HTML/CSS is buildeded on Bootstrap v5.3.</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next">
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

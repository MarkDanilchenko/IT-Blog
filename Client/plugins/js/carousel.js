const myCarousel = document.querySelector("#carouselExampleIndicators");
if (myCarousel) {
  const carousel = new bootstrap.Carousel(myCarousel, {
    interval: 10000,
  });
}

document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.cover-slide');
    let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'flex' : 'none';
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    showSlide(currentSlide); // Show the first slide
    setInterval(nextSlide, 5000); // Change slide every 5 seconds
});

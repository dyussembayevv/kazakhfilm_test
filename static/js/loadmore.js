document.addEventListener('DOMContentLoaded', function() {
    const loadMoreButton = document.getElementById('load-more');
    const gallery = document.getElementById('gallery');
    let offset = 10; // Initial offset

    // Load more functionality
    loadMoreButton.addEventListener('click', function () {
        fetch(`/load_more/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                data.films.forEach(film => {
                    const galleryItem = document.createElement('div');
                    galleryItem.classList.add('gallery-item');

                    const img = document.createElement('img');
                    img.src = film.poster;
                    img.alt = film.title;

                    const info = document.createElement('div');
                    info.classList.add('gallery-item-info');

                    const title = document.createElement('h3');
                    title.textContent = film.title;

                    info.appendChild(title);
                    galleryItem.appendChild(img);
                    galleryItem.appendChild(info);
                    gallery.appendChild(galleryItem);
                });
                offset += 10; // Increment offset for the next batch
            });
    });
});





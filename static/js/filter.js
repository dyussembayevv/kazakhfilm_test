document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const yearDropdown = document.getElementById('year-filter');
    const genreDropdown = document.getElementById('genre-filter');
    const filmCards = document.querySelectorAll('.film-card');

    function filterFilms() {
        const search_query = searchInput.value.toLowerCase();
        const selected_year = yearDropdown.value;
        const selected_genre = genreDropdown.value;

        filmCards.forEach(card => {
            const title = card.dataset.title.toLowerCase();
            const year = card.dataset.year;
            const genre = card.dataset.genre.toLowerCase();

            const matchesSearch = title.includes(search_query);
            const matchesYear = selected_year === 'all' || year === selected_year;
            const matchesGenre = selected_genre === 'all' || genre === selected_genre;

            if (matchesSearch && matchesYear && matchesGenre) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('input', filterFilms);
    yearDropdown.addEventListener('change', filterFilms);
    genreDropdown.addEventListener('change', filterFilms);
});

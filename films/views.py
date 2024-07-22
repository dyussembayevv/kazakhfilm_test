from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
import random

from .models import Film, BackstagePhoto


def index(request):
    films = Film.objects.all()[:10]  # Show the first 10 films initially
    random_films = Film.objects.all()[:5]
    random_film = random.choice(Film.objects.all())
    years = Film.objects.values_list('year', flat=True).distinct()
    genres = Film.objects.values_list('genre', flat=True).distinct()

    return render(request, 'films/index.html', {
        'films': films,
        'random_film': random_film,
        'random_films': random_films,
        'years': years,
        'genres': genres,
    })


def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    context = {
        'film': film,
    }
    return render(request, 'films/film_detail.html', context)


def load_more_films(request):
    offset = int(request.GET.get('offset', 0))
    films = Film.objects.all()[offset:offset + 10]
    film_data = [{
        'title': film.name,
        'poster': film.poster.url,
    } for film in films]

    return JsonResponse({'films': film_data})


def filter_films(request):
    search_query = request.GET.get('search', '').lower()
    selected_year = request.GET.get('year', '')
    selected_genre = request.GET.get('genre', '')

    films = Film.objects.all()

    if search_query:
        films = films.filter(title__icontains=search_query)

    if selected_year:
        films = films.filter(year=selected_year)

    if selected_genre:
        films = films.filter(genre__icontains=selected_genre)

    film_data = [{
        'name': film.name,
        'poster': film.poster.url,
    } for film in films]

    return JsonResponse({'films': film_data})
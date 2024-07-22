from django.contrib import admin
from .models import Film, BackstagePhoto


class BackstagePhotoInline(admin.TabularInline):
    model = BackstagePhoto
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    inlines = [BackstagePhotoInline]
    list_display = ('name', 'year', 'genre', 'director')
    search_fields = ('name', 'director')


admin.site.register(Film, FilmAdmin)
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['me before you', 'love rosie', 'casino']
    }
    return render(request, 'movies/index.html', context)

def fav_genre(request):
    return render(request, 'movies/fav_genre.html', {})

# app/templates/app/index.html
# movies/templates/movies/index.html

from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    movies = Movie.objects.all().order_by('-date')
    return render(request, 'home.html', {'movies': movies,'user':request.user})

def recommend(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.recommended_by = request.user
            movie.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'recommend.html', {'form': form})

def delete(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("/")

def fuckoff(request):
    return HttpResponse("Then fuck off")
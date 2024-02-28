from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Avg
from django.db.models import Q



def home(request):
    context = {}
    return render(request, 'movie_ratings/home.html', context)

def movie_list(request):
    search_query = request.GET.get('search')
    movies = Movie.objects.all()
    if search_query:
        movies = movies.filter(Q(title__icontains=search_query))
    context = {}
    if movies.exists():  # Check if any movies are found
        context['movies'] = movies
    else:
        context['no_movies'] = True
    return render(request, 'movie_ratings/movie_list.html', context)    


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    context = {
        'movie': movie,
        'reviews': reviews,
        'average_rating': average_rating
    }
    return render(request, 'movie_ratings/movie_detail.html', context)

@login_required
def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'movie_ratings/review_list.html', context)

@login_required
def post_review(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        
        existing_review = Review.objects.filter(user=request.user, movie=movie).exists()
        if existing_review:
            messages.error(request, "You have already reviewed this movie.")
            return redirect('app:movie_detail', pk=pk)

        review = Review(user=request.user, movie=movie, rating=request.POST['rating'], comment=request.POST['text'])
        review.save()

    return redirect('app:movie_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:home')  # corrected the redirect path
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST" and request.user.is_authenticated:
        # Provjeravamo je li trenutni korisnik autor recenzije
        if request.user == review.user:
            # Ako jest, ažuriramo recenziju
            review.rating = request.POST['rating']
            review.comment = request.POST['comment']
            review.save()
            messages.success(request, "Review updated successfully.")
        else:
            messages.error(request, "You are not the author of this review.")
    
    context = {
        'review': review
    }
    
    return render(request, 'movie_ratings/review_detail.html', context)



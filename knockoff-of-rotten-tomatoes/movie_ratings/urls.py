from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('<int:pk>/review/new/', views.post_review, name="post_review"),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
]
from django.contrib import admin
from django.urls import path, include
from movie_ratings.views import register
from movie_ratings import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_path'),
    path('movies/', include('movie_ratings.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
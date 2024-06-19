from django.urls import path
from funko_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.indexmovies, name='indexmovies'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('movies_rest/', views.movies_rest, name='movies_rest'),
    path('actors_rest/', views.actors_rest, name='actors_rest'),
    path('add_funko/', views.NewFunkoView.as_view(), name='add_funko'),
    path('add_user/', views.NewUserView.as_view(), name='add_user'),
    path('add_movie/', views.NewMovieView.as_view(), name='add_movie'),
    path('add_actor/', views.NewActorView.as_view(), name='add_actor'),

]
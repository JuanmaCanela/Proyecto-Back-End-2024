from django.shortcuts import render
from funko_api.models import Funko, User, Movie, Actor
from django.http import JsonResponse
from funko_api.serializers import FunkoSerializer, UserSerializer, MovieSerializer, ActorSerializer
from funko_api.forms import FunkoForm, UserForm, MovieForm, ActorForm
from django.views.generic import CreateView
# Create your views here.

def index(request):
  funkos = get_all_funkos()
  return render(request, 'index.html', {'funkos': funkos})

def get_all_funkos():
  funkos = Funko.objects.all().order_by('number')
  funkos_serializers = FunkoSerializer(funkos, many='True')
  return funkos_serializers.data

def funkos_rest(request):
  funkos = get_all_funkos()
  return JsonResponse(funkos, safe=False)

def get_all_users():
  users = User.objects.all().order_by('name')
  users_serializers = UserSerializer(users, many='True')
  return users_serializers.data

def users_rest(request):
  users = get_all_users()
  return JsonResponse(users, safe=False)

class NewFunkoView(CreateView):
    form_class = FunkoForm
    template_name = 'add_funko.html'
    success_url = '/'

class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'
    
#------------------------------------------------------------------------------

def indexmovies(request):
  movies = get_all_movies()
  return render(request, 'indexmovies.html', {'movies': movies})

def get_all_movies():
  movies = Movie.objects.all().order_by('title')
  movies_serializers = MovieSerializer(movies, many='True')
  return movies_serializers.data

def movies_rest(request):
  movies = get_all_movies()
  return JsonResponse(movies, safe=False)

def get_all_actors():
  actors = Actor.objects.all().order_by('name')
  actors_serializers = ActorSerializer(actors, many='True')
  return actors_serializers.data

def actors_rest(request):
  actors = get_all_actors()
  return JsonResponse(actors, safe=False)

class NewMovieView(CreateView):
    form_class = MovieForm
    template_name = 'add_movie.html'
    success_url = '/movies'

class NewActorView(CreateView):
    form_class = ActorForm
    template_name = 'add_actor.html'
    success_url = '/movies'
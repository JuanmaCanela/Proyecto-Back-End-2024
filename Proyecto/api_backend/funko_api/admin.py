from django.contrib import admin
from funko_api.models import Funko, User, Movie, Actor

# Register your models here.

admin.site.register(Funko)
admin.site.register(User)

#---------------------------------

admin.site.register(Movie)
admin.site.register(Actor)
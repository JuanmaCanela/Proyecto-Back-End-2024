from django import forms
from funko_api.models import Funko, User, Movie, Actor

class FunkoForm(forms.ModelForm):
    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'funkos',
        ]

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'director',
            'age',
            'genre',
        ]

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = [
            'name',
            'movies',
        ]
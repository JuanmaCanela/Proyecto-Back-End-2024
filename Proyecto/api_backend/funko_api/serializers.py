from rest_framework import serializers
from funko_api.models import Funko, User, Movie, Actor

class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        #fields = ['name', 'number', 'collection']
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#--------------------------------------------------------

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
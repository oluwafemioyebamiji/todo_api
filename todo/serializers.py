from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' 
        read_only_fields = ('id',)

class TodoFewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id","title","status")
        read_only_fields = ('id',)
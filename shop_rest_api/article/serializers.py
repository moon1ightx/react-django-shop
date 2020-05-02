from rest_framework import serializers
from .models import Category, Product, Comment
from myauth.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):	
	class Meta:
		model = Category
		fields = ('id', 'name')

class Productserializer(serializers.ModelSerializer):	
	category = CategorySerializer(read_only=True)
	class Meta:
		model = Product
		fields = ('id', 'title', 'description','price','sale', 'created_on','image', 'category')

class CommentSerializer(serializers.ModelSerializer):
	product=Productserializer(read_only=True)
	author=UserSerializer(read_only=True)
	class Meta:
		model=Comment
		fields=('id', 'product', 'body','author','created_on')
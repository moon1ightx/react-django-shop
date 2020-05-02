
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .models import Product, Category, Comment
from .serializers import Productserializer, CommentSerializer, CategorySerializer
from rest_framework.views import APIView, Response
from django.contrib.auth.models import User
from rest_framework import status

class ProductViews(APIView):
    serilizer_class = Productserializer
    def get(self, request, format=None):
        products = Product.objects.all()
        serilized = self.serilizer_class(products, many = True)
        return Response(serilized.data)

    def post(self, request, format=None):
        serilized = self.serilizer_class(data=request.data)
        if serilized.is_valid():
            product = Product(
            title=serilized.validated_data.get('title'),
            price=serilized.validated_data.get('price'),
            sale=serilized.validated_data.get('sale'),
            description = serilized.validated_data.get('description'),
            image=request.data.get("image"),
            category = Category.objects.get(pk = request.POST["category"]))
            product.save()
            response_serializer = self.serilizer_class(product)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serilized.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serilizer_class(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(pk=request.POST["id"])
            product.title=serializer.validated_data.get("title")
            product.price=serializer.validated_data.get('price')
            product.sale=serializer.validated_data.get('sale')
            product.image=request.data.get("image")
            product.description=serializer.validated_data.get("description") 
            product.category=Category.objects.get(pk=request.POST["category"])
            product.save()
            response_serializer = self.serilizer_class(product)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductView(APIView):
    serilizer_class = Productserializer
    def get(self, request, pk, format=None):
        product=  Product.objects.get(pk=pk)
        serilized = self.serilizer_class(product)
        return Response(serilized.data)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk).delete()
        return Response({'success': '1 product is deleted'}, status=200)


class CategoryViews(APIView):
    serilizer_class = CategorySerializer
    def get(self, request, format=None):
        categories = Category.objects.all()
        serilized = self.serilizer_class(categories, many = True)
        return Response(serilized.data)

    def post(self, request, format=None):
        serilized = self.serilizer_class(data=request.data)
        if serilized.is_valid():
            category = Category(name=serilized.validated_data.get('name'))
            category.save()
            response_serializer = self.serilizer_class(category)
            return Response(response_serializer.data)

class DeleteCategoryView(APIView):
    def delete(self, request, pk, format=None):
        category = Category.objects.get(pk=pk).delete()
        return Response({'success': '1 category is deleted'}, status=200)

class CommentViews(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serilizer_class = CommentSerializer

    def post(self, request, format=None):
        serialized = self.serilizer_class(data=request.data)
        if serialized.is_valid():
            comment = Comment(product= Product.objects.get(pk = request.POST["product"]),
            body = serialized.validated_data.get('body'), author=request.user)
            comment.save()
            response_serilizer = self.serilizer_class(comment)
            return Response(response_serilizer.data)
    def put(self, request, format=None):
        serialized = self.serilizer_class(data=request.data)
        if serialized.is_valid():
            comment = Comment.objects.get(pk=request.POST["id"])
            comment.body = serialized.validated_data.get('body') 
            comment.save()
            response_serilizer = self.serilizer_class(comment)
            return Response(response_serilizer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCommentView(APIView):
    serilizer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def delete(self, request, pk, format=None):
        comment = Comment.objects.get(pk=pk).delete()
        return Response({"success": "1 comment is deleted"}, status=200)
    def get(self, request,pk, format=None):
        comments = Comment.objects.filter(product=Product.objects.get(pk=pk))
        serialized = self.serilizer_class(comments, many = True)
        return Response(serialized.data)


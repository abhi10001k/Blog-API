from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Category,Post

from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer,PostSerializer


@api_view(['GET'])
def categoryList(request,format=None):
    category = Category.objects.all()
    serializer = CategorySerializer(category,many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def categoryAdd(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def categoryDelete(request,name):
    try:
        category = Category.objects.get(category=name)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])     
def postByCategory(request,name):
    posts = Post.objects.all().filter(category=name)
    if not posts:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
@api_view(['POST'])
def postAdd(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def postDetails(request,name):
    try:
        post = Post.objects.get(title=name)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post)
    return Response(serializer.data,status=status.HTTP_200_OK)


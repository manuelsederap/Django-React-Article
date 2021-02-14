from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(APIView):
    """List all Article or Create a new article"""

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    """Retrived, Update, Delete article instance"""

    def get(self, request, id, format=None):
        try:
            article = Article.objects.get(id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            response = ({'message': 'No data found...'})
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        article = Article.objects.get(id=id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        article = Article.objects.get(id=id)
        article.delete()
        response = ({'message': 'Sucessfully Deleted...'})
        return Response(response, status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET', 'POST'])
# def article_list(request):
#     """Create data or Get all data of article"""

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'GET', 'DELETE'])
# def article_details(request, pk):
#     """Update/Read/Delete the article"""

#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         response = ({'message': 'No data found...'})
#         return Response(response, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         response = ({'message': 'Sucessfully Deleted...'})
#         return Response(response, status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# class ArticleViewSet(viewsets.GenericViewSet,
#                         mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or creating Article.
#     """
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleList(generics.GenericAPIView,
#                     mixins.ListModelMixin,
#                     mixins.CreateModelMixin):
#     """Get and Create data using Generic and Mixin"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# # class ArticleList(APIView):
# #     """List all Article or Create a new article using class based view"""

# #     def get(self, request, format=None):
# #         articles = Article.objects.all()
# #         serializer = ArticleSerializer(articles, many=True)
# #         return Response(serializer.data)

# #     def post(self, request, format=None):
# #         serializer = ArticleSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetails(generics.GenericAPIView,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin):
#     """Retrive, Update, Delete data using Generic and Mixin"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request, id):
#         return self.destroy(request, id=id)

                
# class ArticleDetails(APIView):
#     """Retrived, Update, Delete article instance using class based view"""

#     def get(self, request, id, format=None):
#         try:
#             article = Article.objects.get(id=id)
#             serializer = ArticleSerializer(article)
#             return Response(serializer.data)
#         except Article.DoesNotExist:
#             response = ({'message': 'No data found...'})
#             return Response(response, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, id, format=None):
#         article = Article.objects.get(id=id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id, format=None):
#         article = Article.objects.get(id=id)
#         article.delete()
#         response = ({'message': 'Sucessfully Deleted...'})
#         return Response(response, status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET', 'POST'])
# def article_list(request):
#     """Create data or Get all data of article using function based"""

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
#     """Update/Read/Delete the article using function based"""

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

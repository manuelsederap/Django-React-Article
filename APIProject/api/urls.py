from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, UserViewSet
#from .views import ArticleList, ArticleDetails


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view()),
]

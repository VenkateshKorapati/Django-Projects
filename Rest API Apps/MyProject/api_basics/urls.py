from django.db import router
from django.urls import path, include
from api_basics import views
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', views.article_list ),
    path('article/', views.ArticleAPIView.as_view() ),
    path('detail/<int:id>/', views.ArticleDetailView.as_view() ),
    #path('detail/<int:pk>/', views.article_detail ),
    path('generic/article/<int:id>/', views.GenericAPIView.as_view() ),
]
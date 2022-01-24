from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.news_portal_view),
    path('Political/', views.political_news_view),
    path('Sports/', views.sports_news_view),
    path('Movies/', views.movies_news_view),
]

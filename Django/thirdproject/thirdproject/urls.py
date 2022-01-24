"""thirdproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('morning/',views.good_morning_view,name='good_morning_view' ),
    path('evening/',views.good_evening_view,name='good_evening_view' ),
    path('night/',views.good_night_view,name='good_night_view' ),
]

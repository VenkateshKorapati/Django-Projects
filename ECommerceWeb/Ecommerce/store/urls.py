from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('store/', views.store ,name='store'),
    path('cart/', views.cart ,name='cart'),
    path('checkout/', views.checkout ,name='checkout'),
    path('update_item/', views.updateItem ,name='update_item'),
    path('process_order/', views.processOrder ,name='process_order'),
    #registration
    path('signup', views.SignUp.as_view() ,name='signup'),
    path('login', auth_views.LoginView.as_view() ,name='login'),
    path('logout', auth_views.LogoutView.as_view() ,name='logout'),
]


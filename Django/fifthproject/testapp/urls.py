from django.urls import path
from testapp import views as v

urlpatterns = [
    path('first/',v.first_view,name='first_view' ),
    path('second/',v.second_view,name='second_view' ),
    path('third/',v.third_view,name='third_view' ),
    path('fourth/',v.fourth_view,name='fourth_view' ),
    path('fifth/',v.fifth_view,name='fifth_view' ),
]

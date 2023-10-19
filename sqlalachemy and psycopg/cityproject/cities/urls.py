from django.urls import path
from .views import create_city ,List_city

urlpatterns = [
    path('api/create_city/', create_city, name='create_city'),
    path('api/list/' ,List_city,name='list-city')
]
 
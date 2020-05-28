from django.urls import path
from . import views
urlpatterns = [
    path('',views.chome,name='chome'),
    path('home/',views.home,name='home')
]
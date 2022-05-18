from django.urls import path
from . import views


urlpatterns = [
    path('wish/', views.wish),
    path('server_time/', views.server_time),
    path('results/', views.results),
    path('wish_time/', views.wish_time),
]

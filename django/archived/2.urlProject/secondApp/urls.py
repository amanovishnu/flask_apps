from django.urls import path
from . import views

urlpatterns = [
    path('sixth/', views.sixth_view),
    path('seventh/', views.seventh_view),
    path('eighth/', views.eighth_view),
    path('ninth/', views.ninth_view),
    path('tenth/', views.tenth_view)
]

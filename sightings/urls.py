from django.urls import path
from . import views

urlpatterns = [
        path('', views.all_squirrels),
        path('<Unique_Squirrel_ID>/', views.details),
        ]


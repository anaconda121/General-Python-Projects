from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.index)
	path('update_task/<str:pk>/', views.update_task)
]
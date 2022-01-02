from django.urls import path
from app import views

urlpatterns = [
    path('post/', views.PostView.as_view(), name='post'),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('result/<str:pk>/', views.ResultDetailView.as_view(), name='result-detail'),
]
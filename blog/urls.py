from django.urls import path, include
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetails.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),]



from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('home/', views.index_view, name= 'index'),
]

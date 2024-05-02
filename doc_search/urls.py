from django.urls import path
from . import views
from .views import book_appointment

app_name = "doc_search"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='user_logout'),
    path("ov_appoint/", views.ov_appoint, name="ov_appoint"),
    path('book/', book_appointment, name='book_appointment'),
]
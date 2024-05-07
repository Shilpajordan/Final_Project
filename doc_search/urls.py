from django.urls import path
from . import views

app_name = "doc_search"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='user_logout'),
    path("ov_appoint/<str:doc_id>/", views.ov_appoint, name="ov_appoint"),
    path("detail_appoint/<int:patient_id>/", views.detail_appoint, name="detail_appoint"),
]

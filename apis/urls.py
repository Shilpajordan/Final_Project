from django.urls import path
from .views import HospitalCreateList, HospitalDetailsUpdateDelete

app_name = 'apis'

urlpatterns = [
    path('create/', HospitalCreateList.as_view(), name='create Hospitals'),
    path('create/<int:pk>', HospitalDetailsUpdateDelete.as_view(), name='Deails, Updates and Delete'),
]

from rest_framework import generics
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalCreateList(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalDetailsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

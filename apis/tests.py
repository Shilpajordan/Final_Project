from django.test import TestCase
from .models import Hospital

class HospitalModelTestCase(TestCase):

    def test_hospital_creation(self):
        hospital = Hospital.objects.create(
            name="Test Hospital",
            address="123 Test St, Testville",
            speciality="Gastroenterology",
            number_of_doctors=10,
            number_of_beds=50,
        )
        self.assertEqual(hospital.name, "Test Hospital")
        self.assertEqual(hospital.address, "123 Test St, Testville")
        self.assertEqual(hospital.speciality, "Gastroenterology")
        self.assertEqual(hospital.number_of_doctors, 10)
        self.assertEqual(hospital.number_of_beds, 50)

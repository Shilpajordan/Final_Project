from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Patient


class ResponseTest(TestCase):

    def test_call_view_home(self):
        '''
        Testing url response
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc_search/index.html')


class LoginTestCase(TestCase):
    '''
    Testing login and response of @login_required url
    '''
    def setUp(self):
        self.client = Client()
        # setting up a user in our empty test database
        self.user = User.objects.create_user('admin', 'xxx@xxx.com', '1234')
        # setting up a patient in our empty test database
        self.patient = Patient.objects.create(
            first_name="a",
            last_name="b",
            age=21,
            gender="male",
            email="xxx@xxx.com",
        )

    def test_call_view_ov_appoint(self):
        self.client.login(username='admin', password='1234')
        response = self.client.get('/ov_appoint/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc_search/ov_appoint.html')

    def test_call_view_detail_appoint(self):
        self.client.login(username='admin', password='1234')
        # retrieve test patient 1
        response = self.client.get('/detail_appoint/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc_search/detail_appoint.html')

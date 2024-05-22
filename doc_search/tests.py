from django.test import TestCase, Client
from django.contrib.auth.models import User


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

    def test_call_view_ov_appoint(self):
        self.client.login(username='admin', password='1234')
        response = self.client.get('/ov_appoint/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc_search/ov_appoint.html')

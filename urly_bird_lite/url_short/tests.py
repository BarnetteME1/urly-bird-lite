from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

# Create your tests here.
from url_short.models import UrlBank




class UrlModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='asdf')
        self.url = UrlBank.objects.create(user=self.user, url='https://github.com/BarnetteME1')

    def test_url_bites_length_is_equal_to_thirty_two(self):
        self.assertEqual(self.url.shorten_length, '9a53b27e80840b8208bc29b6644e1ce4')

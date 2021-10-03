import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.test import TestCase

from companies.models import Company


class CompanyManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(company_name="Consumer Affairs", email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(company_name='', email='normal@consumer.com', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(company_name="Consumer Affairs III",
                                                   email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                company_name='Consumer Affairs IV', email='super@user.com', password='foo', is_superuser=False)


class CompanyTestCase(APITestCase):
    def setUp(self):
        Company.objects.create_user(company_name="Consumer Affairs Endpoint duplicated", email='normal@user.com', password='foo')

    def test_registration_company(self):
        data = {
            "company_name": "Consumer Affairs Endpoint",
            "password": "12345"
        }
        response = self.client.post("/companies/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_company_with_duplicated_company_name(self):
        data = {
            "company_name": "Consumer Affairs Endpoint duplicated",
            "password": "12345"
        }
        response = self.client.post("/companies/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content),
            {"company_name": ["Company with this name already exists"]},
        )

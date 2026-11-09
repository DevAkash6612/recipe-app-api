from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    def setUp(self):
        """Create user and client for testing"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='akash@email.com',
            password='123456'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='akash11@email.com',
            password='123456',
            name='Akash')

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

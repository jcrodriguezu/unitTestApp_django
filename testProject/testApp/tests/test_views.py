from django.test import TestCase
from django.test import Client
from django.core.cache import caches

from testApp.views import index
from testApp.models import User


class ViewsTestCase(TestCase):
    fixtures = ['views_fixtures.json']

    def setUp(self):
        super(ViewsTestCase, self).setUp()
        self.user = User.objects.get(pk=1)
        caches['default'].set('user', self.user)
        self.client = Client()

    def test_index(self):
        request = self.client.get('/', follow=True)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context['username'], "test")
        self.assertEqual(request.context['privileges'].name, "USR")
        self.assertListEqual(list(request.context['user_books']), [])
        self.assertEqual(len(request.context['book_list']), 2)

    def test_logout(self):
        request = self.client.get('/logout', follow=True)
        u = caches['default'].get('user')
        self.assertEqual(u, None)

    def test_book_create(self):
        book_data = {'title': 'Book from unit test',
                     'author': 'author from unit test',
                     'num_pages': 10, 'num_copies': 3}
        request = self.client.post('/book_create', book_data, follow=True)
        self.assertEqual(len(request.context['book_list']), 3)
        self.assertTrue(True)

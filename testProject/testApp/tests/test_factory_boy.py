from django.test import TestCase
from testApp.tests import models_factory
from testApp.views import book_lend_logic


class BookLendFBTestCase(TestCase):

    def setUp(self):
        super(BookLendFBTestCase, self).setUp()
        self.user = models_factory.UserFactory()
        self.book1 = models_factory.BookFactory()

    def test_book_fb_lend_valid(self):
        print self.user
        print self.book1
        u = book_lend_logic(self.user, self.book1)
        self.assertTrue(u.books_lent.filter(id=self.book1.id).exists())

    def test_book_fb_lend_fail(self):
        u = book_lend_logic(self.user, self.book1)

        with self.assertRaises(Exception) as e:
            book_lend_logic(self.user, self.book1)
        self.assertEqual(
            "The book is already in the user's list",
            str(e.exception)
        )

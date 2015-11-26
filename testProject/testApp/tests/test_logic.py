from django.test import TestCase

from testApp.models import User, Book
from testApp.views import book_lend_logic


class BookLendTestCase(TestCase):
    fixtures = ['book_lend_fixtures.json']

    def setUp(self):
        super(BookLendTestCase, self).setUp()
        self.user = User.objects.get(pk=1)
        self.book1 = Book.objects.get(pk=1)

    def test_book_lend_valid(self):
        u = book_lend_logic(self.user, self.book1)
        self.assertTrue(u.books_lent.filter(id=self.book1.id).exists())

    def test_book_lend_fail(self):
        u = book_lend_logic(self.user, self.book1)

        # Primera forma
        try:
            book_lend_logic(self.user, self.book1)
            self.assertFail()
        except Exception as e:
            self.assertEqual(e.message,
                             "The book is already in the user's list")

        # # Segunda forma
        # with self.assertRaises(Exception) as e:
        #     book_lend_logic(self.user, self.book1)
        # self.assertEqual(
        #     "The book is already in the user's list",
        #     str(e.exception)
        # )

from django.test import TestCase
from django.core.cache import caches
from django.core.exceptions import ValidationError

from testApp.forms import LoginForm


class LoginFormTestCase(TestCase):
    fixtures = ['form_fixtures.json']

    def setUp(self):
        super(LoginFormTestCase, self).setUp()

    def test_user_login_valid(self):
        form = LoginForm({'username': 'test', 'password': 'test'})
        self.assertTrue(form.is_valid())

    def test_user_login_fail(self):
        form = LoginForm({'username': 'another', 'password': 'another'})
        ret_val = form.is_valid()
        self.assertFalse(ret_val)

        # Validate the error
        err = form.errors.as_data()['__all__'][0]
        self.assertEqual(err.message, "Username / Password not valid")

    def test_user_login_fail_usrname(self):
        form = LoginForm({'username': 'test', 'password': 'another'})
        self.assertFalse(form.is_valid())

    def test_user_login_fail_pwd(self):
        form = LoginForm({'username': 'another', 'password': 'test'})
        self.assertFalse(form.is_valid())

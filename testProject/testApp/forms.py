import datetime
from django.core.cache import caches
from django.forms import ModelForm
from django import forms
from testApp.models import Book
from testApp.models import User


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'num_pages', 'num_copies']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = User.objects.filter(name=username, password=password)
        if (not user) or (not self.user_login(user[0])):
            raise forms.ValidationError("Username / Password not valid")

    def user_login(self, user):
        if user:
            caches['default'].set('user', user)
            user.last_login = datetime.datetime.now()
            user.save()
            return True
        else:
            return False

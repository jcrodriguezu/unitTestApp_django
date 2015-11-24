from django.forms import ModelForm
from testApp.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'num_pages', 'num_copies']

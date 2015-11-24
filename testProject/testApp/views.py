import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import caches
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from testApp.models import Book, User
from testApp.forms import BookForm


def index(request):
    cache = caches['default']
    user = cache.get('user')
    context = {}
    context['book_list'] = get_books()
    if user:
        context['username'] = user.name
        context['privileges'] = user.privileges
        context['user_books'] = user.books_borrowed.all()
    return render(request, 'index.html', context)


def login(request):
    state = "Please log in below..."
    username = password = ''
    cache = caches['default']
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name=username, password=password)
        if user:
            u = user[0]
            cache.set('user', u)
            u.last_login = datetime.datetime.now()
            u.save()
            return redirect('index')
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html', {'state': state,
                                          'username': username})


def logout(request):
    caches['default'].delete('user')
    return redirect('index')


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'book_edit.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'book_delete.html', {'object': book})


def book_borrow(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cache = caches['default']
    user = cache.get('user')
    if user:
        book.num_copies = book.num_copies - 1
        book.save()
        user.books_borrowed.add(book)
        user.save()
        cache.set('user', user)
    return redirect('index')


def book_return(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cache = caches['default']
    user = cache.get('user')
    if user:
        book.num_copies = book.num_copies + 1
        book.save()
        user.books_borrowed.remove(book)
        user.save()
        cache.set('user', user)
    return redirect('index')


def get_books():
    return Book.objects.all()

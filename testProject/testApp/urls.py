from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^book_create$', views.book_create, name='book_create'),
    url(r'^book_update/(?P<pk>\d+)$', views.book_update, name='book_update'),
    url(r'^book_delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
    url(r'^book_lend/(?P<pk>\d+)$', views.book_lend, name='book_lend'),
    url(r'^book_return/(?P<pk>\d+)$', views.book_return, name='book_return'),
]

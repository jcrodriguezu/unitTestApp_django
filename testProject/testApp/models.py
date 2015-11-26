from django.db import models
from datetime import timedelta
from datetime import date


class Privileges(models.Model):
    name = models.CharField(max_length=3, null=False, unique=True)
    desc = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250, null=False)
    author = models.CharField(max_length=150, null=False)
    num_pages = models.PositiveIntegerField()
    num_copies = models.PositiveIntegerField(null=False)

    def is_available(self):
        return self.num_copies > 0

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.author)


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=128, null=False)
    privileges = models.ForeignKey(Privileges)
    books_lent = models.ManyToManyField(Book, blank=True)
    last_login = models.DateTimeField(null=True)

    def is_active(self):
        return self.last_login < (date.today() - timedelta(days=60))

    def __unicode__(self):
        return self.name

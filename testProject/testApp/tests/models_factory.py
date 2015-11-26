import datetime
import factory
import factory.fuzzy


class PrivilegesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "testApp.Privileges"

    name = "USR"
    desc = "User rol"


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "testApp.Book"

    title = factory.Sequence(lambda n: "Book Title %d" % n)
    author = factory.Sequence(lambda n: "Author%d" % n)
    num_pages = factory.fuzzy.FuzzyInteger(10, 1000)
    num_copies = factory.fuzzy.FuzzyInteger(1, 10)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "testApp.User"

    name = factory.Sequence(lambda n: 'user%s' % n)
    password = factory.LazyAttribute(lambda a: '%s' % a.name)
    privileges = factory.SubFactory(PrivilegesFactory)
    # books_lent = factory.SubFactory(BookFactory)
    last_login = datetime.datetime.now()

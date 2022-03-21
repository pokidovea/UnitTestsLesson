import factory
from django.utils.text import slugify

from bookshop.models import Author, Book, Publisher


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Sequence(lambda n: f'Vasya{n}')
    birthday = factory.Faker('date')
    date_of_death = None
    country = factory.Faker('bank_country')
    portrait = factory.django.ImageField()
    bio = factory.Faker('text')


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Faker('word')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('word')
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    short_description = factory.Faker('text')
    page_count = factory.Faker('random_int', min=100, max=1000)
    language = factory.Iterator(Book.Language)
    publisher = factory.SubFactory(PublisherFactory)
    publishing_year = factory.Faker('random_int', min=1900, max=2022)
    cover_type = factory.Iterator(Book.CoverType)
    cost = factory.Faker('random_number', digits=2)
    picture = factory.django.ImageField()
    count_in_storage = factory.Faker('random_int', min=0, max=100)

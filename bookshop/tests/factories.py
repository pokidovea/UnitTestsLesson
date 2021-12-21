import factory

from bookshop.models import Author, Publisher


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

import immobilus
from pytest_factoryboy import register

from bookshop.tests.factories import AuthorFactory, BookFactory, PublisherFactory

register(AuthorFactory)
register(PublisherFactory)
register(BookFactory)

import immobilus  # noqa
from pytest_factoryboy import register

from bookshop.tests.factories import AuthorFactory, PublisherFactory

register(AuthorFactory)
register(PublisherFactory)

import pytest
from immobilus import immobilus

from bookshop.models import Book


@pytest.fixture()
def book(author_factory, publisher_factory):
    book = Book.objects.create(
        title='Title',
        slug='title',
        short_description='',
        page_count=10,
        language='ru',
        publisher=publisher_factory(),
        publishing_year=2011,
        cover_type='soft',
        cost=1000,
        picture='test/test.jpg',
        count_in_storage=10,
    )

    book.authors.set([author_factory(), author_factory()])

    return book


@pytest.mark.django_db
@immobilus('2021-12-21')
def test_cost_with_ny_discount(book):
    assert book.cost_with_discount == book.cost * 0.8


@pytest.mark.django_db
@immobilus('2021-03-08')
def test_cost_with_8_march_discount(book):
    assert book.cost_with_discount == book.cost * 0.9

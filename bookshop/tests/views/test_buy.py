import pytest

from bookshop.models import Book


@pytest.fixture()
def buy_a_book_mock(mocker):
    return mocker.patch('bookshop.views.buy_a_book')


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
def test_book_not_found(client):
    url = '/buy/42'

    response = client.post(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_book_purchased_successfully(book, client, buy_a_book_mock):
    url = f'/buy/{book.id}'
    buy_a_book_mock.return_value = True
    # buy_a_book_mock.side_effect = Exception('wrong')

    response = client.post(url)

    assert response.status_code == 200
    assert response.json() == {
        'success': True,
        'message': f'Book "{book}" purchased successfully',
    }
    buy_a_book_mock.assert_called_once_with(book.id, book.cost_with_discount)

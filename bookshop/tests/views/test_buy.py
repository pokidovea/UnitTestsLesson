import pytest


@pytest.fixture()
def book(book_factory):
    return book_factory(count_in_storage=3)


@pytest.fixture()
def mocked_buy_a_book(mocker):
    return mocker.patch('bookshop.views.buy_a_book')


def test_wrong_method(client):
    response = client.get('/buy/42')

    assert response.status_code == 405


@pytest.mark.django_db
def test_book_not_found(client):
    response = client.post('/buy/42')

    assert response.status_code == 404


@pytest.mark.django_db
def test_out_of_stock(client, book_factory):
    book = book_factory(count_in_storage=0)

    response = client.post(f'/buy/{book.id}')

    assert response.status_code == 200
    assert response.json() == {'message': 'Out of stock', 'success': False}


@pytest.mark.django_db
def test_service_unavailable(client, book, mocked_buy_a_book):
    mocked_buy_a_book.return_value = False

    response = client.post(f'/buy/{book.id}')

    assert response.status_code == 200
    assert response.json() == {
        'message': 'Processing service is unavailable. Please try later.',
        'success': False
    }


@pytest.mark.django_db
def test_successful_purchase(client, book, mocked_buy_a_book):
    mocked_buy_a_book.return_value = True

    response = client.post(f'/buy/{book.id}')

    assert response.status_code == 200
    assert response.json() == {
        'message': f'Book "{book.title} ({book.publishing_year})" purchased successfully',
        'success': True
    }

    book.refresh_from_db()
    assert book.count_in_storage == 2


@pytest.mark.django_db
def test_exception(client, book, mocked_buy_a_book):
    mocked_buy_a_book.side_effect = Exception('AAAAAAAA!!!!')

    with pytest.raises(Exception) as exc:
        client.post(f'/buy/{book.id}')

    assert str(exc.value) == 'AAAAAAAA!!!!'

import pytest
from immobilus import immobilus


@pytest.mark.django_db
@pytest.mark.parametrize('date, expected_cost', [
    ('2022-06-01', 1000),
    ('2022-03-08', 900),
    ('2022-12-25', 800),
])
def test_cost_in_regular_date(book_factory, date, expected_cost):
    book = book_factory(cost=1000)

    with immobilus(date):
        assert book.cost_with_discount == expected_cost

from datetime import date

import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'date_of_death, expected_result',
    [
        (None, 'Vasya (1987-...)'),
        (date(2021, 1, 1), 'Vasya (1987-2021)'),
    ],
)
def test_str_method(date_of_death, expected_result, author_factory):
    author = author_factory(name='Vasya', birthday=date(1987, 1, 1), date_of_death=date_of_death)

    result = str(author)

    assert result == expected_result

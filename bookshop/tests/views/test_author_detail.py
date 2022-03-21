from datetime import date

import pytest


@pytest.mark.django_db
def test_correct_response(author_factory, client, snapshot):
    author = author_factory(
        name='Vasya',
        birthday=date(1987, 1, 1),
        date_of_death=None,
        country='Russia',
        portrait='images/vasya.png',
        bio='Test'
    )

    response = client.get(f'/author/{author.id}')

    assert response.status_code == 200
    snapshot.assert_match(response.content.decode('utf-8'))

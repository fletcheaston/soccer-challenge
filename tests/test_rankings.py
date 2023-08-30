import pytest


from cli import Ranking


@pytest.fixture
def tarantulas_ranking() -> Ranking:
    return Ranking(
        place=1,
        team="Tarantulas",
        points=6,
    )


@pytest.fixture
def lions_ranking() -> Ranking:
    return Ranking(
        place=2,
        team="Lions",
        points=5,
    )


@pytest.fixture
def fc_awesome_ranking() -> Ranking:
    return Ranking(
        place=3,
        team="FC Awesome",
        points=1,
    )


@pytest.fixture
def snakes_ranking() -> Ranking:
    return Ranking(
        place=3,
        team="Snakes",
        points=1,
    )


@pytest.fixture
def grouches_ranking() -> Ranking:
    return Ranking(
        place=5,
        team="Grouches",
        points=0,
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "ranking,string",
    [
        (pytest.lazy_fixture("tarantulas_ranking"), "1. Tarantulas, 6 pts"),
        (pytest.lazy_fixture("lions_ranking"), "2. Lions, 5 pts"),
        (pytest.lazy_fixture("fc_awesome_ranking"), "3. FC Awesome, 1 pt"),
        (pytest.lazy_fixture("snakes_ranking"), "3. Snakes, 1 pt"),
        (pytest.lazy_fixture("grouches_ranking"), "5. Grouches, 0 pts"),
    ],
)
def test_ranking_str(
    ranking: Ranking,
    string: str,
) -> None:
    assert str(ranking) == string


@pytest.mark.unit
def test_ranking_order(
    tarantulas_ranking: Ranking,
    lions_ranking: Ranking,
    fc_awesome_ranking: Ranking,
    snakes_ranking: Ranking,
    grouches_ranking: Ranking,
) -> None:
    correct_ranking = [
        tarantulas_ranking,
        lions_ranking,
        fc_awesome_ranking,
        snakes_ranking,
        grouches_ranking,
    ]

    incorrect_ranking = [
        lions_ranking,
        snakes_ranking,
        tarantulas_ranking,
        grouches_ranking,
        fc_awesome_ranking,
    ]

    assert sorted(incorrect_ranking) == correct_ranking

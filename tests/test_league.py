import pytest

from cli import Game, League, Ranking


@pytest.mark.integration
def test_simple_team_ranking_in_league() -> None:
    league = League()

    league.add_game(
        Game(
            team_a="A",
            team_a_goals=1,
            team_b="B",
            team_b_goals=0,
        ),
    )

    assert league.team_rankings == [
        Ranking(place=1, team="A", points=3),
        Ranking(place=2, team="B", points=0),
    ]


@pytest.mark.integration
def test_complex_team_ranking_in_league() -> None:
    league = League()

    league.add_game(
        Game(
            team_a="Lions",
            team_a_goals=3,
            team_b="Snakes",
            team_b_goals=3,
        ),
    )

    league.add_game(
        Game(
            team_a="Tarantulas",
            team_a_goals=1,
            team_b="FC Awesome",
            team_b_goals=0,
        ),
    )

    league.add_game(
        Game(
            team_a="Lions",
            team_a_goals=1,
            team_b="FC Awesome",
            team_b_goals=1,
        ),
    )

    league.add_game(
        Game(
            team_a="Tarantulas",
            team_a_goals=3,
            team_b="Snakes",
            team_b_goals=1,
        ),
    )

    league.add_game(
        Game(
            team_a="Lions",
            team_a_goals=4,
            team_b="Grouches",
            team_b_goals=0,
        ),
    )

    assert league.team_rankings == [
        Ranking(place=1, team="Tarantulas", points=6),
        Ranking(place=2, team="Lions", points=5),
        Ranking(place=3, team="FC Awesome", points=1),
        Ranking(place=3, team="Snakes", points=1),
        Ranking(place=5, team="Grouches", points=0),
    ]

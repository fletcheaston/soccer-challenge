import pytest

from cli import Game


@pytest.mark.unit
def test_team_a_wins_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=1,
        team_b="B",
        team_b_goals=0,
    )

    assert game.winner == "A"

    assert game.points_for("A") == 3
    assert game.points_for("B") == 0


@pytest.mark.unit
def test_team_b_wins_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=0,
        team_b="B",
        team_b_goals=1,
    )

    assert game.winner == "B"

    assert game.points_for("A") == 0
    assert game.points_for("B") == 3


@pytest.mark.unit
def test_tie_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=0,
        team_b="B",
        team_b_goals=0,
    )

    assert game.winner is None

    assert game.points_for("A") == 1
    assert game.points_for("B") == 1

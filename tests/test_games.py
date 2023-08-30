from cli import Game


def test_team_a_wins_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=1,
        team_b="B",
        team_b_goals=0,
    )

    assert game.winner == "A"


def test_team_b_wins_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=0,
        team_b="B",
        team_b_goals=1,
    )

    assert game.winner == "B"


def test_tie_game() -> None:
    game = Game(
        team_a="A",
        team_a_goals=0,
        team_b="B",
        team_b_goals=0,
    )

    assert game.winner is None

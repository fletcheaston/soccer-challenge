from cli import Game, League


def test_teams_in_league() -> None:
    # No teams to start
    league = League()

    assert league.teams == set()

    # Teams added automatically when adding game
    game = Game(
        team_a="A",
        team_a_goals=1,
        team_b="B",
        team_b_goals=0,
    )

    league.add_game(game)

    assert league.teams == {"A", "B"}

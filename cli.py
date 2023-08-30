from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from typer import Typer

cli = Typer()


@dataclass
class Game:
    team_a: str
    team_a_goals: int

    team_b: str
    team_b_goals: int

    @property
    def winner(self) -> str | None:
        if self.team_a_goals > self.team_b_goals:
            return self.team_a

        if self.team_a_goals < self.team_b_goals:
            return self.team_b

        return None

    def points_for(self, team: str) -> int:
        """
        3 points for the winner
        1 point for a tie
        0 points for a loss
        """

        # Make sure we're given a valid team
        assert team in [self.team_a, self.team_b]

        # Check for win
        if self.winner == team:
            return 3

        # Check for tie
        if self.winner is None:
            return 1

        # Otherwise, loss
        return 0


@dataclass
class SoccerLeague:
    _games: list[Game] = field(default_factory=list)
    _team_points: Counter[str] = field(default_factory=Counter)

    def add_game(self, game: Game) -> None:
        # Save the game for later stats, if needed
        self._games.append(game)

        # Update points for each team from the game
        self._team_points[game.team_a] += game.points_for(game.team_a)
        self._team_points[game.team_b] += game.points_for(game.team_b)

    @property
    def team_rankings(self) -> None:
        return None


@cli.command()
def parse_games(input_file: Path) -> None:
    """Read the games from the specified "input_file", parse each line as a game."""

    if not input_file.exists():
        raise ValueError("Input file doesn't exist.")


@cli.command()
def placeholder() -> None:
    pass


if __name__ == "__main__":
    cli()

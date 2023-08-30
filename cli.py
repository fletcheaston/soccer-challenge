from dataclasses import dataclass
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

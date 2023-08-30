from pathlib import Path

from typer import Typer

cli = Typer()


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

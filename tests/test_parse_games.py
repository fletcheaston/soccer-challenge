from typer.testing import CliRunner

from cli import cli

runner = CliRunner()


def test_fails_with_nonexistant_file() -> None:
    result = runner.invoke(cli, ["parse-games", "does-not-exist.txt"])

    assert result.exit_code != 0


def test_doesnt_fail_with_existing_file() -> None:
    result = runner.invoke(cli, ["parse-games", "sample-input.txt"])

    assert result.exit_code == 0

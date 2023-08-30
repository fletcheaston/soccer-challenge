import filecmp
import os

import pytest
from typer.testing import CliRunner

from cli import cli
import contextlib

runner = CliRunner()


@pytest.mark.e2e
def test_fails_with_nonexistant_input_file() -> None:
    result = runner.invoke(
        cli,
        [
            "input-file-does-not-exist.txt",
            "N/A",
        ],
    )

    assert result.exit_code != 0


@pytest.mark.e2e
def test_output_file_matches_expected_output_file() -> None:
    # Remove the "sample-output.txt" file if it exists
    with contextlib.suppress(Exception):
        os.remove("real-output.txt")

    result = runner.invoke(
        cli,
        [
            "sample-input.txt",
            "real-output.txt",
        ],
    )

    assert result.exit_code == 0

    # See if files match
    assert filecmp.cmp(
        "real-output.txt",
        "expected-output.txt",
        shallow=False,
    )

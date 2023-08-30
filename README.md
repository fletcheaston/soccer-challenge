
# Fletcher's Notes

Started on 08/29/2023 at ~9:10pm PT.
Completed (with documentation, tests, etc.) on 08/29/2023 at ~11:48pm PT.

## Plan

1. Project setup/boilerplate files
   - [Conda](https://docs.conda.io/en/latest/) for environment management
   - [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) for requirements
   - [Typer](https://typer.tiangolo.com/) for the CLI tool
   - [Pytest](https://docs.pytest.org/en/7.4.x/) for the testing tool
   - [Ruff](https://beta.ruff.rs/docs/), [Black](https://black.readthedocs.io/en/stable/), and [Mypy](https://mypy-lang.org/) for dev tooling

2. Read and parse data from a given file path

3. Put data into nice data structures

4. Produce output file for a given file path

5. Write tests validating functionality

6. Documentation

## Setup

This setup assumes you have conda installed.
Find more info [here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) about installing and setting up conda.

Replace `{env name}` below with your desired conda environment name.

1. Create a conda environment for the app
    ```shell
    conda create -n {env name} python=3.11
    ```

2. Activate the conda environment
    ```shell
    conda activate {env name}
    ```

3. Install app dependencies (multiple options avilable)
   1. Install all dependencies (easiest option)
       ```shell
       pip install '.[dev,test]'
       ```
   2. Install only dependencies required to run the CLI (production-ready option)
       ```shell
       pip install .
       ```
   3. Install dev dependencies to run the CLI and perform linting, type checking, etc. (dev option)
       ```shell
       pip install '.[dev]'
       ```
   4. Install dependencies to run the CLI and run tests (CI option)
       ```shell
       pip install '.[test]'
       ```

4. Add your conda environment to your IDE

## Running Locally

### Run the CLI Locally

Activate the conda environment
```shell
conda activate {env name}
```

You can run the CLI with the following shell commands

#### Output results to terminal

```shell
python3 cli.py {input file path}
```

For example, you can use this to run on the `sample-input.txt` file and output to the terminal
```shell
python3 cli.py sample-input.txt
```

#### Output results to a file
```shell
python3 cli.py {input file path} --output-file {output file path}
```

For example, you can use this to run on the `sample-input.txt` file and output to the `real-output.txt` file in the root of the repository
```shell
python3 cli.py sample-input.txt --output-file real-output.txt
```

#### More info

You can find more information on the CLI with the following shell command
```shell
python3 cli.py --help
```

The CLI tests can be found under `tests/test_cli.py`.

### Running Tests

Activate the conda environment (you must have test dependencies installed)
```shell
conda activate {env name}
```

You can run all tests with `pytest` using the following shell command
```shell
pytest . --cov
```

This will run all tests and output test coverage to the terminal.
If you'd like to run specific tests, please check the [pytest documentation](https://docs.pytest.org/en/7.4.x/how-to/usage.html#specifying-which-tests-to-run).
All tests are marked as either `unit`, `integration`, or `e2e` tests.

At the time of challenge completion, the test suite passes with a coverage of 99%.
I wish I could get that last 1%, but it's just the `cli()` entrypoint in `cli.py` so ¯\_(ツ)_/¯ no big deal

```text
======================== test session starts =========================
platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.3.0
rootdir: /Users/fletchereaston/Documents/GitHub/soccer-challenge
configfile: pyproject.toml
plugins: cov-4.1.0, lazy-fixture-0.6.3
collected 14 items

tests/test_cli.py ...                                          [ 21%]
tests/test_games.py ...                                        [ 42%]
tests/test_league.py ..                                        [ 57%]
tests/test_rankings.py ......                                  [100%]

---------- coverage: platform darwin, python 3.11.5-final-0 ----------
Name                     Stmts   Miss  Cover
--------------------------------------------
cli.py                      81      2    98%
tests/__init__.py            0      0   100%
tests/test_cli.py           29      0   100%
tests/test_games.py         20      0   100%
tests/test_league.py        16      0   100%
tests/test_rankings.py      26      0   100%
--------------------------------------------
TOTAL                      172      2    99%


========================= 14 passed in 0.07s =========================
```

## Review

I'm really happy with what I did for the challenge, I really have no major areas that I think could use improvement for this challenge.

I think the only noteworthy thing is that my inital plan (preserved above) had tests coming later and command/CLI stuff coming earlier.
In reality, I tested each class/method/property as I went and only did the full command/CLI implementation at the end.

The part I'm probably most proud of is my usage of the `Counter` collection.
I feel like `Counter` is something most Python devs don't know about, but provides a crazy amount of utility out of the box.
If you don't know what `Counter` is, please [go check it out](https://docs.python.org/3/library/collections.html#collections.Counter).

If the "goal differential" challenge was added, I wouldn't need to do any real overhauls to how this code works.
Essentially, the changes would involve...

1. Add this field to the `League` class: `_team_goal_differential: Counter[str] = field(default_factory=Counter)`
2. Add this field to the `Ranking` class: `goal_differential: int`
3. Update various methods/properties to include goal differentials
   - `__str__` on `Ranking`
   - `__lt__` on `Ranking`
   - `add_game` on `League`
   - `team_rankings` on `League`

I could also add a helper method to the `Game` class for getting the goal differentials for each team, but ¯\_(ツ)_/¯
maybe not super useful, it's easy enough to calculate that

# The Challenge

We want you to create a command-line application that will calculate the
ranking table for a soccer league.


## Table of contents
- [The Challenge](#the-challenge)
  * [Expected input and output](#expected-input-and-output)
  * [The rules](#the-rules)
  * [Guidelines](#guidelines)
    + [After you finish](#after-you-finish)
  * [What to send back to our team](#what-to-send-back-to-our-team)
    + [Platform support](#platform-support)
    + [What to expect afterwards](#what-to-expect-afterwards)

## Expected input and output

You can find the [sample-input.txt](sample-input.txt) and [expected-output.txt](expected-output.txt) files at the top of this repository

The input and output will be text. Your solution should parse the provided `sample-input.txt` file via stdin (pipe or redirect)or by parsing a file passed by name on the command line. Your solution should output the correct result via stdout to the console.

The input contains results of games, one per line. See `sample-input.txt` for details. The output should be ordered from most to least points, following the format specified in `expected-output.txt`.

You can expect that the input will be well-formed. There is no need to add
special handling for malformed input files.

## The rules

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points. If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data). Ranks are assigned according to [standard competition (1224) ranking](https://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_(%221224%22_ranking)).

We expect the resulting output of the provided `sample-input.txt` file to *exactly match the contents* of `expected-output.txt`.

## Guidelines

For the programming languages allowed we would prefer that you use Python. If Python is not a programming language that you use often, please choose a language that is both comfortable for you and suited to the task. However _we would be very impress_ if you are able to submit the challenge in a pythonic fashion (don't worry we would be rating your submission keeping this in mind!).

Your solution should be able to be run (and if applicable, built) from the command line. Please include appropriate scripts and instructions for running your application and your tests.

If you use other libraries installed by a common package manager (pip, poetry, npm, gradle, etc.), it is not necessary to commit the installed packages.

We write automated tests and *we would like you to do so as well*.

We appreciate well factored, object-oriented or functional designs.

We request that you spend no more than a few hours on this portion of the interview ( <= 3 hours is what we expect).

### After you finish

- Please document any steps necessary to run your solution and your tests.
- Please take 10 minutes to review your submission and list a few areas that would benefit from more time and attention. 

## What to send back to our team

Please send an email back to your point of contact with:

- the code you used to calculate the rankings
- your test suite code
- simple instructions on how to install and use your code
- the amount of time you spent on the project
- the list of improvements you would make

> You can send us the submission in the form of a tarball, zip file, or a Github link to your repository.

### Platform support

This will be run in a unix-ish environment (OS X or Linux).
Please use platform-agnostic constructs where possible (line-endings and file-path-separators are two problematic areas).

### What to expect afterwards

Once you have sent us your project, we will review the code with our team members and rate it appropiately.
If everything looks fine, we would like to have a code review interview with you where we will be going over what you sent us, as well as requesting a few changes in the code to see if the output can be altered. An example of what you can be expecting can be seen in this documentation: [goal-differential-instructions.md](goal-differential-instructions.md)

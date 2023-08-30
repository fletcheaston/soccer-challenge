
# Fletcher's Notes

Started on 08/29/2023 at ~9:10pm PT.

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

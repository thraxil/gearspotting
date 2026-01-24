# GEMINI.md

This project uses Python 3.12 and Django 6. Package management is with
`uv` and configured in `pyproject.toml`.

This project uses a `Makefile` to automate common tasks. Here are some of the most useful commands:

## Development

*   `make runserver`: Starts the Django development server.
*   `make test`: Runs the test suite.
*   `make fulltest`: Runs the full test suite, including code style checks.
*   `make shell`: Opens a Django shell.
*   `make migrate`: Applies database migrations.
*   `make makemigrations`: Creates new database migrations based on model changes.
*   `make check`: Runs Django's system check framework.

## Code Quality & Formatting

*   `make ruff-check`: Checks for and fixes import order issues with ruff.
*   `make ruff-format`: Formats the code using ruff.
*   `make mypy`: Runs mypy for static type checking.

- Always include type hints when generating code
- Always use native collection types (e.g., `list`, `dict`) for type hints, not `typing.List`, `typing.Dict`.
- Always run `ruff-check`, `ruff-format`, and `mypy` after editing code.

## Dependencies

*   `make uv.lock`: Updates the `uv.lock` file from `pyproject.toml`.
*   `make libyear`: Checks for outdated dependencies.

## Deployment

*   `make collectstatic`: Collects static files for production.

## Git

*   `make pull`: Pulls the latest changes from git and runs `check`, `test`, and `migrate`.
*   `make rebase`: Pulls the latest changes from git with rebase and runs `check`, `test`, and `migrate`.

## Setup

*   `make install`: Sets up the development environment for the first time. **Warning:** Only run this on a new machine.
*   `make clean`: Removes temporary files.

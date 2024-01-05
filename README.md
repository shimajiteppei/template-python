# template-python

My tiny Python repository template

## tools

| use | name |
|---|---|
| version manager | [pyenv](https://github.com/pyenv/pyenv) |
| package manager | [poetry](https://github.com/python-poetry/poetry) |
| linter, formatter | [ruff](https://github.com/astral-sh/ruff) |
| test | [pytest](https://github.com/pytest-dev/pytest) |
| benchmark | [pytest-benchmark](https://github.com/ionelmc/pytest-benchmark) |

## install

```shell
pyenv shell --unset
poetry install --no-cache
```

## test

```shell
poetry run pytest
```

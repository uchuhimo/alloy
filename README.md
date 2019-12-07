# Alloy

[![](https://img.shields.io/pypi/v/alloy.svg)](https://pypi.python.org/pypi/alloy)
[![](https://img.shields.io/travis/uchuhimo/alloy.svg)](https://travis-ci.org/uchuhimo/alloy)
[![](https://github.com/uchuhimo/alloy/workflows/Python%20package/badge.svg)](https://github.com/uchuhimo/alloy/actions)
[![Documentation Status](https://readthedocs.org/projects/alloy/badge/?version=latest)](https://alloy.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/uchuhimo/alloy/shield.svg)](https://pyup.io/repos/github/uchuhimo/alloy/)

A tool to combine function with DAG.

- Documentation: https://alloy.readthedocs.io.

## Development

### Create a virtual environment

```bash
conda env create -f environment.yml
source activate alloy
```

### Install dependencies

There are two options:

- Use poetry:
    ```bash
    poetry install
    ```
- Use pip:
    ```bash
    pip install -e ".[dev]"
    ```

### Update dependencies

```bash
poetry update
```

### Bump version

```bash
bumpversion minor  # major, minor, patch
```

### Show information about installed packages

```bash
poetry show
```

### Show dependency tree

```bash
dephell deps tree
# or
dephell deps tree pytest
```

### Install git pre-commit hooks

```bash
pre-commit install
```

# License

© uchuhimo, 2019. Licensed under an [Apache 2.0](./LICENSE) license.

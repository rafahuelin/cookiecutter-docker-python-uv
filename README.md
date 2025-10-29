[![GitHub release](https://img.shields.io/github/v/release/rafahuelin/cookiecutter-docker-python-uv)](https://github.com/rafahuelin/cookiecutter-docker-python-uv/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Cookiecutter](https://img.shields.io/badge/built%20with-cookiecutter-orange)](https://github.com/cookiecutter/cookiecutter)

# 🍪 Cookiecutter Python Template

> A clean Cookiecutter template for building production-ready Dockerized Python apps with:
> - Docker
> - uv
> - Devcontainers
> - Ruff
> - pre-commit hooks.
>


## Generate project
[Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you still don't have it and execute:
```shell
uvx cookiecutter gh:rafahuelin/cookiecutter-docker-python-uv
```

## Output Preview
```
📁 your-project/
├── .devcontainer/
│   ├── devcontainer.json
│   └── docker-compose.dev.yml
├── src/
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── Dockerfile
├── pyproject.toml
├── README.md
└── uv.lock
```

## Quick start

1. Generate Project
  ![Generate Project](docs/generate-project.gif)
2. Open Project
  ![Open Project](docs/open-project.gif)
3. Install Devcontainers extension
  ![Install Devcontainers extension](docs/install-devcontainers-extension.gif)
4. Run Tests with coverage
  ![Run tests with coverage](docs/run-tests-with-coverage.gif)
1. Debug Tests
  ![Debug Tests](docs/debug-tests.gif)
1. Linter
  ![Linter](docs/linter.gif)

## Features
- Dockerized Python Develpment setup with global uv setup (without virtual environment)
- Uses only actively supported CPython versions
  - Offered at project creation and pinned in the base image and .python-version.
- Single Dockerfile for dev and production
  - Develop locally with the same Dockerfile that builds your production image.
- VS Code Dev Container setup
  - Docker Compose-based dev environment.
  - Workspace is bind-mounted so Git status and changes behave exactly as on the host.
  - User UID and GID makes possible to edit files from inside or outside the devcontainer.
  - Linter with Error Lens and Ruff.
- Fast dependency management with uv
  - pyproject.toml-based workflow with uv for speedy, reproducible installs.
- Testing scaffold
  - pytest pre-configured with example tests.
  - coverage library pre-installed.
- Pre-commit hooks ready
  - Linting/formatting hooks configured via .pre-commit-config.yaml.
- Environment management
  - .env.example provided; .env consumed by the dev setup.

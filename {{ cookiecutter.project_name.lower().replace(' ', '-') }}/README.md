# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Quick start

- VS Code Dev Container (recommended)
  1. Install the “Dev Containers” extension.
  2. Open this folder in VS Code.
  3. Run: Dev Containers: Reopen in Container.

- Or with Docker Compose directly
```bash
docker compose -f .devcontainer/docker-compose.dev.yml up --build
```

## Features

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

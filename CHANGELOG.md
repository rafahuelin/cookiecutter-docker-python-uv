# Changelog
All notable changes to this project will be documented in this file.
This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] – 2025-10-29
### Added
- 🎉 First official release of the cookiecutter template for Dockerized Python apps with uv.
- Template includes a `.devcontainer/` folder (with `devcontainer.json` and `docker-compose.dev.yml`) for VS Code devcontainer support.
- Project skeleton created: `src/` directory with example `main.py`, `tests/` directory with `conftest.py` and `test_main.py`.
- Provided `.env.example` for environment variables, `.gitignore`, `.pre-commit-config.yaml`, `.python-version`, `Dockerfile`, `pyproject.toml`, and `README.md`.
- Full dockerised setup: single `Dockerfile` usable for both development and production.
- Uses global `uv` (not virtual environments) for dependency management via `pyproject.toml`.
- Linter/formatter setup: `ruff` + pre-commit hooks ready out of the box.
- Fast test scaffold: `pytest` pre-configured, coverage library included.
- Docker Compose based dev environment with workspace bind-mounting and correct UID/GID handling for editing files from inside/outside container.

### Changed
- —

### Fixed
- —

### Removed
- —

### Security
- Uses only actively supported Python versions (ensuring no deprecated CPython version is used) as stated in features.

---
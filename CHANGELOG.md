# Changelog
All notable changes to this project will be documented in this file.
This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] – 2025-11-09
### Added
- Allow adding Python dependencies from the dev container with `uv add <package-name>` (dev user can write to global site-packages).

### Changed
- —

### Fixed
- -

### Removed
- —

### Security
- Prod stage runs as non-root and locks down `/app` and `/usr/local/*` to root ownership.

---

## [1.0.2] – 2025-11-06
### Added
- Extra linux dependencies to ensure python test in devcontainer.
- Improved documentation on how to create project without input.

### Changed
- —

### Fixed
- -

### Removed
- —

### Security
- -

---

## [1.0.1] – 2025-11-02
### Added
- Prod stage
- PYTHONUNBUFFERED=1 to disable python output buffering
- PYTHONDONTWRITEBYTECODE=1 to prevent python from writing .pyc files and __pycache__ directories

### Changed
- —

### Fixed
- Cleanup

### Removed
- —

### Security
- -

---

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
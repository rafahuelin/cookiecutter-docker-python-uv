import subprocess
import os
from pathlib import Path
from shutil import rmtree


def init_git() -> None:
    """Initialize a git repository in the current directory."""
    subprocess.run(
        ["git", "init"],
        capture_output=True,
        text=True
    )


def generate_uv_lock() -> None:
    """Generate uv.lock by running `uv sync` in the given directory."""
    python_version = "{{cookiecutter._supported_python_versions[cookiecutter.python_version].latest}}"

    # Get the latest uv version
    subprocess.run(
        ["uv", "self", "update"],
        capture_output=True,
        text=True
    )

    # Check if the required Python version is already installed
    result_is_python_installed = subprocess.run(
        f'uv python list | grep {python_version} | grep -v "download available"',
        shell=True,
        capture_output=True,
        text=True,
    )

    # Ensure the required Python version is installed by uv's toolchain
    try:
        if len(result_is_python_installed.stdout) == 0:
            subprocess.run(
                ["uv", "python", "install", python_version],
                capture_output=True,
                text=True
            )
    except Exception as e:
        print(f"Failed to install Python {python_version} via uv: {e}")
        raise e

    # Generate uv.lock
    subprocess.run(
        ["uv", "sync", "--python", python_version, "--no-install-project", "--all-groups"],
        capture_output=True,
        text=True
    )


def create_devcontainer_env_file() -> None:
    """
    Create a .devcontainer/.env file with UID and GID.
    This is done for environment variables interpolation in docker-compose.dev.yml.
    """
    Path(".env").touch(exist_ok=True)
    env_file_path = Path(".devcontainer/.env")
    env_file_path.touch(exist_ok=True)

    uid: int = os.getuid()
    gid: int = os.getgid()

    with open(env_file_path, "w") as env_file:
        env_file.write(f"UID={uid}\n")
        env_file.write(f"GID={gid}\n")

    print(f"Created {env_file_path} with UID={uid} and GID={gid}.")


def initial_commit() -> None:
    """Make the initial commit in the git repository."""

    result = subprocess.run(
        ["git", "config", "user.email"],
        capture_output=True,
        text=True
    )

    if "@" in result.stdout and "." in result.stdout:
        subprocess.run(
            ["git", "add", "."],
            capture_output=True,
            text=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            capture_output=True,
            text=True
        )


def delete_venv() -> None:
    """Delete the virtual environment created to generate the uv.lock file."""
    venv_path = Path(".venv")
    rmtree(venv_path)


def main():
    generate_uv_lock()
    create_devcontainer_env_file()
    init_git()
    initial_commit()
    delete_venv()


if __name__ == "__main__":
    main()

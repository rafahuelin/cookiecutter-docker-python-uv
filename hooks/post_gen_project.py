import subprocess
import os
from pathlib import Path
from shutil import rmtree
from unittest import result


def init_git() -> None:
    """Initialize a git repository in the current directory."""
    subprocess.run(
        ["git", "init"],
        capture_output=True,
        text=True
    )


def generate_uv_lock() -> None:
    """Generate uv.lock using the Dockerfile."""
    commands = [
        ["docker", "build", "--target", "lock", "-t", "my-app:lock", "."],
        ["docker", "create", "--name", "temp-lock", "my-app:lock"],
        ["docker", "cp", "temp-lock:/uv.lock", "./"],
        ["docker", "rm", "temp-lock"]
    ]

    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("--- Docker command failed ---")
            print(f"Stderr:\n{e.stderr}")
            print(f"Stdout:\n{e.stdout}")
            print("-----------------------------")
            raise


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


def main():
    generate_uv_lock()
    create_devcontainer_env_file()
    init_git()
    initial_commit()


if __name__ == "__main__":
    main()

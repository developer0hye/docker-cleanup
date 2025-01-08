# dockerclean/cleaner.py

import subprocess

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")

def clean_docker():
    print("🛑 Stopping and removing all containers...")
    run_command("docker stop $(docker ps -aq) 2>/dev/null || true")
    run_command("docker rm $(docker ps -aq) 2>/dev/null || true")

    print("🛑 Removing all images...")
    run_command("docker rmi $(docker images -q) -f 2>/dev/null || true")

    print("🛑 Removing all volumes...")
    run_command("docker volume rm $(docker volume ls -q) -f 2>/dev/null || true")

    print("🛑 Pruning all networks...")
    run_command("docker network prune -f")

    print("🛑 Pruning builder cache...")
    run_command("docker builder prune -af")

    print("🛑 Performing full system prune...")
    run_command("docker system prune -af --volumes")

    print("✅ Docker cleanup completed successfully!")

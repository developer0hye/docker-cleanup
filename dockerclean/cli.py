# dockerclean/cli.py

import argparse
from .cleaner import clean_docker

def main():
    parser = argparse.ArgumentParser(description="Clean all Docker data (containers, images, volumes, networks).")
    parser.add_argument('-y', '--yes', action='store_true', help="Skip confirmation and run cleanup immediately.")
    args = parser.parse_args()

    if args.yes:
        clean_docker()
    else:
        confirm = input("⚠️ This will delete all Docker data (containers, images, volumes, networks). Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            clean_docker()
        else:
            print("Operation cancelled.")

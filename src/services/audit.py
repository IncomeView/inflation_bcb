# audit.py

from pprint import pprint

from src.services.health_check import validate_database


def main():
    print("\n=== DATABASE HEALTH ===\n")
    pprint(validate_database())


if __name__ == "__main__":
    main()

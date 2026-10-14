import os


def main() -> None:
    greeting = os.getenv("GREETING", "Hello")
    learner = os.getenv("LEARNER", "Docker learner")
    print(f"{greeting}, {learner}!")


if __name__ == "__main__":
    main()

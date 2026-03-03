import random


def get_integer_input(prompt: str) -> int:
    """Prompt the user until they provide a valid integer."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Please enter a valid whole number.")


def play_round(lower_bound: int = 1, upper_bound: int = 100) -> int:
    """Play a single round and return the number of attempts used."""
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        guess = get_integer_input("Enter your guess: ")
        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Your guess is out of range. Pick a number from {lower_bound} to {upper_bound}.")
            continue

        if guess > target_number:
            print("Too high")
        elif guess < target_number:
            print("Too low")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            return attempts


def main() -> None:
    """Run the number guessing game with optional replay."""
    print("Welcome to the Number Guessing Game!")

    while True:
        play_round(1, 100)
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

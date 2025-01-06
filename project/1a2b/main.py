import random
from typing import Set, Tuple


def generate_question() -> str:
    question: str = ""
    exist: Set[str] = set()

    for _ in range(4):
        number: str = str(random.randint(0, 9))
        while number in exist:
            number = str(random.randint(0, 9))
        exist.add(number)
        question += number

    return question


def check_number_validation(number: str) -> bool:
    # Check length
    if len(number) != 4:
        return False

    # Check number
    exist: Set[str] = set()
    for digit in number:
        if not digit.isdigit():
            return False
        if digit in exist:
            return False
        exist.add(digit)

    return True


def check_answer(answer: str, user_answer: str) -> bool:
    count_a: int = 0
    count_b: int = 0
    answer_numbers: Set[str] = set(answer)
    compare: Tuple[str, str] = zip(answer, user_answer)

    for answer_digit, user_digit in compare:
        if answer_digit == user_digit:
            count_a += 1
        elif user_digit in answer_numbers:
            count_b += 1

    print(f"Answer you guess:  {user_answer} => {count_a}A{count_b}B")
    return True if count_a == 4 else False


def main():
    while True:
        # Generate a random question
        question: str = generate_question()
        print(f"\n========== New Game Start ==========")

        # Keep guessing until right answer
        counter: int = 1
        while True:
            print(f"{counter}: ", end="")
            user_answer = input(f"Guess a number: ")
            if not check_number_validation(user_answer):
                continue

            if check_answer(question, user_answer):
                print(f"You only use {counter} times to WIN!!!!")
                break

            counter += 1
            print()


if __name__ == "__main__":
    main()

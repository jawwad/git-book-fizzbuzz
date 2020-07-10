#!/usr/bin/env python


def fizzbuzz_for_num(
    n: int,
    fizz_divisor: int = 3,
    fizz_word: str = "Fizz",
    buzz_divisor: int = 5,
    buzz_word: str = "Buzz",
):
    should_fizz = n % 3 == 0
    should_buzz = n % 5 == 0
    if should_fizz and should_buzz:
        return fizz_word + buzz_word
    elif should_fizz:
        return fizz_word
    elif should_buzz:
        return buzz_word
    else:
        return str(n)


def fizzbuzz():
    for n in range(1, 101):
        value = fizzbuzz_for_num(n)
        print(value)


def main():
    fizzbuzz()


if __name__ == "__main__":
    main()

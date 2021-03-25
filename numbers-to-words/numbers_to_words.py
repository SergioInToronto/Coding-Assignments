import math


NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "TODO",
    11: "TODO",
    12: "TODO",
    13: "TODO",
    14: "TODO",
    15: "TODO",
    16: "TODO",
    17: "TODO",
    18: "TODO",
    19: "TODO",
}

POWERS_OF_TEN = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

MULTIPLIERS = [
    "thounsand",
    "million",
    "billion",
]


def numbers_to_words(number):
    print(number)
    if number < 20:
        return NUMBERS[number]

    chunks = math.ceil(len(str(number)) / 3)
    result = ""
    for multiplier in range(chunks):
        triplet = _extract_triplet(number, multiplier)
        triplet = _999_or_less(triplet)
        # print(multiplier, triplet)
        if multiplier:
            triplet += " " + MULTIPLIERS[multiplier - 1]
        result = triplet + " " + result

    return result.strip()


def _extract_triplet(number, multiplier):
    smallest_first = str(number)[::-1]  # has python syntax gone too far?
    triplet = smallest_first[3*multiplier:(3*multiplier)+3][::-1]
    return int(triplet)


def _999_or_less(number):
    result = ""

    if number >= 100:
        hundred = int(str(number)[-3])
        result += f"{NUMBERS[hundred]} hundred "

    tens = int(str(number)[-2])
    if tens != 0:
        result += POWERS_OF_TEN[tens]

    ones = int(str(number)[-1])
    if ones != 0:
        result += " " + NUMBERS[ones]

    return result.strip()


print(numbers_to_words(1))
print(numbers_to_words(23))
print(numbers_to_words(145))
print(numbers_to_words(100))
print(numbers_to_words(32768))
print(numbers_to_words(32768 * 1024 * 2014))

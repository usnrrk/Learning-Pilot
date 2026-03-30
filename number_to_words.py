"""Convert numerals (including real numbers) to their English text equivalent."""

DIGIT_WORDS = [
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine",
]

ONES = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen",
]

TENS = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
]

SCALES = [
    (10**12, "trillion"),
    (10**9, "billion"),
    (10**6, "million"),
    (10**3, "thousand"),
    (10**2, "hundred"),
]


def number_to_words(n: int) -> str:
    if n < 0:
        return "negative " + number_to_words(-n)
    if n == 0:
        return "zero"

    parts = []
    for value, name in SCALES:
        if n >= value:
            count = n // value
            n %= value
            parts.append(number_to_words(count) + " " + name)

    if n >= 20:
        tens_part = TENS[n // 10]
        ones_part = ONES[n % 10]
        parts.append(tens_part + ("-" + ones_part if ones_part else ""))
    elif n > 0:
        parts.append(ONES[n])

    return " ".join(parts)


def real_number_to_words(text: str) -> str:
    """Convert a real number (given as a string) to English words.

    The integer part is converted normally. The fractional part is read
    digit by digit (e.g. 3.14 -> "three point one four").
    """
    negative = text.startswith("-")
    if negative:
        text = text[1:]

    if "." in text:
        int_part, frac_part = text.split(".", 1)
    else:
        int_part, frac_part = text, ""

    int_value = int(int_part) if int_part else 0
    result = number_to_words(int_value)

    if frac_part:
        frac_digits = " ".join(DIGIT_WORDS[int(d)] for d in frac_part)
        result += " point " + frac_digits

    if negative and (int_value != 0 or frac_part):
        result = "negative " + result

    return result


def main():
    print("Number to Words Converter")
    print("Enter a number (or 'q' to quit):\n")

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == "q":
            break

        try:
            float(user_input)  # validate it's a number
        except ValueError:
            print("Please enter a valid number.")
            continue

        print(real_number_to_words(user_input))
        print()


if __name__ == "__main__":
    main()

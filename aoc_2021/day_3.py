"""Day 3: Binary Diagnostic."""

SMALL_INPUT_FILE = 'input_small_day_3.txt'
FULL_INPUT_FILE = 'input_day_3.txt'


def get_input(filename: str) -> list[str]:
    """Gets puzzle input."""

    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def get_digits_at_each_bit(binary_nums: list[str]) -> list[str]:
    """Gets the digits at each bit."""

    return [''.join(bits) for bits in zip(*binary_nums)]


def get_digit_counts(digits: str) -> list[int]:
    """Counts the 0s and 1s at each bit."""

    count = [0] * 2
    for k in range(len(digits)):
        count[int(digits[k])] += 1

    return count


def solve_part1(filename: str) -> int:
    """Solves Part 1."""

    diagnostic_report = get_input(filename)
    num_length = len(diagnostic_report[0])

    gamma_rate = [''] * num_length
    epsilon_rate = [''] * num_length

    digits_at_each_bit = get_digits_at_each_bit(diagnostic_report)

    for i, digits in enumerate(digits_at_each_bit):
        count = get_digit_counts(digits)

        gamma_rate[i] = '0' if count[0] > count[1] else '1'
        epsilon_rate[i] = '0' if count[0] < count[1] else '1'

    gamma_bin = ''.join(gamma_rate)
    gamma_dec = int(gamma_bin, 2)

    epsilon_bin = ''.join(epsilon_rate)
    epsilon_dec = int(epsilon_bin, 2)

    return gamma_dec * epsilon_dec


def solve_part2(filename: str) -> int:
    """Solves Part 2."""

    diagnostic_report = get_input(filename)
    digits_at_each_bit = get_digits_at_each_bit(diagnostic_report)

    for i in range(len(digits_at_each_bit)):

        if i == 0:
            count = get_digit_counts(digits_at_each_bit[i])
            diagnostic_report = [
                num for num in diagnostic_report if num[i] == str(count.index(max(count)))]

        else:
            digits_at_each_bit = get_digits_at_each_bit(diagnostic_report)
            count = get_digit_counts(digits_at_each_bit[i])

            if count[0] == count[1]:
                diagnostic_report = [
                    num for num in diagnostic_report if num[i] == '1']
                oxygen_generator_rating = int(diagnostic_report[0], 2)
                break

            diagnostic_report = [
                num for num in diagnostic_report if num[i] == str(count.index(max(count)))]

    diagnostic_report = get_input(filename)
    digits_at_each_bit = get_digits_at_each_bit(diagnostic_report)

    for i in range(len(digits_at_each_bit)):

        if i == 0:
            count = get_digit_counts(digits_at_each_bit[i])
            diagnostic_report = [
                num for num in diagnostic_report if num[i] == str(count.index(min(count)))]

        else:
            digits_at_each_bit = get_digits_at_each_bit(diagnostic_report)
            count = get_digit_counts(digits_at_each_bit[i])

            if count[0] == count[1]:
                diagnostic_report = [
                    num for num in diagnostic_report if num[i] == '0']
                co2_scrubber_rating = int(diagnostic_report[0], 2)
                break

            diagnostic_report = [
                num for num in diagnostic_report if num[i] == str(count.index(min(count)))]

    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    print(f"Part 1: {solve_part1(FULL_INPUT_FILE)}")
    print(f"Part 2: {solve_part2(FULL_INPUT_FILE)}")

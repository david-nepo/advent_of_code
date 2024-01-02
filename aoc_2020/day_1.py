"""Day 1: Report Repair."""


def find_two_entries(expense_report: list[int]) -> int:
    """Finds the two entries that sum to 2020."""

    for i, expense_x in enumerate(expense_report):
        for expense_y in expense_report[i+1:]:
            if (expense_x + expense_y) == 2020:
                return expense_x, expense_y


def find_three_entries(expense_report: list[int]) -> int:
    """Finds the three entries that sum to 2020."""

    for i, expense_x in enumerate(expense_report):
        for expense_y in expense_report[i+1:]:
            for expense_z in expense_report[i+2:]:
                if (expense_x + expense_y + expense_z) == 2020:
                    return expense_x, expense_y, expense_z


if __name__ == "__main__":

    with open('input_day_1.txt', 'r', encoding='utf-8') as f:
        data = [int(num.strip()) for num in f.readlines()]

    entry1, entry2 = find_two_entries(data)
    entry_x, entry_y, entry_z = find_three_entries(data)

    print(f'{entry1 * entry2 =} ')
    print(entry_x * entry_y * entry_z)

    expense_report = ['a', 'b', 'c', 'd', 'e', 'f']
    for i, expense_x in enumerate(expense_report):
        for expense_y in expense_report[i+1:]:
            for expense_z in expense_report[i+2:]:
                print(expense_x, expense_y, expense_z)

import random

MAX_LINES = 3  # global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):  # the actual "slot machine"
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        col = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(value)
        columns.append(columns)

    return columns


def print_slot_machine(columns):  # printing from horizontal to vertical
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input('How much are you depositing? KES ')
        if amount.isdigit():  # check if the amount is actually a digit
            amount = int(amount)  # convert string to int
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number')

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            'Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')  # giving options to the max amount of lines
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # checking if the value is inbetween values
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number')

    return lines


def get_bet():  # checking if the bet is between the minimum and maximum bet amount

    while True:
        amount = input('How much would you like to bet one each line? KES ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f'Amount must be between KES {MIN_BET} - KES {MAX_BET}. ')
        else:
            print('Please enter a number')

    return amount


def main():  # call all functions
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: KES {balance}")
        else:
            break

    print(
        f'You are betting KES {bet} on {lines} lines. Total bet is equal to: KES {total_bet}')
    print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()

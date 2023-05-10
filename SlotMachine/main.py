MAX_LINES = 3  # global constant
MAX_BET = 100
MIN_BET = 1


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
        amount = input('What would you like to bet one each line? KES ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}. ')
        else:
            print('Please enter a number')

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_number_of_lines()
    print(balance, lines)


main()

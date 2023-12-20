import random

MAX_LINES = 3
MAX_BETS = 100
MIN_BETS = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= " ")

        print()
    

def deposit():
    while True:
        amount = input("The Amount that you would like to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The Amount must be greater than zero")
        else:
            print("Invalid Input, please enter a number")

    return amount

def get_number_of_lines():
    while True:
        no_of_lines = input("Select the number of lines to bet (1-" + str(MAX_LINES) + ")? ")
        if no_of_lines.isdigit():
            no_of_lines = int(no_of_lines)
            if no_of_lines > 0 and no_of_lines <= MAX_LINES:
                break
            else:
                print("The number of lines must be between (1 - 3)")
        else:
            print("Invalid Input, please enter a number")

    return no_of_lines

def getbet():
    while True:
        amount = input("Select the number of bets taken (1-" + str(MAX_BETS) + ")? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= MAX_BETS:
                break
            else:
                print("The number of lines must be between (1-" + str(MAX_BETS) + ")")
        else:
            print("Invalid Input, please enter a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = getbet()
        total_amount = bet * lines
        if total_amount>balance:
            print("You do not have enough to bet that amount, your current balance is", balance)    
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total amount is ${total_amount}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings} on {winning_lines} lines.")
    return winnings - total_amount

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")   
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()

import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
      symbol=columns[0][line]
      for column in columns:
         symbol_to_check=column[line]
         if symbol_to_check != symbol:
             break
      else:
          winnings+=values[symbol]*bet
          winning_lines.append(line+1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns, rows, cols):
    for r in range(len(columns[0])):
        for c in range(cols):
            if c != len(columns)-1:
               print(columns[c][r], end='|')
            else:
                print(columns[c][r])

def deposit():
    while True:
        amount= input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount= input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines=get_number_of_lines()
    while True:
       bet = get_bet()
       total= bet*lines
       if total > balance:
           print(f"You do not have enough to bet that amount, your current balance is ${balance}")
       else:
           break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total}")
    
    slots=get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots, ROWS, COLS)
    winnings, winning_lines=check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines", *winning_lines)
    return winnings - total

def main():
    balance=deposit()
    while True:
        print(f"Current balance is: {balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()

import time

from validations import ans_input_validation
from repository.balance_repository import init_db, add_balance, get_balance, get_history

def main_loop():
    init_db()
    while True:
        print("----------------------------------------")
        print("MENU:")
        print("1. Add Income")
        print("2. Add Outcome")
        print("3. View Balance")
        print("4. View Balance-Change History")
        print("5. Quit")

        ans = int(input())
        validator = ans_input_validation(ans)

        if not validator:
            print("Invalid input")
            continue

        if ans == 1:
            print("----------------------------------------")
            print("Income:")
            while True:
                income = input("Enter Income ['quit' to quit]: ")
                if income == "quit":
                    break
                print(f"Are you sure you want to add (yes/no) {income}?")
                ans = input().lower()
                if ans == "yes":
                    add_balance(income, "income") #TODO change to enum
                    print("Income added successfully")
                else:
                    print("Invalid command")
        elif ans == 2:
            print("----------------------------------------")
            print("Outcome:")
            while True:
                outcome = input("Enter Outcome ['quit' to quit]: ")
                if outcome == "quit":
                    break
                print(f"Are you sure you want to sub (yes/no) {outcome}?")
                ans = input().lower()
                if ans == "yes":
                    add_balance(outcome, "outcome")
                    print("Outcome added successfully")
                else:
                    print("Invalid command")
        elif ans == 3:
            print("----------------------------------------")
            print("Balance:")
            balance = get_balance()
            print(f"Current balance: {balance:.2f}")
        elif ans == 4:
            print("----------------------------------------")
            print("Balance-Change History:")
            for row in get_history():
                print(f"{row[3]} | {row[1].capitalize()} | {row[2]}")
        elif ans == 5:
            print("Disconnecting...")
            time.sleep(1)
            break
        else:
            print("Invalid command")
if __name__ == "__main__":
    main_loop()
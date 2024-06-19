from datetime import datetime
import pandas as pd

expenses = []
payments = []  

def add_expense(name, amount, description):
    if (description == ''):
        description = "none"
    expenses.append([name, amount, description, str(datetime.now())])
    print(f"\nAdded expense: {name} - {amount} - {description}")

def add_payment (name, amount, method, description):
    if (description == ''):
        description = "none"
    payments.append([name, amount, method, description, str(datetime.now())])
    print(f"\nAdded payment: {name} - {amount} - {method} - {description}")
    
def display_expenses(name):
    total_expenses = 0.0
    name_found = False

    for expense in expenses:
        if (expense[0] == name):
            name_found = True
            print(f"\nAmount: {expense[1]}\nDescription: {expense[2]}\nExpense date: {expense[3]}")
            total_expenses += expense[1]       
        elif (name == "all"):
            name_found = True
            print(f"\nName: {expense[0]}\nAmount: {expense[1]}\nDescription: {expense[2]}\nExpense date: {expense[3]}")
            total_expenses += expense[1]

    if (name_found != True):
        print(f"invalid name: {name}")
    else:    
        print(f"\nTotal expenses of {name}: {total_expenses}")

def display_payments(name):
    total_payments = 0.0
    name_found = False

    for payment in payments:
        if (payment[0] == name):
            name_found = True
            print(f"\nAmount: {payment[1]}\nPayment Method: {payment[2]}\nDescription: {payment[3]}\nPayment date: {payment[4]}")
            total_payments += payment[1]       
        elif (name == "all"):
            name_found = True
            print(f"\nName: {payment[0]}\nAmount: {payment[1]}\nPayment Method: {payment[2]}\nDescription: {payment[3]}\nPayment date: {payment[4]}")
            total_payments += payment[1]

    if (name_found != True):
        print(f"invalid name: {name}")
    else:    
        print(f"\nTotal payments of {name}: {total_payments}")

def display_shares():
    names = []
    for item in payments + expenses:
        if (item[0] not in names):
            names.append(item[0])
                
    if len(names) > 0:
        divisor = len(names)
    else:
        print("No transaction available")
        return
    
    total_expenses = sum(item[1] for item in expenses)
    total_payments = sum(item[1] for item in payments)
    balane_amount = total_payments - total_expenses
    share_per_person = total_expenses / divisor

    print(f"Total expenses: {total_expenses:.2f}")
    if balane_amount >= 0:
        print(f"Amount in hand: {balane_amount:.2f}")
    elif balane_amount < 0:
        print(f"Balance due: {-balane_amount:.2f}")
    print(f"Share per person ({divisor} pax): {share_per_person:.2f}")

    print()
    for name in names:
        total_payments = sum(item[1] for item in payments if item[0] == name)
        net_amount = total_payments - share_per_person

        if net_amount > 0:
            print(f"{name} needs to receive {net_amount:.2f}")
        elif net_amount < 0:
            print(f"{name} needs to pay {-net_amount:.2f}")
        else:
            print(f"{name}'s account balanced")
            
def save_to_excel(filename):
    try:
        excelname = f"{filename}.xlsx"
        payments_headings = ["Name", "Amount", "Method", "Description", "Date added"]
        expenses_headings = ["Name", "Amount", "Description", "Date added"]
        payments_df = pd.DataFrame(payments, columns=payments_headings)
        expenses_df = pd.DataFrame(expenses, columns=expenses_headings)

        with pd.ExcelWriter(excelname) as writer:
            payments_df.to_excel(writer, sheet_name='Payments', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        
        print(f"{excelname} has been added")
    except Exception as e:
        print("Invalid Filename")

def load_from_excel(filename):
    global payments, expenses
    try:
        excelname = f"{filename}.xlsx"
        payments_df = pd.read_excel(excelname, sheet_name='Payments')
        expenses_df = pd.read_excel(excelname, sheet_name='Expenses')

        payments = payments_df.values.tolist()
        expenses = expenses_df.values.tolist()

        print(f"Data loaded from {excelname}")
    except FileNotFoundError:
        print(f"{excelname} not found")


if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")

    while True:
        print("\n---- Menu ----")
        print("1. Add Expense" +
        "\n2. Add Payment" +
        "\n3. Display Expenses" +
        "\n4. Display Payments" +
        "\n5. Display Shares" +
        "\n6. Save Data As Excel" +
        "\n7. Load Data From Excel" +
        "\n8. Exit")

        choice = input("\nChoose an option: ")
        print("")

        if choice == '1':
            name = input("Enter payee name: ")
            if (len(name) == 0):
                print("Invalid name, please try again")
                continue
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Invalid amount, please try again")
                continue
            description = input("Enter expense description (Optional): ")
            add_expense(name, amount, description)
        elif choice == '2':
            name = input("Enter payee name: ")
            if (len(name) == 0):
                print("Invalid name, please try again")
                continue
            try:
                amount = float(input("Enter payment amount: "))
            except ValueError:
                print("Invalid amount, please try again")
                continue
            method = input("Enter payment method: ")
            if (len(method) == 0):
                print("invalid payment method, please try again")
                continue
            description = input("Enter payment description (Optional): ")
            add_payment(name, amount, method, description)
        elif choice == '3':
            name = input("Enter name (type \"all\" to print all): ")
            display_expenses(name)
        elif choice == '4':
            name = input("Enter name (type \"all\" to print all): ")
            display_payments(name)
        elif choice == '5':
            display_shares()
        elif choice == '6':
            filename = input("Enter filename to save data: ")
            save_to_excel(filename)
        elif choice == '7':
            filename = input("Enter filename to load data: ")
            load_from_excel(filename)
        elif choice == '8':
            print("Exiting Expense Tracker!")
            break
        else:
            print("Invalid choice, please try again")
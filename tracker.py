from datetime import datetime
import pandas as pd

expenses = []
payments = []  

def add_expense(name, amount, description="none"):
    expenses.append([name, amount, description, str(datetime.now())])
    print(f"\nAdded expense: {name} - {amount} - {description}")

def add_payment (name, amount, description="none"):
    payments.append([name, amount, description, str(datetime.now())])
    print(f"\nAdded payment: {name} - {amount} - {description}")
    
def display_expenses(name):
    total_expenses = 0.0
    for expense in expenses:
        if (expense[0] == name):
            print(f"- {expense}")
            total_expenses += expense[1]       
        elif (name == "all"):
            print(f"- {expense}")
            total_expenses += expense[1]
        else:
            print(f"invalid name: {name}")
        
    print(f"Total expenses of {name}: {total_expenses}")

def display_payments(name):
    total_payments = 0.0
    for payment in payments:
        if (payment[0] == name):
            print(f"- {payment}")
            total_payments += payment[1]       
        elif (name == "all"):
            print(f"- {payment}")
            total_payments += payment[1]
        else:
            print(f"invalid name: {name}")
        
    print(f"\nTotal payments of {name}: {total_payments}")

def display_shares():
    names = []
    for item in payments + expenses:
        if item[0] != names:
            names.append(item[0])
                
    if len(names) > 0:
        divisor = len(names)
    else:
        print("No names available")
        return
    
    total_expenses = sum(item[1] for item in expenses)
    share_per_person = total_expenses / divisor

    print(f"Total expenses: {total_expenses:.2f}")
    print(f"Each person's share: {share_per_person:.2f}")

    for name in names:
        total_payments = sum(item[1] for item in payments if item[0] == name)
        total_expenses = sum(item[1] for item in expenses if item[0] == name)
        balance_amount = total_payments - total_expenses
        net_amount = balance_amount - share_per_person

        print("")
        if net_amount > 0:
            print(f"{name} needs to receive {net_amount:.2f}")
        elif net_amount < 0:
            print(f"{name} needs to pay {-net_amount:.2f}")
        else:
            print(f"{name}'s account balanced")
            

def save_to_excel(filename):
    try:
        excelname = f"{filename}.xlsx"
        columns_headings = ["Name", "Amount", "Description", "Date and Time of Transaction"]
        payments_df = pd.DataFrame(payments, columns=columns_headings)
        expenses_df = pd.DataFrame(expenses, columns=columns_headings)

        with pd.ExcelWriter(excelname) as writer:
            payments_df.to_excel(writer, sheet_name='Payments', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        
        print(f"{excelname} has been added.")
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
        print(f"No data file found with the name {excelname}")


if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")

    while True:
        print("\n---- Menu ----")
        print("1. Add Expense" +
        "\n2. Add Payment" +
        "\n3. Display Expenses" +
        "\n4. Display Payments" +
        "\n5. Display Shares" +
        "\n6. Save Data as Excel" +
        "\n7. Load Data from Excel" +
        "\n8. Exit")

        choice = input("\nChoose an option: ")
        print("")

        if choice == '1':
            name = input("Enter the person name: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            add_expense(name, amount, description)
        elif choice == '2':
            name = input("Enter the person name: ")
            amount = float(input("Enter payment amount: "))
            description = input("Enter payment description: ")
            add_payment(name, amount, description)
        elif choice == '3':
            name = input("Enter the person name (type \"all\" to print all): ")
            display_expenses(name)
        elif choice == '4':
            name = input("Enter the person name (type \"all\" to print all): ")
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
            print("Invalid choice, please try again.")
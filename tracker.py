from datetime import datetime

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
        
    print(f"Total payments of {name}: {total_payments}")
       

if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")

    while True:
        print("\n---- Menu ----")
        print("1. Add Expense" +
        "\n2. Add Payment" +
        "\n3. Display Expenses" +
        "\n4. Display shares" +
        "\n5. Save Data" +
        "\n6. Load Data" +
        "\n7. Exit")

        choice = input("\nChoose an option: ")

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
            filename = input("Enter filename to save data: ")
            save_data(filename)
        elif choice == '6':
            filename = input("Enter filename to load data: ")
            load_data(filename)
        elif choice == '7':
            print("Exiting Expense Tracker!")
            break
        else:
            print("Invalid choice, please try again.")
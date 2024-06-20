from datetime import datetime # Retrieving datetime from computer 
import pandas as pd # Used for Excel compatibility

# Defining lists to store data
expenses = []
payments = []  


def add_expense(name, amount, description):
    """
    This function adds a new expense to the expenses list.

    Parameters:
    name (str): The name of the payee.
    amount (float): The amount of the expense.
    description (str): The description of the expense. If not provided, it defaults to "none".

    Returns:
    None

    Prints:
    A message indicating the successful addition of the expense.
    """
    if (description == ''): # Making the description optional
        description = "none"
    expenses.append([name, amount, description, str(datetime.now())])
    print(f"\nAdded expense: {name} - {amount} - {description}")

def add_payment (name, amount, method, description):
    """
    This function adds a new payment to the payments list.

    Parameters:
    name (str): The name of the payee.
    amount (float): The amount of the payment.
    method (str): The method of payment.
    description (str, optional): The description of the payment. Defaults to "none" if not provided.

    Returns:
    None

    Prints:
    A message indicating the successful addition of the payment.
    """
    if (description == ''): # Making the description optional
        description = "none"
    payments.append([name, amount, method, description, str(datetime.now())])
    print(f"\nAdded payment: {name} - {amount} - {method} - {description}")
    
def display_expenses(name):
    """
    This function prints all expenses of a specific person or all expenses if 'all' is provided.
    It also calculates and prints the total expenses of the specified person.

    Parameters:
    name (str): The name of the person whose expenses are to be displayed. If 'all' is provided, all expenses are displayed.

    Returns:
    None

    Prints:
    The amount, description, and date of each expense of the specified person.
    The total expenses of the specified person.
    A message indicating an invalid name if the provided name does not match any person's name.
    """
    total_expenses = 0.0 # Declaring a variable to hold the total amount of expenses
    name_found = False # Declaring a variable to validate the name

    for expense in expenses:
        if (expense[0] == name): # Checking the name matches the person name
            name_found = True
            print(f"\nAmount: {expense[1]}\nDescription: {expense[2]}\nExpense date: {expense[3]}")
            total_expenses += expense[1]       
        elif (name == "all"): # Printing all expenses
            name_found = True
            print(f"\nName: {expense[0]}\nAmount: {expense[1]}\nDescription: {expense[2]}\nExpense date: {expense[3]}")
            total_expenses += expense[1]

    if (name_found != True): # Prints an error message if name not found
        print(f"invalid name: {name}")
    else:    
        print(f"\nTotal expenses of {name}: {total_expenses}")

def display_payments(name):
    """
    This function prints all payments of a specific person or all payments if 'all' is provided.
    It also calculates and prints the total payments of the specified person.

    Parameters:
    name (str): The name of the person whose payments are to be displayed. If 'all' is provided, all payments are displayed.

    Returns:
    None

    Prints:
    The amount, payment method, description, and date of each payment of the specified person.
    The total payments of the specified person.
    A message indicating an invalid name if the provided name does not match any person's name.
    """
    total_payments = 0.0  # Declaring a variable to hold the total amount of payments
    name_found = False # Declaring a variable to validate the name

    for payment in payments:
        if (payment[0] == name): # Checking the name matches the person name
            name_found = True
            print(f"\nAmount: {payment[1]}\nPayment Method: {payment[2]}\nDescription: {payment[3]}\nPayment date: {payment[4]}")
            total_payments += payment[1]       
        elif (name == "all"): # Printing all payments
            name_found = True
            print(f"\nName: {payment[0]}\nAmount: {payment[1]}\nPayment Method: {payment[2]}\nDescription: {payment[3]}\nPayment date: {payment[4]}")
            total_payments += payment[1]

    if (name_found != True): # Prints an error message if name not found
        print(f"invalid name: {name}")
    else:    
        print(f"\nTotal payments of {name}: {total_payments}")

def display_shares():
    """
    This function calculates and prints the total expenses, total payments, balance amount, 
    and share per person. It also determines the net amount each person needs to receive or pay.

    Parameters:
    None

    Returns:
    None

    Prints:
    Total expenses, total payments, balance amount, share per person, and net amount for each person.
    A message indicating "No transaction available" if there are no transactions.
    """
    names = [] # Declared a list to keep track of the names of the transactions
    for item in payments + expenses:
        if (item[0] not in names): # Appending names without any duplicates
            names.append(item[0])
                
    if len(names) > 0: # Checkpoint for ZeroDivisionError
        divisor = len(names)
    else:
        print("No transaction available")
        return
    
    total_expenses = sum(item[1] for item in expenses) # Adds all the expense amounts
    total_payments = sum(item[1] for item in payments) # Adds all the payments amounts
    balane_amount = total_payments - total_expenses # Balance amount that is in hand
    share_per_person = total_expenses / divisor

    print(f"Total expenses: {total_expenses:.2f}")
    # Prints two different lines for better user understanding
    if balane_amount >= 0:
        print(f"Amount in hand: {balane_amount:.2f}")
    elif balane_amount < 0:
        print(f"Balance due: {-balane_amount:.2f}")
    print(f"Share per person ({divisor} pax): {share_per_person:.2f}")

    print() # Code clarity
    for name in names:
        total_payments = sum(item[1] for item in payments if item[0] == name) # Adds all the payments for each person
        net_amount = total_payments - share_per_person # Amount that needs to be paid or received for each person

        # Prints different lines for better user understanding
        if net_amount > 0:
            print(f"{name} needs to receive {net_amount:.2f}")
        elif net_amount < 0:
            print(f"{name} needs to pay {-net_amount:.2f}")
        else:
            print(f"{name}'s account balanced")
            
def save_to_excel(filename):
    """
    This function saves the current expenses and payments data into an Excel file.

    Parameters:
    filename (str): The name of the Excel file to be created. The ".xlsx" extension will be added automatically.

    Returns:
    None

    Prints:
    A message indicating the successful creation of the Excel file if no exceptions occur.
    An error message if an exception occurs, such as an invalid filename.

    Raises:
    Exception: If any other error occurs during the file operation.

    Note:
    The function uses pandas library to create and write data into the Excel file.
    """
    try:
        excelname = f"{filename}.xlsx"
        # Headings for each column of the file
        payments_headings = ["Name", "Amount", "Method", "Description", "Date added"]
        expenses_headings = ["Name", "Amount", "Description", "Date added"]
        # Creates a new Excel file with the specified filename
        payments_df = pd.DataFrame(payments, columns=payments_headings)
        expenses_df = pd.DataFrame(expenses, columns=expenses_headings)

        with pd.ExcelWriter(excelname) as writer:
            # Writes the data into the Excel file
            payments_df.to_excel(writer, sheet_name='Payments', index=False)
            expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        
        print(f"{excelname} has been added")
    except Exception as e:
        print("Invalid Filename")

def load_from_excel(filename):
    """
    This function loads the current expenses and payments data from an Excel file.

    Parameters:
    filename (str): The name of the Excel file to be loaded. The ".xlsx" extension will be added automatically.

    Returns:
    None

    Prints:
    A message indicating the successful loading of the data if the file exists.
    An error message if the file does not exist.

    Raises:
    FileNotFoundError: If the specified file does not exist.

    Note:
    The function uses pandas library to read data from the Excel file.
    The loaded data is stored in the global variables 'payments' and 'expenses'.
    """
    global payments, expenses # Declaring global variables to store the data
    try:
        excelname = f"{filename}.xlsx"
        # Reads the data from the Excel file
        payments_df = pd.read_excel(excelname, sheet_name='Payments')
        expenses_df = pd.read_excel(excelname, sheet_name='Expenses')

        # Converts the data into a list of lists
        payments = payments_df.values.tolist()
        expenses = expenses_df.values.tolist()

        print(f"Data loaded from {excelname}")
    except FileNotFoundError:
        print(f"{excelname} not found")


if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")

    # Menu that repeats until user enter 8 to exit
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
        print() # Code clarity

        if choice == '1':
            name = input("Enter payee name: ")
            if (len(name) == 0): # Make sure the name is valid
                print("Invalid name, please try again")
                continue
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError: # Make sure the amount is valid
                print("Invalid amount, please try again")
                continue
            description = input("Enter expense description (Optional): ")
            add_expense(name, amount, description)
        elif choice == '2':
            name = input("Enter payee name: ")
            if (len(name) == 0): # Make sure the name is valid
                print("Invalid name, please try again")
                continue
            try:
                amount = float(input("Enter payment amount: "))
            except ValueError: # Make sure the amount is valid
                print("Invalid amount, please try again")
                continue
            method = input("Enter payment method: ")
            if (len(method) == 0): # Make sure the method is valid
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
            print("Exiting Expense Tracker!") # Prints a thank you message and exits
            break
        else:
            print("Invalid choice, please try again") # Prints error message if there is no choice
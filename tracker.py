expenses = []
payment = []  


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
            display_shares(name)
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
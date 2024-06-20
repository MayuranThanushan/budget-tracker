# Expense Tracker

Welcome to the Expense Tracker! This program helps you manage and track your expenses and payments, calculate shares, and save or load data from Excel files. Below is a guide on how to use the program, including its functions and menu options.

## Features

- **Add Expense:** Record an expense with details such as name, amount, and description.
- **Add Payment:** Record a payment with details such as name, amount, payment method, and description.
- **Display Expenses:** View expenses for a specific person or  for all expenses.
- **Display Payments:** View payments for a specific person or for all payments.
- **Display Shares:** Calculate and display total expenses, payments, balance amount, share per person, and net amounts that a specific person needs to pay or recieve.
- **Save Data As Excel:** Save the current expenses and payments data into an Excel file.
- **Load Data From Excel:** Load expenses and payments data from an Excel file.

## Installation

1. Ensure you have Python installed on your computer.
2. Install the required libraries using pip:

    ```bash
    pip install pandas
    ```

## Usage

1. Run the program:

    ```bash
    python expense_tracker.py
    ```

2. Follow the on-screen menu to interact with the program.

## Functions

### add_expense

Adds a new expense to the expenses list.

**Parameters:**

- `name` (str): The name of the payee.
- `amount` (float): The amount of the expense.
- `description` (str): The description of the expense. Optional, defaults to "none".

### add_payment

Adds a new payment to the payments list.

**Parameters:**

- `name` (str): The name of the payee.
- `amount` (float): The amount of the payment.
- `method` (str): The method of payment.
- `description` (str): The description of the payment. Optional, defaults to "none".

### display_expenses

Prints all expenses of a specific person or all expenses if 'all' is provided. Calculates and prints the total expenses of the specified person.

**Parameters:**

- `name` (str): The name of the person whose expenses are to be displayed. If 'all' is provided, all expenses are displayed.

### display_payments

Prints all payments of a specific person or all payments if 'all' is provided. Calculates and prints the total payments of the specified person.

**Parameters:**

- `name` (str): The name of the person whose payments are to be displayed. If 'all' is provided, all payments are displayed.

### display_shares

Calculates and prints the total expenses, total payments, balance amount, and share per person. Determines the net amount each person needs to receive or pay.

### save_to_excel

Saves the current expenses and payments data into an Excel file.

**Parameters:**

- `filename` (str): The name of the Excel file to be created. The ".xlsx" extension will be added automatically.

### load_from_excel

Loads the current expenses and payments data from an Excel file.

**Parameters:**

- `filename` (str): The name of the Excel file to be loaded. The ".xlsx" extension will be added automatically.

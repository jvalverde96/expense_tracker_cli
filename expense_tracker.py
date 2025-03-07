import os
import pandas as pd
from datetime import datetime
import csv

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Generates the file name based on the specified year and month
def generate_file_name(year=None, month=None):
    if not os.path.exists("files"):
        os.makedirs("files")
    if not year or not month:
        today = datetime.today()
        year = today.year
        month = today.month
    return os.path.join("files", f"expenses_{year}_{month:02d}.csv")


# Creates the CSV file if it doesn't exist
def initialize_file(year=None, month=None):
    expense_file = generate_file_name(year, month)
    if not os.path.exists(expense_file):
        with open(expense_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount (Colones)", "Amount (Dollars)", "Description"])

# Adds a new expense entry to the CSV file
def add_expense():
    print("Add New Expense 💰")
    while True:
        date = input("Date (YYYY-MM-DD or press Enter for today): ") or datetime.today().strftime('%Y-%m-%d')
        # Validate date format
        try:
            # Try to parse the date with the expected format
            datetime.strptime(date, '%Y-%m-%d')
            break  # If no error, the date is valid, so break the loop
        except ValueError:
            print("\n⚠️ Invalid date format. Please use the format YYYY-MM-DD or press Enter for today.\n")

    category = input("Category: ")
    amount_colones = input("Amount in Colones: ") or 0
    amount_dollars = input("Amount in Dollars: ") or 0
    description = input("Description: ")

    # Check if amounts are valid numbers (including floats)
    try:
        amount_colones = float(amount_colones) if amount_colones != 0 else 0
        amount_dollars = float(amount_dollars) if amount_dollars != 0 else 0
    except ValueError:
        print("\n⚠️ Invalid amounts detected. Both amounts must be valid numbers (including decimals). Entry not added.\n")
        return
    
    # If the amount is zero, we can skip adding it
    amount_colones = amount_colones if amount_colones != 0 else ""
    amount_dollars = amount_dollars if amount_dollars != 0 else ""

    # Split the date into year, month, and day
    year, month, _ = date.split('-')

    # Convert year and month to integers for correct formatting
    year = int(year)
    month = int(month)

    # Initialize file before adding data
    initialize_file(year, month)

    expense_file = generate_file_name(year, month)

    with open(expense_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount_colones, amount_dollars, description])

    print(f"\n✅ Expense successfully added to {expense_file} file.\n")

# Displays expenses for a specific month
def view_expenses():
    print("View Expenses Per Month 📅")
    while True:
        date = input("View expenses for which (YYYY-MM): or press Enter for current month: ") or datetime.today().strftime('%Y-%m-%d')
        # Validate date format
        try:
            # Try to parse the date with the expected format
            datetime.strptime(date, '%Y-%m-%d')
            break  # If no error, the date is valid, so break the loop
        except ValueError:
            print("\n⚠️ Invalid date format. Please use the format YYYY-MM-DD or press Enter for current month.\n")
    # Split the month_year into year and month
    year, month = map(int, date.split('-'))
    
    # Get the month name
    month_name = month_names[month - 1]

    expense_file = generate_file_name(year, month)

    # Check if the file exists
    if not os.path.exists(expense_file):
        print("\n📌 No expenses recorded for that month.\n")
        return

    df = pd.read_csv(expense_file)

    # Display expenses in a table format
    print(f"\n📜 Expenses for {month_name} {year}:\n")
    print(df)

# Generates a monthly expense report
def generate_monthly_report():
    print("Generate a Summary of Expenses for a Specific Month. 📊")
    while True:
        date = input("Generate report for which month (YYYY-MM) or press Enter for current month): ") or datetime.today().strftime('%Y-%m-%d')

        # Validate date format
        try:
            # Try to parse the date with the expected format
            datetime.strptime(date, '%Y-%m-%d')
            break  # If no error, the date is valid, so break the loop
        except ValueError:
            print("\n⚠️ Invalid date format. Please use the format YYYY-MM-DD or press Enter for current month.\n")

    # Split the month_year into year and month
    year, month = map(int, date.split('-'))
    
    # Get the month name
    month_name = month_names[month - 1]
    
    expense_file = generate_file_name(year, month)

    # Check if the file exists
    if not os.path.exists(expense_file):
        print("\n📌 No expenses recorded for that month.\n")
        return
    
    # Load the data from the .csv file
    df = pd.read_csv(expense_file)

    # Convert the 'Amount (Colones)' and 'Amount (Dollars)' columns to numeric, handle errors if any
    df["Amount (Colones)"] = pd.to_numeric(df["Amount (Colones)"], errors="coerce").fillna(0)
    df["Amount (Dollars)"] = pd.to_numeric(df["Amount (Dollars)"], errors="coerce").fillna(0)

    # Calculate total expenses in both currencies
    total_colones = df["Amount (Colones)"].sum()
    total_dollars = df["Amount (Dollars)"].sum()

    # Display the report
    print(f"\n📊 Report for {month_name} {year}:")
    print(f"\n💰 Total Spent:")
    print(f"   - Colones: ₡{total_colones:.2f}")
    print(f"   - Dollars: ${total_dollars:.2f}\n")

    # Display all fields in the report
    print("📋 Full Expenses Report:")
    print(df)

def main():
    while True:
        # Display the main menu
        print("\n📌 Welcome to the Expense Tracker CLI tool 😁")
        print("\n")
        print("1️⃣  Add Expense 💰")
        print("2️⃣  View Expenses by Month 📅")
        print("3️⃣  Generate Monthly Report 📊")
        print("4️⃣  Exit ❌")
        
        choice = input("\nSelect an option: ")
        print("\n")

        # Execute the appropriate function based on user choice
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_monthly_report()
        elif choice == "4":
            print("\n👋 Exiting Expense Tracker. See you next time!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()

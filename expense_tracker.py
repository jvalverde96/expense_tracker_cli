import csv
import os
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# Generates the file name based on the current month and year
def generate_file_name():
    today = datetime.today()
    return f"expenses_{today.year}_{today.month:02d}.csv"

# Creates the CSV file if it doesn't exist and adds headers
def initialize_file():
    expense_file = generate_file_name()
    if not os.path.exists(expense_file):
        with open(expense_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount (Colones)", "Amount (Dollars)", "Description"])

# Adds a new expense entry to the CSV file
def add_expense():
    date = input("Date (YYYY-MM-DD or press Enter for today): ") or datetime.today().strftime('%Y-%m-%d')
    category = input("Category: ")
    amount_colones = input("Amount in Colones: ")
    amount_dollars = input("Amount in Dollars: ")
    description = input("Description: ")

    expense_file = generate_file_name()

    with open(expense_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount_colones, amount_dollars, description])
    
    print(f"\n✅ Expense successfully added to {expense_file} file.\n")

# Displays expenses for a specific month
def view_expenses():
    month = input("View expenses for which month (YYYY-MM): ") or datetime.today().strftime('%Y-%m')
    expense_file = f"expenses_{month.replace('-', '_')}.csv"

    # Check if the file exists
    if not os.path.exists(expense_file):
        print("\n📌 No expenses recorded for that month.\n")
        return

    df = pd.read_csv(expense_file)
    # Check if the file is empty
    if df.empty:
        print("\n📌 No expenses recorded yet.\n")
        return

    # Display expenses in a table format
    print(f"\n📜 Expenses for {month}:\n")
    print(tabulate(df, headers="keys", tablefmt="grid"))


# Generates a monthly expense report
def generate_monthly_report():
    """Generate a summary of expenses for a specific month."""
    month = input("Generate report for which month (YYYY-MM): ") or datetime.today().strftime('%Y-%m')
    expense_file = f"expenses_{month.replace('-', '_')}.csv"

    # Check if the file exists
    if not os.path.exists(expense_file):
        print("\n📌 No expenses recorded for that month.\n")
        return
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(expense_file)
    
    # Convert the 'Amount (Colones)' and 'Amount (Dollars)' columns to numeric, handle errors if any
    df["Amount (Colones)"] = pd.to_numeric(df["Amount (Colones)"], errors="coerce")
    df["Amount (Dollars)"] = pd.to_numeric(df["Amount (Dollars)"], errors="coerce")

    # Calculate total expenses in both currencies
    total_colones = df["Amount (Colones)"].sum()
    total_dollars = df["Amount (Dollars)"].sum()

    # Calculate category-wise summary in both currencies
    category_summary_colones = df.groupby("Category")["Amount (Colones)"].sum()
    category_summary_dollars = df.groupby("Category")["Amount (Dollars)"].sum()

    # Display the report in a table format
    print(f"\n📊 Report for {month}:")
    print(f"\n💰 Total Spent:")
    print(f"   - Colones: ₡{total_colones:.2f}")
    print(f"   - Dollars: ${total_dollars:.2f}\n")

    print("📋 Expenses by Category (Colones):")
    print(tabulate(category_summary_colones.reset_index(), headers=["Category", "Total (Colones)"], tablefmt="grid"))

    print("\n📋 Expenses by Category (Dollars):")
    print(tabulate(category_summary_dollars.reset_index(), headers=["Category", "Total (Dollars)"], tablefmt="grid"))


def main():
    initialize_file()
    while True:
        # Display the main menu
        print("\n📌 Expense Tracker CLI")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses by Month")
        print("3️⃣ Generate Monthly Report")
        print("4️⃣ Exit")
        
        choice = input("\nSelect an option: ")

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
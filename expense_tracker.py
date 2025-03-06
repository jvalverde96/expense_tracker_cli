import csv
import os
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# Generates the file name based on the current month and year
def generate_file_name():
    """Generate the CSV file name based on the current month and year."""
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

def main():
    initialize_file()
    print("Main")

if __name__ == "__main__":
    main()
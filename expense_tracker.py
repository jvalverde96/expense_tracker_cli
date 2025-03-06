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
    """Create the CSV file if it doesn't exist and add headers."""
    expense_file = generate_file_name()
    if not os.path.exists(expense_file):
        with open(expense_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount (Colones)", "Amount (Dollars)", "Description"])

def main():
    initialize_file()
    print("Main")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
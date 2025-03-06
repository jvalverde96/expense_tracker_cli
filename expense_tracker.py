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
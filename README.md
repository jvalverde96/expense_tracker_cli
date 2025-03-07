# Expense Tracker CLI Tool 📊💰

A simple, user-friendly command-line tool to track your monthly expenses. This tool allows you to add, view, and generate expense reports with ease. All data is saved in CSV format within a dedicated `files` folder.

---

## Features 🚀

- **Add Expense 💵**: Add an expense entry with details like date, category, amount in colones, amount in dollars, and description.
- **View Expenses 📅**: View expenses for a specific month in a neat table format.
- **Generate Monthly Report 📊**: Summarize the total expenses for a given month, including total spent in colones and dollars.
- **CSV File Storage 🗄️**: All expenses are stored in CSV format within the `files` directory, making it easy to manage and back up.
- **Easy Navigation 🧭**: The CLI interface makes it easy to navigate through the options to add expenses, view them, or generate reports.

---

## Installation 💻

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/expense-tracker-cli.git
    cd expense-tracker-cli
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For macOS/Linux
    .\venv\Scripts\activate    # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## How to Use 🧑‍💻

1. **Start the Tool**: To run the expense tracker tool, execute:

    ```bash
    python expense_tracker.py
    ```

2. **Options Menu**:
    - **Add Expense 💰**: Add a new expense to the tracker.
    - **View Expenses by Month 📅**: View the expenses recorded for a specific month.
    - **Generate Monthly Report 📊**: Generate a report summarizing total expenses for a given month.
    - **Exit ❌**: Exit the tool.

---

## Screenshots 📸

### Main Menu:

![image](https://github.com/user-attachments/assets/5779184b-16ef-47a0-bb7c-c2584e05da3c)

### Adding Expense:

![image](https://github.com/user-attachments/assets/c0c325ac-75d2-4c1b-bf76-275ffe49bb4e)

### View Expenses:

![image](https://github.com/user-attachments/assets/7c2ef7a1-d30b-4867-b8e8-e777a78dee7a)

### Monthly Report:

![image](https://github.com/user-attachments/assets/0d72c47b-4f40-497d-bf98-b8a825b9af50)

---

## Future Improvements 🌱

- **Automate Expense Addition 🤖**:
    - Currently, all expenses are manually entered. I plan to automate this process by integrating with bank accounts or third-party APIs to automatically add expenses based on transactions.

- **Expense Categories 💡**:
    - Introduce predefined categories for expenses to make categorization easier (e.g., Health, Food, Transportation).

- **Expense Notifications 📲**:
    - Set monthly budget goals and get notified when you are about to exceed your budget.

- **Currency Conversion 🌍**:
    - Integrate an API to automatically convert between different currencies, especially for international expenses.
---

## Technologies Used 💻

- **Python**: The core language for building the Expense Tracker CLI tool.
- **Pandas**: Used for reading and manipulating CSV data, performing calculations, and generating reports.



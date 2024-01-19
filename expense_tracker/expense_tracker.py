import json
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []
    return expenses

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=2)

def show_expenses(expenses):
    print("\nExpense List:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} | {expense['category']} | ${expense['amount']}")

def add_expense(expenses, category, amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nExpense added: {date} | {category} | ${amount}")

def view_spending_pattern(expenses):
    categories = set(expense['category'] for expense in expenses)
    
    print("\nSpending Pattern:")
    for category in categories:
        total_spent = sum(expense['amount'] for expense in expenses if expense['category'] == category)
        print(f"{category}: ${total_spent}")

def main():
    expenses = load_expenses()

    while True:
        print("\nOptions:")
        print("1. Show Expenses")
        print("2. Add Expense")
        print("3. View Spending Pattern")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_expenses(expenses)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
        elif choice == '3':
            view_spending_pattern(expenses)
        elif choice == '4':
            print("Exiting the expense tracker application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

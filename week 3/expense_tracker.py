import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    expenses = load_expenses()

    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense Added Successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No Expenses Found!")
        return

    print("\nExpense Records")
    print("-" * 50)

    for expense in expenses:
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ₹{expense['amount']}")
        print(f"Description : {expense['description']}")
        print("-" * 50)

def search_expense():
    expenses = load_expenses()

    category = input("Enter Category to Search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)
            found = True

    if not found:
        print("No Expenses Found!")

def total_expense():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total}")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")

main()

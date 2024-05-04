# Function to add an expense
def add_expense(expense_dict):
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    if amount <= 0:
        print("Invalid input. Please enter a valid number for the expense amount.")
    else:
        if category in expense_dict:
            expense_dict[category].append((name, amount))
        else:
            expense_dict[category] = [(name, amount)]
        print("Expense added successfully.")

# Function to view all expenses
def view_expenses(expense_dict):
    if not expense_dict:
        print("No expenses recorded yet.")
    else:
        print("Category\tExpense\tAmount")
        for category, expenses in expense_dict.items():
            for expense_details in expenses:
                print(f"{category}\t{expense_details[0]}\t{expense_details[1]}")

# Function to calculate total expenses
def total_expenses(expense_dict):
    total = sum(amount for expenses in expense_dict.values() for _, amount in expenses)
    print(f"Total expenses: {total}")

# Function to delete an expense
def delete_expense(expense_dict):
    category = input("Enter category to delete expense: ")
    if category in expense_dict:
        name = input("Enter expense name to delete: ")
        expenses = expense_dict[category]
        for expense_details in expenses:
            if expense_details[0] == name:
                expenses.remove(expense_details)
                print("Expense deleted successfully.")
                break
        else:
            print("Expense not found.")
    else:
        print("Category not found.")

# Function to search for an expense
def search_expense(expense_dict):
    name = input("Enter expense name to search: ")
    for category, expenses in expense_dict.items():
        for expense_details in expenses:
            if expense_details[0] == name:
                print(f"Expense found in {category} category: {expense_details[1]}")
                return
    print("Expense not found.")

# Function to set budget limits
def set_budget_limit(budget_limits):
    category = input("Enter category to set budget limit: ")
    limit = float(input("Enter budget limit: "))
    budget_limits[category] = limit
    print("Budget limit set successfully.")

# Main function
def main():
    expenses = {}
    budget_limits = {}
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Calculate total expenses")
        print("4. Delete an expense")
        print("5. Search for an expense")
        print("6. Set budget limit")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            search_expense(expenses)
        elif choice == "6":
            set_budget_limit(budget_limits)
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Call the main function directly
main()
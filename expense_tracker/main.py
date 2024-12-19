from expense_tracker import add_expense, view_expenses, update_expense, delete_expense, summarize_expenses

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Summarize Expenses")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            add_expense(date, amount, category, description)
            print("Expense added successfully!")
        
        elif choice == '2':
            expenses = view_expenses()
            print("\nID | Date       | Amount  | Category    | Description")
            print("-------------------------------------------------------")
            for row in expenses:
                print(f"{row[0]:<3}| {row[1]:<10}| ${row[2]:<7}| {row[3]:<10}| {row[4]}")
        
        elif choice == '3':
            expense_id = int(input("Enter expense ID to update: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            description = input("Enter new description (optional): ")
            update_expense(expense_id, date, amount, category, description)
            print("Expense updated successfully!")
        
        elif choice == '4':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully!")
        
        elif choice == '5':
            summary = summarize_expenses()
            print("\nCategory    | Total Spent")
            print("--------------------------")
            for row in summary:
                print(f"{row[0]:<10} | ${row[1]:.2f}")
        
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

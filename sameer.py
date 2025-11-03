"""
Expense Splitter (Roommates)
Uses: Data Types, Type Casting, Conditions, Loops, Functions,
Lambda/Map/Filter/Reduce, String, List, Tuple, Set, Dictionary
"""

from functools import reduce


expenses = []
roommates = set()
categories = ("Rent", "Food", "Bills", "Misc")
PASSWORD = "sameer"




def add_expense():
    print("\n--- Add Expense ---")
    exp_id = input("Enter Expense ID: ")
    item = input("Enter Item Name: ").strip()
    amount = float(input("Enter Amount: "))
    payer = input("Who Paid?: ").strip().capitalize()
    participants = input("Enter Participants (comma separated): ").title().split(",")
    date = input("Enter Date (DD-MM-YYYY): ")

    roommates.update([payer] + [p.strip() for p in participants])

    print("Categories:", categories)
    category = input("Enter Category: ").capitalize()
    if category not in categories:
        category = "Misc"

    expense = {
        "id": exp_id,
        "item": item,
        "amount": amount,
        "payer": payer,
        "participants": [p.strip() for p in participants],
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("✅ Expense Added Successfully!")


def modify_expense():
    print("\n--- Modify Expense ---")
    eid = input("Enter Expense ID: ")
    for exp in expenses:
        if exp["id"] == eid:
            new_amt = input("Enter new amount (leave blank to keep same): ")
            if new_amt:
                exp["amount"] = float(new_amt)
            exp["item"] = input("Enter new item (leave blank to keep same): ") or exp["item"]
            print("✅ Expense Modified!")
            return
    print("❌ Expense not found.")


def delete_expense():
    print("\n--- Delete Expense ---")
    eid = input("Enter Expense ID: ")
    for exp in expenses:
        if exp["id"] == eid:
            expenses.remove(exp)
            print("🗑️ Expense Deleted!")
            return
    print("❌ Expense not found.")


def view_reports():
    print("\n--- View Reports ---")
    print("1. Detailed Report\n2. Summary Report")
    ch = input("Enter choice: ")

    if ch == "1":
        print("\n--- Detailed Report ---")
        for e in expenses:
            print(f"{e['id']} | {e['item']} | ₹{e['amount']} | {e['payer']} | {e['category']} | {e['date']}")
    elif ch == "2":
        print("\n--- Summary Report ---")
        summary = {}
        for e in expenses:
            summary[e["payer"]] = summary.get(e["payer"], 0) + e["amount"]
        for k, v in summary.items():
            print(f"{k}: ₹{v:.2f}")
    else:
        print("Invalid choice.")


def breakdown():
    print("\n--- Individual Breakdown ---")
    for name in roommates:
        total_paid = sum(e["amount"] for e in expenses if e["payer"] == name)
        share = sum(e["amount"]/len(e["participants"]) for e in expenses if name in e["participants"])
        net = total_paid - share
        print(f"{name}: Paid ₹{total_paid:.2f}, Share ₹{share:.2f}, Net ₹{net:.2f}")


def search_expense():
    print("\n--- Search Expense ---")
    keyword = input("Enter item keyword: ").lower()
    found = list(filter(lambda e: keyword in e["item"].lower(), expenses))
    if found:
        for e in found:
            print(f"→ {e}")
    else:
        print("No matches found.")


def total_spent():
    if expenses:
        total = reduce(lambda a, b: a + b["amount"], expenses, 0)
        print(f"\n💰 Total Spent: ₹{total:.2f}")
    else:
        print("\nNo expenses recorded yet.")



def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add Expense")
        print("2. Modify Expense")
        print("3. Delete Expense")
        print("4. View Reports")
        print("5. Individual Breakdown")
        print("6. Search Expense")
        print("7. Total Spent")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            modify_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            view_reports()
        elif choice == "5":
            breakdown()
        elif choice == "6":
            search_expense()
        elif choice == "7":
            total_spent()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")



def login():
    for _ in range(3):
        pwd = input("Enter Password: ")
        if pwd == PASSWORD:
            print("✅ Login Successful!")
            main_menu()
            return
        else:
            print("❌ Wrong password, try again.")
    print("Access Denied.")



if __name__ == "__main__":
    login()

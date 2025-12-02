import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")

        # Data Storage
        self.income_list = []
        self.total_income = []
        self.reminders = []
        self.goals = []
        self.expense_list = []
        self.monthly_income = 0

        # -------------------- INCOME SECTION --------------------
        income_frame = tk.LabelFrame(root, text="Income", padx=10, pady=10)
        income_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        tk.Label(income_frame, text="(Monthly Income)").grid(row=0, column=0, sticky="e")
        self.monthly_income_entry = tk.Entry(income_frame)
        self.monthly_income_entry.grid(row=0, column=1, padx=5)

        tk.Button(income_frame, text="Set monthly", command=self.set_monthly_income).grid(row=0, column=2, padx=5)

        # -------------------- EXPENSE SECTION --------------------
        expense_frame = tk.LabelFrame(root, text="Expense", padx=10, pady=10)
        expense_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        tk.Label(expense_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.expense_name_entry = tk.Entry(expense_frame)
        self.expense_name_entry.grid(row=0, column=1, padx=5)

        tk.Label(expense_frame, text="Amount:").grid(row=1, column=0, sticky="e")
        self.expense_amount_entry = tk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=1, column=1, padx=5)

        tk.Label(expense_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="e")
        self.expense_date_entry = tk.Entry(expense_frame)
        self.expense_date_entry.grid(row=2, column=1, padx=5)

        tk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=5)

        

        # -------------------- REMINDER SECTION --------------------
        reminder_frame = tk.LabelFrame(root, text="Reminders", padx=10, pady=10)
        reminder_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        tk.Label(reminder_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.reminder_name_entry = tk.Entry(reminder_frame)
        self.reminder_name_entry.grid(row=0, column=1, padx=5)

        tk.Label(reminder_frame, text="Amount:").grid(row=1, column=0, sticky="e")
        self.reminder_amount_entry = tk.Entry(reminder_frame)
        self.reminder_amount_entry.grid(row=1, column=1, padx=5)

        tk.Label(reminder_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="e")
        self.reminder_date_entry = tk.Entry(reminder_frame)
        self.reminder_date_entry.grid(row=2, column=1, padx=5)

        tk.Button(reminder_frame, text="Add Reminder", command=self.add_reminders).grid(row=3, column=0, columnspan=2, pady=5)

        # -------------------- GOALS SECTION --------------------
        goals_frame = tk.LabelFrame(root, text="Goals", padx=10, pady=10)
        goals_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        tk.Label(goals_frame, text="Goal:").grid(row=0, column=0, sticky="e")
        self.goal_entry = tk.Entry(goals_frame)
        self.goal_entry.grid(row=0, column=1, padx=5)

        tk.Button(goals_frame, text="Add Goal", command=self.add_goal).grid(row=0, column=2, padx=5)

        # -------------------- OUTPUT SECTION --------------------
        self.output_frame = tk.Frame(root, padx=10, pady=10)
        self.output_frame.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Button(self.output_frame, text="Show Expenses", command=self.show_expenses).grid(row=2, column=0, pady=5)

        tk.Button(self.output_frame, text="Calculate Balance", command=self.display_balance).grid(row=0, column=0, padx=5)
        self.balance_label = tk.Label(self.output_frame, text="Balance: $0.00")
        self.balance_label.grid(row=0, column=1, padx=5)

        tk.Button(self.output_frame, text="Show Reminders", command=self.show_reminders).grid(row=1, column=0, pady=5)
        tk.Button(self.output_frame, text="Show Goals", command=self.show_goals).grid(row=1, column=1, pady=5)
    # -----------------------------------------------------------
    # LOGIC FUNCTIONS
    # -----------------------------------------------------------

    def update_balance_display(self):
        balance = self.calculate_balance()
        self.balance_label.config(text=f"Balance: ${balance:.2f}")

    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = self.expense_amount_entry.get()
        date = self.expense_date_entry.get()

        if not name or not amount or not date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        # Store expense as dictionary
        self.expense_list.append({
            "name": name,
            "amount": amount,
            "date": date
        })

        # Clear entry fields
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)
        self.expense_date_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Expense added!")
        self.update_balance_display()  

    def show_expenses(self):
        if not self.expense_list:
            messagebox.showinfo("Expenses", "No expenses added.")
            return

        # Create a new window
        window = tk.Toplevel(self.root)
        window.title("All Expenses")
        text_widget = tk.Text(window, width=60)
        text_widget.pack()

        # Header
        text_widget.insert(tk.END, "Name       | Amount     | Date\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")

        # Insert each expense
        for exp in self.expense_list:
            text_widget.insert(
                tk.END,
                f"{exp['name'].ljust(10)} | ${exp['amount']:.2f} | {exp['date']}\n"
            )

        text_widget.config(state="disabled")

    def add_reminders(self):
        name = self.reminder_name_entry.get()
        amount = self.reminder_amount_entry.get()
        date = self.reminder_date_entry.get()

        if not name or not amount or not date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be numeric.")
            return

        self.reminders.append({"name": name, "amount": amount, "date": date})

        self.reminder_name_entry.delete(0, tk.END)
        self.reminder_amount_entry.delete(0, tk.END)
        self.reminder_date_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Reminder added!")
        self.update_balance_display()

    def add_goal(self):
        goal = self.goal_entry.get()
        if goal:
            self.goals.append(goal)
            self.goal_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Goal added!")

    def set_monthly_income(self):
        try:
            amount = float(self.monthly_income_entry.get())
            self.monthly_income = amount
            self.monthly_income_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Monthly income set.")
            self.update_balance_display()

        except ValueError:
            messagebox.showerror("Error", "Invalid income amount.")

    def calculate_balance(self):
        # Sum all expenses
        total_expenses = sum(exp["amount"] for exp in self.expense_list)

        # Sum all reminders
        total_reminders = sum(rem["amount"] for rem in self.reminders)

        return self.monthly_income - total_expenses - total_reminders

        # Total goals
        total_goals = 0
        for goal in self.goals:
            try:
                total_goals += float(goal)  # assuming goal is a number
            except ValueError:
                continue  # ignore non-numeric goals

        # Determine status
        if balance < total_goals:
            status = "Behind goal"
        elif balance == total_goals:
            status = "On track"
        else:
            status = "Above goal"

        # Build popup
        popup = (
            f"Total Expenses: ${total_expenses:.2f}\n"
            f"Total Reminders: ${total_reminders:.2f}\n"
            f"Total Goals: ${total_goals:.2f}\n"
            f"Remaining Balance: ${balance:.2f}\n"
            f"Status: {status}"
        )

        messagebox.showinfo("Balance Details", popup)
        self.balance_label.config(text=f"Balance: ${balance:.2f} | {status}")


    def display_balance(self):
        balance = self.calculate_balance()

        total_expenses = sum(exp["amount"] for exp in self.expense_list)
        total_reminders = sum(rem["amount"] for rem in self.reminders)

        # Total goals
        total_goals = sum(float(goal) for goal in self.goals if self.is_number(goal))

        # Determine goal status
        if balance < total_goals:
            status = "Behind goal"
        elif balance == total_goals:
            status = "On track"
        else:
            status = "Above goal"

        popup = (
            f"Total Expenses: ${total_expenses:.2f}\n"
            f"Total Reminders: ${total_reminders:.2f}\n"
            f"Total Goals: ${total_goals:.2f}\n"
            f"Remaining Balance: ${balance:.2f}\n"
            f"Status: {status}"
        )

        messagebox.showinfo("Balance Details", popup)
        self.balance_label.config(text=f"Balance: ${balance:.2f} | {status}")

    def show_goals(self):
        if not self.goals:
            messagebox.showinfo("Goals", "No goals added.")
        else:
            messagebox.showinfo("Goals", "\n".join(self.goals))

    def show_reminders(self):
        if not self.reminders:
            messagebox.showinfo("Reminders", "No reminders added.")
            return

        window = tk.Toplevel(self.root)
        window.title("All Reminders")
        text_widget = tk.Text(window, width=60)
        text_widget.pack()

        text_widget.insert(tk.END, "Name       | Amount     | Date\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")

        for r in self.reminders:
            text_widget.insert(
                tk.END,
                f"{r['name'].ljust(10)} | ${str(r['amount']).rjust(8)} | {r['date']}\n"
            )

        text_widget.config(state="disabled")
    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

root = tk.Tk()
app = BudgetApp(root)
root.mainloop()
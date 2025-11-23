#Python work
from email.mime import text
import tkinter as tk
from tkinter import messagebox

import adding_income
from datetime import datetime

class budgetapp():
    def __init__(self, root):
        self.root = root
        self.root.title("Recording Income")
        self.reminder_amount_entry = tk.Entry(root)
        self.reminder_amount_entry.grid(row=2, column=1)
        self.reminder_date_entry = tk.Entry(root)
        self.reminder_date_entry.grid(row=2, column=5)

        self.income_list = []
        self.total_income = []
        self.reminders = []
        self.goals = []
        self.expense_list =[]

        # Income
        tk.Label(root, text= "Add Income").grid(row=0, column=0)
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1)

        tk.Button(root, text="Add", command=self.add_income).grid(row=0, column=2)
        tk.Label(root, text="Amount").grid(row=2, column=0)
        tk.Label(root,text="Date (YYYY-MM-DD)").grid(row=2, column=4)

        tk.Button(root,text="Add", command=self.add_reminders).grid(row=2,column=6)
    
        # Expense
        tk.Label(root, text="Add Expense").grid(row=1, column=0)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=1, column=1)
        tk.Button(root, text="Add", command=self.add_expense).grid(row=1, column=2)

        # reminders
        tk.Label(root, text="Add Reminder").grid(row=2, column=0)
        self.reminder_entry =tk.Entry(root)
        self.reminder_entry.grid(row=2, column=1)
        tk.Button(root, text="Add", command=self.add_reminders).grid(row=2, column=2)

        #Financial Goal
        tk.Label(root, text="Goal:").grid(row=3, column=0)
        self.goal_entry = tk.Entry(root)
        self.goal_entry.grid(row=3, column=1)
        tk.Button(root, text="Add", command=self.show_goals).grid(row=3, column=2)

        #Output
        tk.Button(root, text="Calculate Balance", command=self.display_balance).grid(row=4, column=0)
        self.balance_label = tk.Label(root, text='Balance: $0')
        self.balance_label.grid(row=4, column=1)

        tk.Button(root,text="Show Reminders", command=self.show_reminders).grid(row=5, column=0)
        tk.Button(root, text="Show Goals", command=self.show_goals).grid(row=5, column=1)

        # Name
        tk.Label(root, text="Name").grid(row=2, column=0)
        self.reminder_name_entry = tk.Entry(root)
        self.reminder_name_entry.grid(row=2, column=1)

        # Reminder Description
        tk.Label(root, text="Reminder").grid(row=2, column=2)
        self.reminder_entry = tk.Entry(root)
        self.reminder_entry.grid(row=2, column=3)

        # Amount
        tk.Label(root, text="Amount").grid(row=2, column=4)
        self.reminder_amount_entry = tk.Entry(root)
        self.reminder_amount_entry.grid(row=2, column=5)

        # Date
        tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=6)
        self.reminder_date_entry = tk.Entry(root)
        self.reminder_date_entry.grid(row=2, column=7)

        # Add button
        tk.Button(root, text="Add", command=self.add_reminders).grid(row=2, column=8)
        
    def add_income(self):
        try:
            income = float(self.income_entry.get())
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.income_list.append((income, date))
            self.total_income.append(income)
            messagebox.showinfo("Success", f"Income of ${income} added on {date}.")
            self.income_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for income.")

    def add_expense(self):
        try:
            amount = float(self.expense_entry.get())
            self.expense_list.append(amount)
            self.expense_entry.delete(0, tk.END)
            messagebox.showinfo("Success",f"Expense of ${amount} added.")
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number.")
        
    def add_reminders(self):
         # Strip inputs
        name = self.reminder_name_entry.get().strip()
        text = self.reminder_entry.get().strip()
        amount_text = self.reminder_amount_entry.get().strip()
        date_text = self.reminder_date_entry.get().strip()

        # Validate inputs
        if not name:
            messagebox.showerror("Error", "Enter a name for the reminder.")
            return
        if not text:
            messagebox.showerror("Error", "Enter a reminder description.")
            return

        # Clean and validate amount
        cleaned_amount = amount_text.replace(',', '').replace('$', '')
        try:
            amount = float(cleaned_amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number (example: 50, 1000, or 12.99).")
            return

        # Validate date
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format.\nUse YYYY-MM-DD (example: 2025-03-01).")
            return

        # Store reminder as tuple: (name, description, amount, date)
        self.reminders.append((name, text, amount, date_text))

        # Clear fields
        self.reminder_name_entry.delete(0, tk.END)
        self.reminder_entry.delete(0, tk.END)
        self.reminder_amount_entry.delete(0, tk.END)
        self.reminder_date_entry.delete(0, tk.END)

        # Success message
        messagebox.showinfo("Success", f"Reminder added:\nName: {name}\n{text}\n${amount}\n{date_text}")

    def show_goals(self):
        if not self.goals:
            messagebox.showinfo("Goals", "No goals added.")
            return
        messagebox.showinfo("Goals", "\n".join(self.goals))
    def calculate_balance(self):
        total_income = sum(float(i) for i in self.total_income)
        total_expenses = sum(float(e) for e in self.expense_list)

        total_reminders = sum(float(r) for r in self.reminders)
        
        # if there are no expense, subtact reminders instead 
        if not total_expenses:
            total_expenses == 0 
            balance = total_income -total_reminders
        else:
            balance = total_income -total_expenses

        return balance
       
    def display_balance(self):
        balance = self.calculate_balance()
        self.balance_label.config(text=f"Balance: ${balance:.2f}")
        
    def show_reminders(self):
        
        if not self.reminders:
            messagebox.showinfo("Reminders", "No reminders added.")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Reminders")
        text_widget = tk.Text(window, width=60)
        text_widget.pack()

        text_widget.insert(tk.END, "Name       | Description       | Amount    | Date\n")
        text_widget.insert(tk.END, "-"*50 + "\n")
        for name, desc, amount, date in self.reminders:
            text_widget.insert(tk.END, f"{name.ljust(10)} | {desc.ljust(16)} | ${str(amount).rjust(8)} | {date}\n")

        text_widget.config(state="disabled")
  #run app
root = tk.Tk()
app = budgetapp(root)
root.mainloop()
  
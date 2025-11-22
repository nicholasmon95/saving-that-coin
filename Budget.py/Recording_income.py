#Python work
import tkinter as tk
from tkinter import messagebox

import adding_income

class budgetapp():
    def __init__(self, root):
        self.root = root
        self.root.title("Recording Income")

        self.income_list = []
        self.total_income = []
        self.reminders = []
        self.goals = []
        self.expense_list =[]

        # Income
        tk.Label(root, text= "Add Income").grid(row=0, column=0)
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1)
        tk.Button(root, text="Add Income", command=self.add_income).grid(row=0, column=2)
    
        # Expense
        tk.Label(root, text="Add Expense").grid(row=1, column=0)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=1, column=1)
        tk.Button(root, text="Add", command=self.add_reminders).grid(row=2, column=2)

        #Bill reminders
        tk.Label(root, text="Add Bill Reminder").grid(row=2, column=0)
        self.reminder_entry =tk.Entry(root)
        self.reminder_entry.grid(row=2, column=1)
        tk.Button(root, text="Add", command=self.add_reminders).grid(row=2, column=2)

        #Financial Goal
        tk.Label(root, text="Goal:").grid(row=3, column=0)
        self.goal_entry = tk.Entry(root)
        self.goal_entry.grid(row=3, column=1)
        tk.Button(root, text="Add", command=self.add_goal).grid(row=3, column=2)

        #Output
        tk.Button(root, text="Calculate Balance", command=self.calculate_balance).grid(row=4, column=0)
        self.balance_label = tk.Label(root, text='Balance: $0')
        self.balance_label.grid(row=4, column=1)

        tk.Button(root,text="Show Reminders", command=self.show_reminders).grid(row=5, column=0)
        tk.Button(root, text="Show Goals", command=self.show_goals).grid(row=5, column=1)
    
    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.income_list.append(income)
            self.total_income.append(income)
            messagebox.showinfo("Success", f"Income of ${income} added.")
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
        text = self.reminder_entry.get()
        if text:
            self.reminders.append(text)
            self.reminder_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Reminders added.")
        else:
            messagebox.showerror("Error", "Enter a reminders description.")

    def add_goal(self):
        text = self.goal_entry.get()
        if text:
            self.goals.append(text)
            self.goal_entry.delete(0, tk.END)
            messagebox.showinfo("Added", "Goal added!")
        else:
            messagebox.showerror("Error", "Enter a goal description.")
    def calculate_balance(self):
        total_income = sum(self.total_income)
        total_expenses = sum(self.expense_list)
        balance = total_income -total_expenses
        self.balance_label.config(text=f"Balance: ${balance:.2f}")
        
    def show_reminders(self):
        messagebox.showinfo("Reminders", "\n".join(self.reminders) if self.reminders else "No reminders added.")
    def show_goals(self):
        messagebox.showinfo("Goals", "\n".join(self.reminders) if self.reminder else"no reminders added.")
    def show_goals(self):
        messagebox.showinfo("Goals", "\n".join(self.goals) if self.goals else "no goals added.")


# Run the app
root = tk.Tk()
app = budgetapp(root)
root.mainloop()
  
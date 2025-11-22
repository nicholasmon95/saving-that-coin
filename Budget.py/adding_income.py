import tkinter as tk
from tkinter import messagebox


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
    
def add_reminder(self):
    text = self.reminder_entry.get()
    if text:
        self.reminder.append(text)
        self.reminder_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Reminder added.")
    else:
        messagebox.showerror("Error", "Enter a reminder description.")

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

#Python work
import tkinter as tk
from tkinter import messagebox


class recordingincome:
 def __init__(self, root):
  self.root = root
  self.root.title("Recording Income")

  self.income_list = []
  self.total_income = []
  self.reminders = []
  self.goals = []

  # Income
  tk.Label(root, text= "Add Income").grid(row=0, column=0)
  self.income_entry = tk.Entry(root)
  self.income_entry.grid(row=0, column=1)
  tk.Button(root, text="Add Income", command=self.add_income).grid(row=0, column=2)
  
  # Expense
  tk.Label(root, text="Add Expense").grid(row=1, column=0)
  self.expense_entry = tk.Entry(root)
  self.expense_entry.grid(row=1, column=1)
  tk.Button(root, text="Add", command=self.add_reminder).grid(row=2, column=2)

  #Bill reminder
  tk.Label(root, text="Add Bill Reminder").grid(row=2, column=0)
  self.reminder_entry =tk.Entry(root)
  self.reminder_entry.grid(row=2, column=1)
  tk.Button(root, text="Add", command=self.add_reminder).grid(row=2, column=2)

  #Financial Goal
  tk.Label(root, text="Goal:").grid(row=3, column=0)
  self.goal_entry = tk.Entry(root)
  self.goal_entry.grid(row=3, column=1)
  tk.Button(root, text="Add", command=self.add_goal).grid(row=3, column=2)
  
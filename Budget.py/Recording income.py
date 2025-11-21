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


# saving-that-coin
This is a program for the first part of my capstone project about saving/budgeting. 
# Budget App (Tkinter-Based Personal Finance Tool)

## 📌 Overview
This Python application is a graphical budget management tool that allows users to track **monthly income, expenses, reminders, and financial goals**. It provides a simple interface using `Tkinter`, making it easy for users to enter financial information and instantly see their remaining balance.

The program automatically calculates the user's current balance by subtracting expenses and reminders from the set monthly income. It is designed for beginners who want a hands-on approach to learning financial management and GUI programming in Python.

---

## 🛠 Features

### ✔ Income Management
- Set a monthly income amount
- Automatically updates balance when income changes

### ✔ Expense Tracking
- Add expenses with:
  - **Name**
  - **Amount**
  - **Date (YYYY-MM-DD)**
- View all expenses in a separate window

### ✔ Reminders
- Schedule reminders with:
  - **Name**
  - **Amount**
  - **Date**
- Display all reminders in a popup window
- Prevents visual overlap issues

### ✔ Financial Goals
- Add custom financial goals
- Program compares your balance to your goals and shows status:
  - `Behind goal`
  - `On track`
  - `Above goal`

### ✔ Balance Calculation
- Computes remaining balance:  
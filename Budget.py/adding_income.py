def add_income(self):
    try:
        income = float(self.income_entry.get())
        self.income_list.append(income)
        self.total_income.append(income)
        messagebox.showinfo("Success", f"Income of ${income} added.")
        self.income_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for income.")
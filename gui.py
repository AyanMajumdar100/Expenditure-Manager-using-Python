import tkinter as tk
from tkinter import ttk, messagebox
from storage import load_expenditures, save_expenditures
from utils import validate_date, validate_amount

class ExpenditureManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expenditure Manager")
        self.expenditures = load_expenditures()
        self.create_widgets()
        self.populate_treeview()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.master, columns=('ID', 'Date', 'Category', 'Amount', 'Description'), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        form_frame = tk.Frame(self.master)
        form_frame.pack(pady=10)

        labels = ["Date (YYYY-MM-DD):", "Category:", "Amount:", "Description:"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label] = entry

        tk.Button(self.master, text="Add Expenditure", command=self.add_expenditure).pack(pady=5)

        year_frame = tk.Frame(self.master)
        year_frame.pack(pady=10)

        tk.Label(year_frame, text="Year:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.year_entry = tk.Entry(year_frame)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(year_frame, text="Find Total Expenditure by Year", command=self.find_total_by_year).grid(row=0, column=2, padx=5, pady=5)

    def add_expenditure(self):
        date, category, amount, description = [self.entries[label].get() for label in self.entries]
        if not validate_date(date):
            messagebox.showwarning("Input Error", "Invalid date format. Use YYYY-MM-DD.")
            return
        if not validate_amount(amount):
            messagebox.showwarning("Input Error", "Invalid amount. Ensure it is a positive number.")
            return

        expenditure = {
            'id': len(self.expenditures) + 1,
            'date': date,
            'category': category,
            'amount': float(amount),
            'description': description
        }

        self.expenditures.append(expenditure)
        save_expenditures(self.expenditures)
        self.populate_treeview()
        self.clear_entries()

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for exp in self.expenditures:
            self.tree.insert('', tk.END, values=(exp['id'], exp['date'], exp['category'], exp['amount'], exp['description']))

    def find_total_by_year(self):
        year = self.year_entry.get()
        if not year.isdigit() or len(year) != 4:
            messagebox.showwarning("Input Error", "Invalid year format. Use YYYY.")
            return
        total = sum(exp['amount'] for exp in self.expenditures if exp['date'].startswith(year))
        messagebox.showinfo("Total Expenditure", f"Total expenditure for {year}: {total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenditureManagerApp(root)
    root.mainloop()

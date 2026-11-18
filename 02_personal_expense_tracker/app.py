from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import date

app = Flask(__name__)
DATA_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=2)


@app.route("/")
def index():
    expenses = load_expenses()
    total = sum(float(item["amount"]) for item in expenses)
    return render_template("index.html", expenses=expenses, total=total, today=date.today().isoformat())


@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "Other")
    expense_date = request.form.get("expense_date") or date.today().isoformat()
    try:
        amount = float(request.form.get("amount", "0"))
    except ValueError:
        amount = 0

    if title and 0 < amount <= 100000000:
        expenses = load_expenses()
        expenses.append({
            "id": max([item.get("id", 0) for item in expenses], default=0) + 1,
            "title": title,
            "category": category,
            "date": expense_date,
            "amount": round(amount, 2)
        })
        save_expenses(expenses)
    return redirect(url_for("index"))


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expenses = [item for item in load_expenses() if item.get("id") != expense_id]
    save_expenses(expenses)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

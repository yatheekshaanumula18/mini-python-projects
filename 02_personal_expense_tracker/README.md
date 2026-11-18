# Personal Expense Tracker

A small web app built with Python Flask, HTML, and CSS. Add expenses, choose a category, view the total, and delete entries. Data is stored locally in `expenses.json`.

## Requirements
- Python 3.8 or newer
- pip

## Install and run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open the local address printed in the terminal (usually http://127.0.0.1:5000).

## Project structure
- `app.py` - Flask routes and expense storage
- `templates/index.html` - page layout
- `static/style.css` - styling
- `expenses.json` - created automatically when you add an expense

## Note
This is a learning project, not a financial or accounting system. The Flask development server is for local learning only; do not deploy it publicly with debug mode enabled.

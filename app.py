from flask import Flask, render_template
import sqlite3
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('credit_cards.db')
    c = conn.cursor()

    # Retrieve all cards
    c.execute("SELECT * FROM cards")
    rows = c.fetchall()

    # Get the current month and year
    now = datetime.datetime.now()
    current_month = now.month
    current_year = now.year

    # Calculate which payments are due this month and the total minimum due
    due_this_month = []
    total_minimum_due = 0
    for row in rows:
        if len(row[2]) > 10:
            payment_due_date_time = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
        else:
            payment_due_date_time = datetime.datetime.strptime(row[2], '%Y-%m-%d')
            #row[1] = round(row[1], 2)
        payment_due_month = payment_due_date_time.month
        payment_due_year = payment_due_date_time.year
        if payment_due_month == current_month and payment_due_year == current_year and payment_due_date_time > datetime.datetime.now():
            due_this_month.append(row[0])  # Add the card name to the list
            total_minimum_due += round(row[3], 2)  # Add the minimum payment to the total
            
    total_minimum_due = round(total_minimum_due, 2)
    # Close the connection
    conn.close()

    # Render the HTML template with the card data, payment due dates, and total minimum due
    return render_template('index.html', cards=rows, due_this_month=due_this_month, current_month=current_month, current_year=current_year, total_minimum_due=round(total_minimum_due,2))


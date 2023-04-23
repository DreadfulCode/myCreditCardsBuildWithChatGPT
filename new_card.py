import sqlite3

# Create connection to database
conn = sqlite3.connect('credit_cards.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS cards
             (card_name TEXT, balance REAL, payment_due_date_time TEXT, minimum_payment REAL)''')

# Get inputs from user
card_name = input("Enter the name of the credit card: ")
balance = float(input("Enter the balance: "))
payment_due_date_time = input("Enter the payment due date and time (YYYY-MM-DD HH:MM:SS): ")
minimum_payment = float(input("Enter the minimum payment: "))

# Insert values into table
c.execute("INSERT INTO cards (card_name, balance, payment_due_date_time, minimum_payment) VALUES (?, ?, ?, ?)",
          (card_name, balance, payment_due_date_time, minimum_payment))

# Commit changes and close connection
conn.commit()
conn.close()

print("Credit card information saved to database.")


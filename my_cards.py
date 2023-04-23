import sqlite3

# Create connection to database
conn = sqlite3.connect('credit_cards.db')
c = conn.cursor()

# Retrieve data from table and print
c.execute("SELECT * FROM cards")
rows = c.fetchall()
for row in rows:
    print("Card name:", row[0])
    print("Balance:", row[1])
    print("Payment due date and time:", row[2])
    print("Minimum payment:", row[3])
    print()

# Close connection
conn.close()


import sqlite3

# Connect to the database
conn = sqlite3.connect('credit_cards.db')
c = conn.cursor()

# Retrieve all cards and print their ids and names
c.execute("SELECT rowid, card_name FROM cards")
rows = c.fetchall()
if not rows:
    print("No cards found in database.")
else:
    print("Please select a card to update:")
    for row in rows:
        print(f"{row[0]}) {row[1]}")

    # Prompt user to select card to update
    card_id = input("Enter the id of the card you want to update: ")

    try:
        card_id = int(card_id)
    except ValueError:
        print("Invalid input: Please enter a numeric value.")
        exit(1)

    # Check if the card exists in the table
    c.execute("SELECT * FROM cards WHERE rowid = ?", (card_id,))
    row = c.fetchone()

    if row:
        # If the card exists, prompt the user to update the fields
        balance = input("Enter the new balance for the card: ")
        payment_due_date_time = input("Enter the new payment due date and time for the card (YYYY-MM-DD HH:MM:SS): ")
        minimum_payment = input("Enter the new minimum payment for the card: ")

        # Update the card's information in the table
        c.execute("UPDATE cards SET balance = ?, payment_due_date_time = ?, minimum_payment = ? WHERE rowid = ?", (balance, payment_due_date_time, minimum_payment, card_id))
        conn.commit()

        print("Card information updated successfully.")
    else:
        print("Card not found.")

# Close the connection
conn.close()


import sqlite3
import DataBase

# This function works:
# - Connect to the database
# - Create the table 'Clients' if it does not exist  
#   Rows:
#     - Full_name
#     - Number_phone
#     - Date
#     - Dimensions_of_metal
#     - Price_has_been_paid
# - Insert data
# - Save the changes and close the connection
def Create_and_add_clients_data(Dimensions_of_metal, Full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment):  
    try:
        # Connect to the database
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        # Create the Clients table if it does not exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            Number INTEGER PRIMARY KEY AUTOINCREMENT,
            Dimensions_of_metal TEXT NOT NULL,
            Full_name TEXT NOT NULL,
            Number_phone TEXT NOT NULL,
            Number_of_items TEXT NOT NULL,
            Date TEXT NOT NULL,
            Price_has_been_paid TEXT NOT NULL,
            Comment TEXT NOT NULL
        )
        ''')

        # Insert data into the Clients table
        cursor.execute('''
        INSERT INTO Clients (Dimensions_of_metal, Full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (Dimensions_of_metal, Full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment))

        # Commit the changes
        conn.commit()
        return "Data inserted successfully."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        # Close the connection
        conn.close()
        
# Instance of DataHandling
dt = DataBase.DataHandling("clients.db")
        
def remove_data_in_db_client(data):
    try:
        # Split the data and remove the first element
        data = data.split(" ")[0]
        dt.data_delete("Clients", int(data))
    except Exception as e:
        return f"An error occurred while deleting data: {e}"


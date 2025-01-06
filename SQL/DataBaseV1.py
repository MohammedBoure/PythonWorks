import sqlite3

def insert_data_employees(Full_name_of_the_employee, Employee_task, description, been_worked_on):
        try:
            # Connect to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            # Create the table if it does not exist
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Types_of_buildings (
                number_of_employee INTEGER PRIMARY KEY AUTOINCREMENT,
                Full_name_of_the_employee TEXT NOT NULL,
                Employee_task TEXT NOT NULL,
                description TEXT,
                been_worked_on TEXT NOT NULL
            )
            ''')

            # Insert data
            cursor.execute('''
            INSERT INTO Types_of_buildings (Full_name_of_the_employee, Employee_task, description, been_worked_on)
            VALUES (?, ?, ?, ?)
            ''', (Full_name_of_the_employee, Employee_task, description, been_worked_on))

            # Save the changes and close the connection
            conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


class DataHandling:

    def __init__(self, option):
        self.option = option

    def selected_row(self, num_row):
        try:
            if self.option == "row":
                # Establish a connection to the database
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()

                # Retrieve a single row using the correct table and column name
                cursor.execute('SELECT * FROM Types_of_buildings WHERE number_of_employee = ?', (num_row,))
                row = cursor.fetchone()

                if row:
                    print(row)
                else:
                    print(f"No data found for number_of_employee = {num_row}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    def data_delete(self, num_row):
        try:
            if self.option == "row":
                # Establish a connection to the database
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()

                # Delete a row using the correct table and column name
                cursor.execute('DELETE FROM Types_of_buildings WHERE number_of_employee = ?', (num_row,))
                conn.commit()  # Save changes to the database

                # Check if any rows were affected
                if cursor.rowcount > 0:
                    print(f"Row with number_of_employee = {num_row} deleted successfully.")
                else:
                    print(f"No data found for number_of_employee = {num_row}.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

# Create an instance of DataHandling with the option "row"
dt = DataHandling("row")


# Fetch and print data for rows 0 through 29
for i in range(1,4):
    dt.selected_row(i)





    

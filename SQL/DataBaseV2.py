import sqlite3

def insert_data_employees(Full_name_of_the_employee, number_phone, date, Type_of_car, description, been_worked_on,prix):
    try:
        # Connect to the database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Create the table if it does not exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Types_of_buildings (
            number_of_employee INTEGER PRIMARY KEY AUTOINCREMENT,
            Full_name_of_the_employee TEXT NOT NULL,
            number_phone TEXT NOT NULL,
            date TEXT NOT NULL,
            Type_of_car TEXT NOT NULL,
            description TEXT,
            been_worked_on TEXT NOT NULL,
            prix TEXT NOT NULL
        )
        ''')

        # Insert data
        cursor.execute('''
        INSERT INTO Types_of_buildings (Full_name_of_the_employee, number_phone, date, Type_of_car, description, been_worked_on,prix)
        VALUES (?, ?, ?, ?, ?, ?,?)
        ''', (Full_name_of_the_employee, number_phone, date, Type_of_car, description, been_worked_on,prix))

        # Save the changes and close the connection
        conn.commit()
        return "Data inserted successfully."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        conn.close()



class DataHandling:

    def __init__(self, option):
        self.option = option


    def display_all_data(self):
        try:
            # Connect to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            # Fetch all data from the table
            cursor.execute('SELECT * FROM Types_of_buildings')
            rows = cursor.fetchall()  # Fetch all rows from the query result

            if rows:
                # Print the column headers
                column_names = [description[0] for description in cursor.description]
                header = ' | '.join(column_names)

                # Gather all rows into a single string
                data = '\n'.join(' | '.join(map(str, row)) for row in rows)
                
                # Combine header and data
                result = f"{header}\n{data}"
                return result
            else:
                return "No data found."
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()


    def edit_data_row(self, name_table, num_row, column_name=None, new_value=None):
        try:
            # Establish a connection to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            if self.option == "row":
                # Retrieve a single row using the correct table and column name
                cursor.execute(f'SELECT * FROM {name_table} WHERE number_of_employee = ?', (num_row,))
                row = cursor.fetchone()

                if row:
                    if column_name and new_value is not None:
                        # Update the specific column with the new value
                        cursor.execute(f'UPDATE {name_table} SET {column_name} = ? WHERE number_of_employee = ?', (new_value, num_row))
                        conn.commit()
                        return f"Data updated successfully for {name_table}, {column_name} set to {new_value} for row {num_row}"
                    else:
                        return row
                else:
                    return f"No data found for {name_table} = {num_row}"

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()




    def selected_row(self, name_table,num_row):
        try:
            if self.option == "row":
                # Establish a connection to the database
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()

                # Retrieve a single row using the correct table and column name
                cursor.execute(f'SELECT * FROM {name_table} WHERE number_of_employee = ?', (num_row,))
                row = cursor.fetchone()

                if row:
                    return(row)
                else:
                    return(f"No data found for {name_table} = {num_row}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    def fetch_all_data(self,table_name):
        try:
            # Connect to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            # Fetch all data from the table
            cursor.execute(f'SELECT * FROM {table_name}')
            rows = cursor.fetchall()  # Fetch all rows from the query result
            
            if rows:
                return rows
            else:
                return "No data found."
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()


    def data_delete(self, table_name,num_row):
        try:
            if self.option == "row":
                # Establish a connection to the database
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()

                # Delete a row using the correct table and column name
                cursor.execute(f'DELETE FROM {table_name} WHERE number_of_employee = ?', (num_row,))
                conn.commit()  # Save changes to the database

                # Check if any rows were affected
                if cursor.rowcount > 0:
                    return(f"Row with {table_name} = {num_row} deleted successfully.")
                else:
                    return(f"No data found for {table_name} = {num_row}.")
        except sqlite3.Error as e:
            return(f"An error occurred: {e}")
        finally:
            conn.close()


    def delete_all_data_from_table(self,table_name):
        try:
            # Connect to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            # Ensure the table exists
            cursor.execute(f"PRAGMA table_info({table_name})")
            if not cursor.fetchall():
                return f"Table '{table_name}' does not exist."

            # Delete all data from the specified table
            cursor.execute(f"DELETE FROM {table_name}")
            conn.commit()  # Commit the changes

            return f"All data deleted from table '{table_name}'."
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()




    def search_database_by_prefix(self,column, value):
        try:
            # Connect to the database
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()

            # Construct and execute the query
            query = f"SELECT * FROM Types_of_buildings WHERE {column} LIKE ?"
            cursor.execute(query, (f"%{value}%",))
            rows = cursor.fetchall()

            if rows:
                # Print the column headers
                column_names = [description[0] for description in cursor.description]
                header = ' | '.join(column_names)

                # Gather all rows into a single string
                data = '\n'.join(' | '.join(map(str, row)) for row in rows)
                
                # Combine header and data
                result = f"{header}\n{data}"
                return result
            else:
                return "No data found."
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()





# Create an instance of DataHandling with the option "row"
dt = DataHandling("row")








#print(dt.search_database_by_prefix("Full_name_of_the_employee","il"))
#print(dt.display_all_data())


#------------------------------------------------------------------------------------





def process_inputs(inp1, inp2, inp3, inp4, inp5, inp6):
    liste = []

    # Define the columns and inputs
    columns = [
        ("Full_name_of_the_employee", inp1),
        ("Phone_number", inp2),
        ("Date", inp3),
        ("Type_of_car", inp4),
        ("Description", inp5),
        ("Been_worked_on", inp6)
    ]

    # Loop through columns and inputs
    for column, inp in columns:
        if inp:
            # Search the database with each non-empty input
            result = dt.search_database_by_prefix(column, inp)
            if result:  # Check if the result is not empty
                liste.append(result)

    # If no inputs match, return None or empty string
    if not liste:
        return None  # or return "" if you prefer an empty string

    # Return combined results
    return '\n'.join(list(set(liste)))


def remove_duplicates(data):
    unique_data = []
    seen = set()
    
    for line in data:
        if line not in seen:
            unique_data.append(line)
            seen.add(line)
    
    return unique_data
def process_input(inp):
    liste = []

    # Define the columns you want to search in
    columns = [
        "Full_name_of_the_employee",
        "Phone_number",
        "Date",
        "Type_of_car",
        "Description",
        "Been_worked_on"
    ]

    # Loop through each column and search with the input
    for column in columns:
        if inp:
            # Assuming dt.search_database_by_prefix(column, inp) returns a string with newline-separated results
            result = dt.search_database_by_prefix(column, inp)
            if result:  # Check if the result is not empty
                x = result.strip().split('\n')
                liste.extend(x)  # Add the results to the list

    # If no inputs match, return None
    if not liste:
        return None

    # Return the list of results
    x = remove_duplicates(liste)
    x.remove("An error occurred: no such column: Phone_number")
    x.remove("No data found.")
    x.remove("number_of_employee | Full_name_of_the_employee | number_phone | date | Type_of_car | description | been_worked_on | prix")
    return x



#print(process_inputs("","","","","","no"))
#dt.data_delete("Types_of_buildings",68)
#print(dt.display_all_data())
dt.edit_data_row("Types_of_buildings",1,"Been_worked_on","yes")
print(dt.selected_row("Types_of_buildings",1))
print(len(process_input("no")))
'''
for i in process_input("no"):
    print(i)
'''

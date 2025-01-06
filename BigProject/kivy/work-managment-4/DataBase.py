import sqlite3

class DataHandling:

    def __init__(self,DB_name):
        self.DB_name = DB_name

    def display_all_data(self,name_of_table):
        try:
            # Connect to the database
            conn = sqlite3.connect(self.DB_name)
            cursor = conn.cursor()

            # Fetch all data from the table
            cursor.execute(f'SELECT * FROM {name_of_table}')
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
            conn = sqlite3.connect(self.DB_name)
            cursor = conn.cursor()

                # Retrieve a single row using the correct table and column name
            cursor.execute(f'SELECT * FROM {name_table} WHERE Number = ?', (num_row,))
            row = cursor.fetchone()

            if row:
                if column_name and new_value is not None:
                        # Update the specific column with the new value
                    cursor.execute(f'UPDATE {name_table} SET {column_name} = ? WHERE Number = ?', (new_value, num_row))
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
                # Establish a connection to the database
                conn = sqlite3.connect(self.DB_name)
                cursor = conn.cursor()

                # Retrieve a single row using the correct table and column name
                cursor.execute(f'SELECT * FROM {name_table} WHERE Number = ?', (num_row,))
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
            conn = sqlite3.connect(self.DB_name)
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
                # Establish a connection to the database
            conn = sqlite3.connect(self.DB_name)
            cursor = conn.cursor()

                # Delete a row using the correct table and column name
            cursor.execute(f'DELETE FROM {table_name} WHERE Number = ?', (num_row,))
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
            conn = sqlite3.connect(self.DB_name)
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

    def search_in_all_columns(self, name_of_table, search_value):
        try:
            # Connect to the database
            conn = sqlite3.connect(self.DB_name)
            cursor = conn.cursor()

            # Get all column names from the table
            cursor.execute(f'PRAGMA table_info({name_of_table})')
            columns = [info[1] for info in cursor.fetchall()]

            if not columns:
                return f"Table '{name_of_table}' does not exist."

            # Construct the query to search in all columns
            query = f"SELECT * FROM {name_of_table} WHERE " + " OR ".join([f"{column} LIKE ?" for column in columns])
            search_pattern = f"%{search_value}%"

            # Execute the search query
            cursor.execute(query, tuple([search_pattern] * len(columns)))
            rows = cursor.fetchall()

            if rows:
                return rows  # Return the rows as a list of lists (each row is a list)
            else:
                return []  # Return an empty list if no data is found

        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()

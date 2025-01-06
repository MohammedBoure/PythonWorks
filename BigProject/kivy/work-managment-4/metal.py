import sqlite3
import DataBase

def Create_and_add_metal_data(Dimensions, Number_present, Number_used, Prix):
    if Dimensions and Number_present and Number_used and Prix:
        try:
            conn = sqlite3.connect('metal.db')
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Metal (
                Number INTEGER PRIMARY KEY AUTOINCREMENT,
                Dimensions TEXT NOT NULL,
                Number_present TEXT NOT NULL,
                Number_used TEXT NOT NULL,
                Prix TEXT NOT NULL
            )
            ''')

            cursor.execute('''
            INSERT INTO Metal (Dimensions, Number_present, Number_used, Prix)
            VALUES (?, ?, ?, ?)
            ''', (Dimensions, Number_present, Number_used, Prix))
            conn.commit()
            return "Data inserted successfully."
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()

dt = DataBase.DataHandling("metal.db")
        
def remove_data_in_db_metal(data): 
    data = data.split(" ")[1]  #exp:   N: 2    D: 30/30 3m    NP: 10     NU: 0    P: 100
    dt.data_delete("Metal",int(data))
    
    


import sqlite3
import csv

# # Connect to the database (or create it if it doesn't exist)
# conn = sqlite3.connect('US.db')

# # Create a cursor object to interact with the database
# cur = conn.cursor()

# # Create the US_CENSUS table if it doesn't already exist
# cur.execute(''' 
#     CREATE TABLE IF NOT EXISTS US_CENSUS (
#     id INTEGER PRIMARY KEY,
#     age INTEGER NOT NULL,
#     sex TEXT NOT NULL,
#     bmi REAL NOT NULL,
#     children INTEGER NOT NULL,
#     smoker TEXT NOT NULL, 
#     region TEXT NOT NULL,
#     charges REAL
#     )
# ''')

# # Commit the changes
# conn.commit()

# # Clear the existing data in the table to avoid duplicate entries
# cur.execute("DELETE FROM US_CENSUS")
# conn.commit()

# # Open the CSV file and insert the data into the US_CENSUS table
# with open('insurance.csv', newline='') as insurance_csv:
#     insurance_reader = csv.reader(insurance_csv)
#     next(insurance_reader, None)  # Skip the header row
#     for row in insurance_reader:

#         cur.execute('''
#         INSERT INTO US_CENSUS(age, sex, bmi, children, smoker, region, charges)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  # Insert values from the CSV file
#         conn.commit()

# # Close the connection to the database
# conn.close()
#function allows users to query the data without having to replicate the code

def query_census_data(query):
    conn = sqlite3.connect('US.db')
    cur = conn.cursor()

    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

def collect_data():
    query = "SELECT COUNT(*) FROM US_CENSUS"
    data = query_census_data(query)
    count = data[0][0]
    # print(count)
    return count

def calculate_average_charge():
    query = "SELECT AVG(charges) FROM US_CENSUS WHERE charges IS NOT NULL"
    result = query_census_data(query)
    avg_charge = result[0][0]  # Extract the average value
    
    if avg_charge is not None:
        avg_charge = round(avg_charge, 2)  # Round the average to 2 decimal places
    
    # print(avg_charge)
    return avg_charge



def calculate_sum_charges():
    query = "SELECT SUM(charges) FROM US_CENSUS WHERE charges IS NOT NULL"
    result = query_census_data(query)
    sum_charge = result[0][0]
    if sum_charge is not None:
        sum_charge = round(sum_charge, 2)
    return sum_charge

average_charge = calculate_average_charge()

# average = 17755824.99 / 1338
# average charge is 13270.42

def count_non_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'no'"
    result = query_census_data(query)
    total_non_smokers = result[0][0]
    # print(total_non_smokers)
    return total_non_smokers

def count_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'yes'"
    result = query_census_data(query)
    total_smokers = result[0][0]
    print(total_smokers)
    return total_smokers

smokers = count_smokers()

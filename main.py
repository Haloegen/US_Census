import sqlite3
import csv
import numpy as np 
import statistics

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
# 1338 entries in the data

def calculate_average_charge():
    query = "SELECT AVG(charges) FROM US_CENSUS WHERE charges IS NOT NULL"
    result = query_census_data(query)
    avg_charge = result[0][0]  # Extract the average value
    
    if avg_charge is not None:
        avg_charge = round(avg_charge, 2)  # Round the average to 2 decimal places
    
    # print(avg_charge)
    return avg_charge
# 13270.42 is the average insurance charge



def calculate_sum_charges():
    query = "SELECT SUM(charges) FROM US_CENSUS WHERE charges IS NOT NULL"
    result = query_census_data(query)
    sum_charge = result[0][0]
    if sum_charge is not None:
        sum_charge = round(sum_charge, 2)
    return sum_charge
# total of all the insurance charges in the data set 17755824.99

average_charge = calculate_average_charge()

# average = 17755824.99 / 1338
# average charge is 13270.42

def count_non_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'no'"
    result = query_census_data(query)
    total_non_smokers = result[0][0]
    # print(total_non_smokers)
    return total_non_smokers
# 1064 non smokers

def count_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'yes'"
    result = query_census_data(query)
    total_smokers = result[0][0]
    # print(total_smokers)
    return total_smokers
# 274 smokers

def count_people_with_children():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children > 0"
    result = query_census_data(query)
    total_people_with_children = result[0][0]
    # print(total_people_with_children)
    return total_people_with_children
# 764 people with children

def count_people_without_children():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children = 0"
    result = query_census_data(query)
    people_without_children = result[0][0]
    # print(people_without_children)
    return(people_without_children)
# 574 people have no children

def count_people_with_children_and_dont_smoke():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children > 0 AND LOWER(smoker) = 'no'"
    result = query_census_data(query)
    people_with_children_and_dont_smoke = result[0][0]
    # print(people_with_children_and_dont_smoke)
    return people_with_children_and_dont_smoke
# 605 people who dont smoke and have a child

def count_people_who_dont_have_kids_but_smoke():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children = 0 AND LOWER(smoker) = 'yes'"
    result = query_census_data(query)
    people_who_dont_have_kids_but_smoke = result[0][0]
    # print(people_who_dont_have_kids_but_smoke)
    return people_who_dont_have_kids_but_smoke
# 115 people who dont have kids but smoke
# by deduction the remainder should be 618 people

def count_people_who_smoke_and_have_kids():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children > 0 AND LOWER(smoker) = 'yes'"
    result = query_census_data(query)
    people_who_smoke_and_have_kids = result[0][0]
    # print(people_who_smoke_and_have_kids)
    return people_who_smoke_and_have_kids
# 159 people who smoke and have kids
# 459 people who dont have kids and dont smoke should be the remainder

def count_people_dont_smoke_no_kids():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE children = 0 AND LOWER(smoker) = 'no'"
    result = query_census_data(query)
    people_dont_smoke_no_kids = result[0][0]
    # print(people_dont_smoke_no_kids)
    return people_dont_smoke_no_kids
#459 is the remainder which means the math adds up

def find_top_charges():
    query = "SELECT charges FROM US_CENSUS ORDER BY charges DESC limit 10"
    result = query_census_data(query)
    print(result)
    return(result)
# [(63770.42801,), (62592.87309,), (60021.39897,), (58571.07448,), (55135.40209,)] biggest charges
# [(1121.8739,), (1131.5066,), (1135.9407,), (1136.3994,), (1137.011,)] lowest charges


def get_all_charges():
    query = "SELECT charges FROM US_CENSUS WHERE charges IS NOT NULL"
    result = query_census_data(query)

    charges = [row[0] for row in result]
    return charges

def calculate_iqr_and_std():
    charges = get_all_charges()
    
    if len(charges) == 0:
        print("No data available")
        return None, None

    q75, q25 = np.percentile(charges, [75,25])
    iqr = q75 - q25

    std_dev = statistics.stdev(charges)

    print(f"Interquartile Range (IQR): {iqr}")
    print(f"Standard Deviation: {std_dev}")
    
    return iqr, std_dev

# IQR = 11899.63
# STD_DEV = 12110.01


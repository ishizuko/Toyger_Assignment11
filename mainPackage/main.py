# File Name : main.py
# Student Name: Omar Alkhawaga,Kengo Ishizuka
# email: alkhawoe@mail.uc.edu
#        ishizuko@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: 
# Citations: https://chatgpt.com/, https://www.geeksforgeeks.org/working-csv-files-python/
# Anything else that's relevant:https://app.zipcodebase.com

from functionPackage.function import *
from zip_fillerPackage.zip_filler import*
import os
from dotenv import load_dotenv



if __name__ == "__main__":

    load_dotenv()  
    api_key_zipcode = os.getenv("API_KEY_ZIPCODE")

    file_path = "./dataFiles/fuelPurchaseData.csv"
    # Read the CSV file
    csv = CSVDataProcessor()
    df = csv.read_CSV_file(file_path)

    # Format gross price to 2 decimal places
    df = csv.format_gross_price(df, 'Gross Price')
    
    # Delete duplicate rows
    df = csv.drop_duplicates(df)

    # Extract Pepsi rows (data anomalies)
    df_pepsi = csv.exstract_anomalies(df, 'Fuel Type', 'Pepsi')

    # Export Pepsi rows to dataAnomalies.csv
    csv.export_to_csv(df_pepsi, './Data/dataAnomalies.csv')

    # Remove Pepsi rows from main dataset
    df = csv.delete_rows(df, 'Fuel Type', 'Pepsi')
    
    


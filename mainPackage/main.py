# File Name : main.py
# Student Name: Omar Alkhawaga,Kengo Ishizuka
# email: alkhawoe@mail.uc.edu
#        ishizuko@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: This module cleans fuel purchase data by formatting prices, removing duplicates/anomalies, filling ZIPs via API, and exporting results.
# Citations: https://chatgpt.com/, https://www.geeksforgeeks.org/working-csv-files-python/
# Anything else that's relevant:https://app.zipcodebase.com

from functionPackage.function import *
from zip_fillerPackage.zip_filler import*




if __name__ == "__main__":

    api_key_zipcode = "05e648a0-1afd-11f0-a8c9-41b13795941d"    #API Key

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
    

    # Fill missing ZIP codes (first 5)
    filler = ZipCodeFiller(api_key = api_key_zipcode)  
    df = csv.fill_missing_zip_codes(df, filler)

    # Export cleaned data
    csv.export_to_csv(df, './Data/cleanedData.csv')
    


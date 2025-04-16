# File Name : main.py
# Student Name: Omar Alkhawaga,Kengo
# email: alkhawoe@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: 
# Citations: https://chatgpt.com/, https://www.geeksforgeeks.org/working-csv-files-python/
# Anything else that's relevant:N/A

from requests.auth import parse_dict_header
from functionPackage.function import *





if __name__ == "__main__":

    file_path = "./dataFiles/fuelPurchaseData.csv"
    # Read the CSV file
    csv = CSVDataProcessor()
    df = csv.read_CSV_file(file_path)
    # Align decimal points
    df = csv.format_gross_price(df, 'Gross Price')
    
    # Delete duplicate rows
    df = csv.drop_duplicates(df)

    # Extract data that has pepsi as Fuel Type and export to dataAnomalies.csv
    df_pepsi = csv.exstract_anomalies(df, 'Fuel Type', 'Pepsi')
    df_pepsi = csv.drop_duplicates(df_pepsi)
    csv.export_to_csv(df_pepsi, './Data/dataAnomalies.csv')
    
    
    # Delete data that has pepsi as Fuel Type from dataframe
    df = csv.delete_rows(df,'Fuel Type', 'Pepsi')

    df = csv.split_address(df)  
    df = csv.fill_missing_zip_codes(df)  
   
     # Fill missing ZIP codes
    df = csv.fill_missing_zip_codes(df, city_column='City', zip_column='ZipCode')

    

    # Export final cleaned data
    csv.export_to_csv(df, './Data/cleanedData.csv')
    df = pd.read_csv(file_path, low_memory=False)

    
    
    
    

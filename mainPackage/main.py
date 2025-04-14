# main.py

from requests.auth import parse_dict_header
from functionPackage.function import *
import pandas as pd




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
    

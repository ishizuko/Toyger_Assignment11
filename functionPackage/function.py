
# File Name : function.py
# Student Name: Omar Alkhawaga
# email: alkhawoe@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: 
# Citations: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html, https://chatgpt.com/
# Anything else that's relevant:N/A


import pandas as pd
import requests
import os

class CSVDataProcessor:

    def __init__(self):
        self.api_key = os.environ.get('API_KEY_ASSIGNMENT11')

    
    def read_CSV_file(self, file_path):
        '''
        Read from a CSV file 
        @param file_path String: The CSV file path to read. It should have a header row, which will be skipped
        @return Pandas_dataframe
        '''
        df = pd.read_csv(file_path)

        return df
    
    def format_gross_price(self, df, column_name):
        """
        Format the specified column to always show two decimal places as string.
        @param df: pandas DataFrame
        @param column_name String:The column name to format
        @return: DataFrame with formatted column
        """
        df[column_name] = df[column_name].apply(lambda x: "{:.2f}".format(float(x)))
        return df


    def drop_duplicates(self, df):
        """
        Drop duplicate rows from the DataFrame
        @param df: pandas DataFrame
        @return: DataFrame with duplicates removed
        """
        df = df.drop_duplicates()
        return df  

    def exstract_anomalies(self, df, header_name, key_value):
        """
        Extract pandas dataframe with specific value
        @param df dataframe: The dataframe to edit
        @param header_name String: The name of colum to check
        @param key_value String: The specific value to check
        @return DataFrame
        """
        df = df[df[header_name] == key_value]

        return df

    def export_to_csv(self, df, file_name):
        """
        Export pandas dataframe to CSV file
        @param df dataframe: The data to export 
        @param file_name String: The name of the CSV file
        @return None
        """
        df.to_csv(file_name)

    def delete_rows(self, df, header_name, key_value):
        """
        Delete rows with specific value
        @param df dataframe: The dataframe to delete
        @param header_name String: The name of colum to check
        @param key_value String: The specific value to check
        @return DataFrame
        """
        df = df.drop(df[df[header_name] == key_value].index)

        return df

    def fill_missing_zip_codes(self, df, city_column='City', zip_column='ZipCode'):
        """

        """
        for index, row in df[df[zip_column].isnull() | (df[zip_column] == '')].iterrows():
            city = row[city_column]
            zip_code = self.lookup_zip_code(city)
            if zip_code:
                df.at[index, zip_column] = zip_code
        return df

    def lookup_zip_code(self, city, country='US'):
        """

        """
        try:
            response = requests.get(
                "https://app.zipcodebase.com/api/v1/search",
                params={
                    "apikey": self.api_key,
                    "city": city,
                    "country": country
                }
            )
            data = response.json()
            results = data.get("results", {})
            if results:
                first_result = next(iter(results.values()))
                if first_result:
                    return first_result[0].get("postal_code")
        except Exception as e:
            print(f"Error fetching ZIP for city '{city}': {e}")
        return ''

    def split_address(self, df, address_column='Full Address'):
        """
        Extract city and zip code from full address and add as new columns.
        """
        address_parts = df[address_column].str.extract(r'^(.*?),\s*(.*?),\s*([A-Z]{2})\s*(\d{5})?$')
        df['City'] = address_parts[1]
        df['ZipCode'] = address_parts[3]
        return df



    



       




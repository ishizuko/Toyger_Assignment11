
# File Name : function.py
# Student Name: Omar Alkhawaga
#               Kengo Ishizuka
# email: alkhawoe@mail.uc.edu
#        ishizuko@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: This module provides tools to clean and export CSV data, including price formatting, duplicate removal, anomaly extraction, and ZIP code filling via API.
# Citations: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html, https://chatgpt.com/
# Anything else that's relevant:N/A


import pandas as pd
import re
import os

class CSVDataProcessor:
    
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

    def exstract_anomalies(self, df, column_name, key_value):
        """
        Extract pandas dataframe with specific value
        @param df dataframe: The dataframe to edit
        @param column_name String: The name of colum to check
        @param key_value String: The specific value to check
        @return DataFrame
        """
        df = df[df[column_name].str.lower() == key_value.lower()]

        return df

    def delete_rows(self, df, column_name, key_value):
        """
        Delete rows with specific value
        @param df dataframe: The dataframe to delete
        @param column_name String: The name of colum to check
        @param key_value String: The specific value to check
        @return DataFrame
        """
        df = df[df[column_name].str.lower() != key_value.lower()]

        return df

    def export_to_csv(self, df, file_name):
        """
        Export pandas dataframe to CSV file
        @param df dataframe: The data to export 
        @param file_name String: The name of the CSV file
        @return None
        """
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        df.to_csv(file_name, index=False)



    def fill_missing_zip_codes(self, df, zip_filler):
        """
        Fill ZIP codes for the first 5 missing ZIP rows using both city and state.
        @param df dataframe: The data to use
        @param zip_filler Class: The class to connect API
        @return DataFrame
        """
        missing_rows = df[~df['Full Address'].str.contains(r'\d{5}', na=False)].head(5) # Pick 5 missing ZIP rows and store them into list

        for idx, row in missing_rows.iterrows():
            full_address = row['Full Address']
            parts = [p.strip() for p in full_address.split(',')]

            if len(parts) >= 3:
                city = parts[1]
                state_abbr = parts[2].split()[0]  # e.g., "OH"
            else:
                print(f"[Skipped] Invalid address format: {full_address}")
                continue

            # Map state abbreviation to full state name
            state_full = self._convert_state_abbr_to_full(state_abbr)

            if not state_full:
                print(f"[Skipped] Unknown state abbreviation: {state_abbr}")
                continue

            zip_code = zip_filler.get_zip_code(city, state_full)

            if zip_code:
                df.at[idx, 'Full Address'] = f"{full_address} {zip_code}"
                print(f"[Updated] {full_address} ? {df.at[idx, 'Full Address']}")
            else:
                print(f"[Not Found] No ZIP found for {city}, {state_full}")
       
        return df

    def _convert_state_abbr_to_full(self, abbr):
        """
        Convert abbreviation of state name to full state name
        @param abbr String: The abbreviation of state name
        @return String: Full state name correspond to the abbreviation
        """
        states = {
                "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
                "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
                "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
                "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
                "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
                "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
                "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
                "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
                "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
                "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
                "DC": "District of Columbia"
        }
        return states.get(abbr.upper(), None)





       




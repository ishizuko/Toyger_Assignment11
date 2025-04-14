# function.py
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html

import pandas as pd

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




    



       




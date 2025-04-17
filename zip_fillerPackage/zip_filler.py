# File Name : zip_filler.py
# Student Name: Omar Alkhawaga
# email: alkhawoe@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/17/2025
# Course #/Section:IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: We were given a CSV file and had to cleanup the file by doing some tasks
# Brief Description of what this module does: This module takes an API key frm zipcodebase.com and generates zipcode for missing addresses
# Citations:https://chatgpt.com/
# Anything else that's relevant:N/A




import requests

class ZipCodeFiller:
    def __init__(self, api_key):
        """
        @param api_key String: The API key
        @return None
        """
        self.api_key = api_key
        self.base_url = "https://app.zipcodebase.com/api/v1/code/city"

    def get_zip_code(self, city, state_name, country="US"):
        """
        Get zipcode from API correspond the city and state
        @param city String: The city name
        @param state_name String: Full state name
        @param country: "US" by default
        @return
        """
        params = {
            "apikey": self.api_key,
            "city": city,
            "state_name": state_name,
            "country": country
        }

        try:
            response = requests.get(self.base_url, params=params)
            print(f"[DEBUG] API URL: {response.url}")
            response.raise_for_status()
            data = response.json()
            print(f"[DEBUG] Response JSON: {data}")

            zip_codes = data.get("results", [])
            return zip_codes[0] if zip_codes else None

        except Exception as e:
            print(f"[API Error] {city}, {state_name} ? {e}")
            return None




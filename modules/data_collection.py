# modules/data_collection.py

import csv
import requests

def load_destination_data(file_path="data/destinations.csv"):
    """
    Load destination data from a CSV file.
    The CSV should contain columns for destination, avg_temp, budget, and activities.
    """
    destinations = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            destination = {
                "name": row["destination"],
                "avg_temp": float(row["avg_temp"]),
                "budget": int(row["budget"]),
                "activities": row["activities"].split(',')
            }
            destinations.append(destination)
    return destinations

def fetch_weather_data(city):
    """
    Fetches current weather data for a given city.
    This is a placeholder function for fetching real-time weather data using an API.
    Replace <YOUR_API_KEY> with a valid API key.
    """
    api_key = "<YOUR_API_KEY>"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']  # Return the current temperature
    else:
        print("Failed to fetch weather data")
        return None



def convert_currency(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another using Exchange Rates API.
    """
    api_key = "<YOUR_API_KEY>"
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        rate = data["rates"].get(to_currency)
        if rate:
            return amount * rate
        else:
            print(f"Currency {to_currency} not found.")
            return None
    except Exception as e:
        print("Failed to fetch exchange rate:", e)
        return None


def load_destination_data(file_path="data/destinations.csv"):
    """
    Load destination data from a CSV file, setting defaults for missing values.
    """
    destinations = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            destination = {
                "name": row["destination"],
                "avg_temp": float(row["avg_temp"]),
                "budget": int(row["budget"]),
                "activities": row["activities"].split(','),
                "safety_index": float(row.get("safety_index", 5.0)),  # Default safety_index to 5.0 if missing
                "family_friendly": row.get("family_friendly", "No")   # Default family_friendly to "No" if missing
            }
            destinations.append(destination)
    return destinations

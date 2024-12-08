

import csv

def load_destination_data(file_path="data/output.csv"):
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
                "spring_temp": float(row["spring_temp"]),
                "summer_temp": float(row["summer_temp"]),
                "fall_temp": float(row["fall_temp"]),
                "winter_temp": float(row["winter_temp"])
            }
            destinations.append(destination)
    return destinations

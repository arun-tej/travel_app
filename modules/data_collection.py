import csv

def load_destination_data(file_path):
    destinations = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Ensure that the temperature fields are correctly converted to floats
                spring_temp = float(row["spring_temp"]) if row["spring_temp"].replace('.', '', 1).isdigit() else None
                summer_temp = float(row["summer_temp"]) if row["summer_temp"].replace('.', '', 1).isdigit() else None
                fall_temp = float(row["fall_temp"]) if row["fall_temp"].replace('.', '', 1).isdigit() else None
                winter_temp = float(row["winter_temp"]) if row["winter_temp"].replace('.', '', 1).isdigit() else None

                destinations.append({
                    "destination": row["destination"],
                    "avg_temp": float(row["avg_temp"]),
                    "budget": float(row["budget"]),
                    "activities": row["activities"],
                    "spring_temp": spring_temp,
                    "summer_temp": summer_temp,
                    "fall_temp": fall_temp,
                    "winter_temp": winter_temp,
                })
            except ValueError as e:
                print(f"Error processing row: {row}. Error: {e}")
    return destinations

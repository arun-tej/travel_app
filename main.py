from flask import Flask, render_template, request
import os
from modules.recommendation import recommend_destinations
from modules.data_collection import load_destination_data

# File path to the CSV containing destination data
file_path = "/Users/aruntej/Desktop/travel_app/data/destinations.csv"
destinations = load_destination_data(file_path)

# Initialize the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None  # Initialize recommendations as None
    error = None  # Initialize error message as None

    if request.method == "POST":
        try:
            # Retrieve user preferences from form inputs
            min_temp = float(request.form["min_temp"])
            max_temp = float(request.form["max_temp"])
            min_budget = int(request.form["min_budget"])
            max_budget = int(request.form["max_budget"])
            activities = request.form.getlist("activities")
        except ValueError:
            # Handle invalid input gracefully
            error = "Please enter valid values for all fields."
            return render_template("index.html", recommendations=recommendations, error=error)

        # Package preferences into a dictionary
        user_preferences = {
            "temperature_range": (min_temp, max_temp),
            "budget_range": (min_budget, max_budget),
            "activities": activities
        }

        # Get recommendations based on user preferences
        recommendations = recommend_destinations(user_preferences, destinations)

        if not recommendations:
            error = "No recommendations found. Please try different preferences."

    # Render the form initially without recommendations, or with the recommendations after form submission
    return render_template("index.html", recommendations=recommendations, error=error)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

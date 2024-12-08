from flask import Flask, render_template, request
from modules.recommendation import recommend_destinations
from modules.data_collection import load_destination_data

app = Flask(__name__)

# Load destination data once when the app starts
destinations = load_destination_data("data/output.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve user preferences from form inputs
        try:
            min_temp = float(request.form["min_temp"])
            max_temp = float(request.form["max_temp"])
            min_budget = int(request.form["min_budget"])
            max_budget = int(request.form["max_budget"])
            activities = request.form.getlist("activities")
        except ValueError:
            # Handle invalid input gracefully
            return render_template("index.html", error="Please enter valid values for all fields.")

        # Package preferences into a dictionary
        user_preferences = {
            "temperature_range": (min_temp, max_temp),
            "budget_range": (min_budget, max_budget),
            "activities": activities
        }
        
        # Get recommendations based on user preferences
        recommended_destinations = recommend_destinations(user_preferences, destinations)
        
        # Render results along with the original form
        return render_template("index.html", recommendations=recommended_destinations, error=None)
    
    # Render the form initially without recommendations
    return render_template("index.html", recommendations=None, error=None)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


# modules/recommendation.py

def recommend_destinations(user_preferences, destinations):
    """
    Recommend destinations based on user preferences.
    Parameters:
    - user_preferences: Dictionary with user's temperature, activity, and budget preferences.
    - destinations: List of destinations loaded from data.
    """
    recommended = []

    for destination in destinations:
        # Check temperature range
        temp_ok = (
            user_preferences["temperature_range"][0] <= destination["avg_temp"] <= user_preferences["temperature_range"][1]
        )

        # Check budget range
        budget_ok = (
            user_preferences["budget_range"][0] <= destination["budget"] <= user_preferences["budget_range"][1]
        )

        # Check for matching activities
        activity_match = any(activity in destination["activities"] for activity in user_preferences["activities"])

        # If all conditions are met, add the destination to recommendations
        if temp_ok and budget_ok and activity_match:
            recommended.append(destination)

    return recommended

def display_recommendations(recommended_destinations):
    """
    Displays a list of recommended destinations.
    """
    if not recommended_destinations:
        print("Sorry, no destinations match your preferences.")
    else:
        print("\nWe found some destinations that match your preferences!\n")
        for dest in recommended_destinations:
            print(f"Destination: {dest['name']}")
            print(f"  Average Temperature: {dest['avg_temp']}°C")
            print(f"  Budget: ${dest['budget']} per day")
            print(f"  Activities: {', '.join(dest['activities'])}\n")


# In modules/recommendation.py

def recommend_destinations(user_preferences, destinations, season=None):
    """
    Recommend destinations based on user preferences, considering seasonal weather if specified.
    """
    recommended = []

    for destination in destinations:
        # Seasonal temperature check
        if season:
            avg_temp = destination.get(f"{season.lower()}_temp", destination["avg_temp"])
        else:
            avg_temp = destination["avg_temp"]

        # Check temperature range
        temp_ok = user_preferences["temperature_range"][0] <= avg_temp <= user_preferences["temperature_range"][1]

        # Check budget range
        budget_ok = user_preferences["budget_range"][0] <= destination["budget"] <= user_preferences["budget_range"][1]

        # Check for matching activities
        activity_match = any(activity in destination["activities"] for activity in user_preferences["activities"])

        # If all conditions are met, add the destination to recommendations
        if temp_ok and budget_ok and activity_match:
            recommended.append(destination)

    return recommended


def recommend_destinations(user_preferences, destinations, season=None, safety_min=5, family_friendly=None):
    """
    Recommend destinations based on user preferences, including advanced filtering.
    """
    recommended = []

    for destination in destinations:
        # Seasonal temperature check
        if season:
            avg_temp = destination.get(f"{season.lower()}_temp", destination["avg_temp"])
        else:
            avg_temp = destination["avg_temp"]

        # Basic filters
        temp_ok = user_preferences["temperature_range"][0] <= avg_temp <= user_preferences["temperature_range"][1]
        budget_ok = user_preferences["budget_range"][0] <= destination["budget"] <= user_preferences["budget_range"][1]
        activity_match = any(activity in destination["activities"] for activity in user_preferences["activities"])

        # Advanced filters
        safety_ok = destination["safety_index"] >= safety_min
        family_ok = family_friendly is None or destination["family_friendly"] == family_friendly

        # Add destination if all conditions are met
        if temp_ok and budget_ok and activity_match and safety_ok and family_ok:
            recommended.append(destination)

    return recommended

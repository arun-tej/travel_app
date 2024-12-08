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

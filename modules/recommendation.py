def recommend_destinations(user_preferences, destinations):
    min_temp, max_temp = user_preferences["temperature_range"]
    min_budget, max_budget = user_preferences["budget_range"]
    activities = user_preferences["activities"]

    recommended_destinations = []

    for destination in destinations:
        # Check if temperature values are valid (not None)
        spring_temp = destination["spring_temp"]
        summer_temp = destination["summer_temp"]
        fall_temp = destination["fall_temp"]
        winter_temp = destination["winter_temp"]

        # Debugging: Print values to help understand the issue
        print(f"Checking destination: {destination['destination']}")
        print(f"Temperature values: {spring_temp}, {summer_temp}, {fall_temp}, {winter_temp}")
        print(f"User preferences: Temp range: {min_temp}-{max_temp}, Budget range: {min_budget}-{max_budget}, Activities: {activities}")

        # Handle None values in temperature fields
        if (spring_temp is not None and min_temp <= spring_temp <= max_temp) or \
           (summer_temp is not None and min_temp <= summer_temp <= max_temp) or \
           (fall_temp is not None and min_temp <= fall_temp <= max_temp) or \
           (winter_temp is not None and min_temp <= winter_temp <= max_temp):

            # Check if the destination budget is within the user's budget range
            if min_budget <= destination["budget"] <= max_budget:

                # Check if any of the selected activities match the destination's activities
                if any(activity in destination["activities"] for activity in activities):
                    recommended_destinations.append(destination)

    print(f"Filtered recommendations: {recommended_destinations}")  # Debugging line
    return recommended_destinations

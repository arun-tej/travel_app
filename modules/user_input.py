# modules/user_input.py

def get_user_preferences():
    print("Welcome to the Data-Driven Travel Suggestion App!")
    
    # Get preferred temperature range
    temp_min = float(input("Enter your minimum preferred temperature (°C): "))
    temp_max = float(input("Enter your maximum preferred temperature (°C): "))
    preferred_temp = (temp_min, temp_max)
    
    # Get activity type preferences
    print("What type of activities do you enjoy? (Choose from: Adventure, Relaxation, Cultural, Nature)")
    activities = input("Enter preferred activities separated by commas: ").split(',')
    activities = [activity.strip().capitalize() for activity in activities]
    
    # Get budget range
    budget_min = int(input("Enter your minimum budget per day (in USD): "))
    budget_max = int(input("Enter your maximum budget per day (in USD): "))
    budget = (budget_min, budget_max)

    # Collect preferences in a dictionary
    user_preferences = {
        "temperature_range": preferred_temp,
        "activities": activities,
        "budget_range": budget
    }
    
    print("\nThank you! Your preferences have been recorded.\n")
    return user_preferences

# main.py

from modules.user_input import get_user_preferences
from modules.data_collection import load_destination_data
from modules.recommendation import recommend_destinations, display_recommendations

def main():
    # Step 1: Get user preferences
    user_preferences = get_user_preferences()
    
    # Step 2: Load destination data
    destinations = load_destination_data()
    
    # Step 3: Get recommendations based on preferences
    recommended_destinations = recommend_destinations(user_preferences, destinations)
    
    # Step 4: Display recommendations
    display_recommendations(recommended_destinations)

if __name__ == "__main__":
    main()

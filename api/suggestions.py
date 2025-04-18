SUGGESTIONS = {
    "Order Food": [
        {"action_code": "PLACE_ORDER", "display_text": "Place an Order at Your Favorite Restaurant"},
        {"action_code": "VIEW_RECIPES", "display_text": "Explore Recipes for Your Favorite Dishes"},
        {"action_code": "FIND_RESTAURANTS", "display_text": "Find Nearby Restaurants"},
    ],
    "Ask Question": [
        {"action_code": "CONTACT_SUPPORT", "display_text": "Contact Customer Support"},
        {"action_code": "SEARCH_FAQ", "display_text": "Search Frequently Asked Questions"},
        {"action_code": "ASK_COMMUNITY", "display_text": "Ask the Community for Help"},
    ],
    "Share News": [
        {"action_code": "POST_SOCIAL_MEDIA", "display_text": "Post News on Social Media Platforms"},
        {"action_code": "EMAIL_NEWS", "display_text": "Share News via Email"},
        {"action_code": "CREATE_BLOG_POST", "display_text": "Write a Blog Post About the News"},
    ],
    "Book Travel": [
        {"action_code": "SEARCH_FLIGHTS", "display_text": "Search for Flights"},
        {"action_code": "BOOK_HOTEL", "display_text": "Book a Hotel Room"},
        {"action_code": "CHECK_WEATHER", "display_text": "Check Weather at Your Destination"},
    ],
    "Manage Finances": [
        {"action_code": "VIEW_BALANCE", "display_text": "View Account Balance"},
        {"action_code": "PAY_BILLS", "display_text": "Pay Your Bills"},
        {"action_code": "TRANSFER_FUNDS", "display_text": "Transfer Funds to Another Account"},
    ],
    "Learn Skills": [
        {"action_code": "ENROLL_COURSE", "display_text": "Enroll in an Online Course"},
        {"action_code": "WATCH_TUTORIALS", "display_text": "Watch Video Tutorials"},
        {"action_code": "READ_BOOKS", "display_text": "Read Books on the Subject"},
    ],
    "Health & Fitness": [
        {"action_code": "TRACK_WORKOUT", "display_text": "Track Your Workout"},
        {"action_code": "SCHEDULE_CHECKUP", "display_text": "Schedule a Health Checkup"},
        {"action_code": "PLAN_DIET", "display_text": "Plan a Healthy Diet"},
    ],
    "Entertainment": [
        {"action_code": "STREAM_MOVIES", "display_text": "Stream Movies and TV Shows"},
        {"action_code": "PLAY_GAMES", "display_text": "Play Online or Offline Games"},
        {"action_code": "LISTEN_MUSIC", "display_text": "Listen to Music or Podcasts"},
    ]
}

def suggest_actions(intent):
    return SUGGESTIONS.get(intent, [{"action_code": "GENERAL_HELP", "display_text": "Get General Help"}])
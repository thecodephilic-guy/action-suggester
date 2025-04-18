SUGGESTIONS = {
    "Order Food": [
        {"action_code": "PLACE_ORDER", "display_text": "Place an Order at Your Favorite Restaurant"},
        {"action_code": "VIEW_RECIPES", "display_text": "Explore Recipes for Your Favorite Dishes"},
        {"action_code": "ORDER_GROCERIES", "display_text": "Order Groceries Online"},
        {"action_code": "FIND_RESTAURANTS", "display_text": "Find Nearby Restaurants"},
        {"action_code": "CHECK_DELIVERY_STATUS", "display_text": "Check Your Delivery Status"},
    ],
    "Ask Question": [
        {"action_code": "CONTACT_SUPPORT", "display_text": "Contact Customer Support"},
        {"action_code": "SEARCH_FAQ", "display_text": "Search Frequently Asked Questions"},
        {"action_code": "ASK_COMMUNITY", "display_text": "Ask the Community for Help"},
        {"action_code": "CHAT_BOT", "display_text": "Chat with a Virtual Assistant"},
        {"action_code": "READ_DOCUMENTATION", "display_text": "Read the User Documentation"},
    ],
    "Share News": [
        {"action_code": "POST_SOCIAL_MEDIA", "display_text": "Post News on Social Media Platforms"},
        {"action_code": "EMAIL_NEWS", "display_text": "Share News via Email"},
        {"action_code": "CREATE_BLOG_POST", "display_text": "Write a Blog Post About the News"},
        {"action_code": "SHARE_WHATSAPP", "display_text": "Share News via WhatsApp"},
        {"action_code": "SEND_PUSH_NOTIFICATION", "display_text": "Send a Push Notification"},
    ],
    "Book Travel": [
        {"action_code": "SEARCH_FLIGHTS", "display_text": "Search for Flights"},
        {"action_code": "BOOK_HOTEL", "display_text": "Book a Hotel Room"},
        {"action_code": "RENT_CAR", "display_text": "Rent a Car for Your Trip"},
        {"action_code": "PLAN_ITINERARY", "display_text": "Plan Your Travel Itinerary"},
        {"action_code": "CHECK_WEATHER", "display_text": "Check Weather at Your Destination"},
    ],
    "Manage Finances": [
        {"action_code": "VIEW_BALANCE", "display_text": "View Account Balance"},
        {"action_code": "PAY_BILLS", "display_text": "Pay Your Bills"},
        {"action_code": "TRANSFER_FUNDS", "display_text": "Transfer Funds to Another Account"},
        {"action_code": "INVEST_STOCKS", "display_text": "Invest in Stocks or Mutual Funds"},
        {"action_code": "SET_BUDGET", "display_text": "Set a Monthly Budget"},
    ],
    "Learn Skills": [
        {"action_code": "ENROLL_COURSE", "display_text": "Enroll in an Online Course"},
        {"action_code": "WATCH_TUTORIALS", "display_text": "Watch Video Tutorials"},
        {"action_code": "READ_BOOKS", "display_text": "Read Books on the Subject"},
        {"action_code": "JOIN_WORKSHOP", "display_text": "Join a Workshop or Seminar"},
        {"action_code": "PRACTICE_PROJECTS", "display_text": "Work on Practice Projects"},
    ],
    "Health & Fitness": [
        {"action_code": "TRACK_WORKOUT", "display_text": "Track Your Workout"},
        {"action_code": "SCHEDULE_CHECKUP", "display_text": "Schedule a Health Checkup"},
        {"action_code": "PLAN_DIET", "display_text": "Plan a Healthy Diet"},
        {"action_code": "JOIN_FITNESS_CLASS", "display_text": "Join a Fitness Class"},
        {"action_code": "MONITOR_SLEEP", "display_text": "Monitor Your Sleep Patterns"},
    ],
    "Entertainment": [
        {"action_code": "STREAM_MOVIES", "display_text": "Stream Movies and TV Shows"},
        {"action_code": "BUY_TICKETS", "display_text": "Buy Tickets for Events"},
        {"action_code": "PLAY_GAMES", "display_text": "Play Online or Offline Games"},
        {"action_code": "LISTEN_MUSIC", "display_text": "Listen to Music or Podcasts"},
        {"action_code": "EXPLORE_EVENTS", "display_text": "Explore Local Events and Activities"},
    ]
}

def suggest_actions(intent):
    return SUGGESTIONS.get(intent, [{"action_code": "GENERAL_HELP", "display_text": "Get General Help"}])
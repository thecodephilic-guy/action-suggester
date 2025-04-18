from google import genai
import os
import json

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

def get_tone_and_intent(text):
    prompt = f"""
        What is the tone and intent of the following message?

        Respond with a JSON in this format: {{"tone": "...", "intent": "..."}}

        Valid intent categories include:
        - Order Food
        - Ask Questions
        - Share News
        - Book Travel
        - Manage Finances
        - Learn Skills
        - Health & Fitness
        - Entertainment

        Example:
        Message: "I'm really hungry and craving some sushi tonight."
        Response: {{"tone": "Hungry", "intent": "Order Food"}}

        Now analyze this:
        Message: "{text}"
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=[prompt]
        )
        cleaned = response.text.strip().removeprefix("```json").removesuffix("```").strip() #the response.text is a string that looks like this: ```json {{"tone": "...", "intent": "..."}}``` which can not be parsed by json.loads so refractoring it in a valid format.
        return json.loads(cleaned)  # Safely parse JSON response
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return {"tone": "Unknown", "intent": "Unknown"}
    

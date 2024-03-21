import json
import re
import os
from random_response import random_string

class ChatBot:
    def __init__(self):
        # Loading JSON data
        self.response_data = self.load_json("bot.json")
        self.random_string = random_string()

    def load_json(self, file):
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        file_path = os.path.join(static_dir, file)

        with open(file_path) as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)

    def get_response(self, input_string):
        # Split the user's input into a list of lowercase words
        user_words = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        response_rankings = []

        # Check all the responses in the loaded JSON data file
        for response in self.response_data:
            word_match_score = 0
            required_score = 0
            required_words = response["required_words"]

            # Check if there are any required words in the user's input
            if required_words:
                for word in user_words:
                    if word in required_words:
                        required_score += 1

            # The number of required words should match the required score
            if required_score == len(required_words):
                # Checking each word the user has typed
                for word in user_words:
                    # If the word is in the response, it adds it to the response score
                    if word in response["user_input"]:
                        word_match_score += 1

            # Adding the score to a list
            response_rankings.append(word_match_score)

        # Finding the best response and return it if they're not all 0
        best_response = max(response_rankings)
        response_index = response_rankings.index(best_response)

        # Check if input is empty
        if input_string == "":
            return "Please type something so we can chat :("

        # If there is no good response, return a random one.
        if best_response != 0:
            return self.response_data[response_index]["bot_response"]

        return random_string()

if __name__ == "__main__":
    chat_bot = ChatBot()

    while True:
        user_input = input("You: ")
        print("Bot:", chat_bot.get_response(user_input))

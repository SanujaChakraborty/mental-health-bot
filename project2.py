# import random

import pandas as pd
df = pd.read_csv('DASS-21 - Form responses 1.csv')
# Drop Timestamp
df = df.drop(columns=['Timestamp'])

# Melt the DataFrame to turn columns into rows
melted = df.melt(var_name='Question', value_name='Response')

# Save cleaned CSV
melted.to_csv('cleaned_data.csv', index=False)

mental_health_data = pd.read_csv('cleaned_data.csv')

# Mapping 0,1,2,3 to mental health sentences
rating_messages = {
    0: "You seem to be doing fine. Keep it up! 🌟",
    1: "Mild feelings detected. Stay positive! 🌼",
    2: "Moderate issues. Take some rest and self-care. 💆",
    3: "Severe feelings. It's good to talk to someone you trust. ❤️"
}


from fuzzywuzzy import fuzz

def get_mental_health_response(user_query):
    best_score = 0
    best_response = None

    for index, row in mental_health_data.iterrows():
        score = fuzz.partial_ratio(user_query.lower(), row['Question'].lower())
        if score > best_score:
            best_score = score
            best_response = row['Response']

    if best_score > 60:  # You can adjust threshold
        # Convert the number to a nice sentence
        try:
            best_response = int(best_response)  # Make sure it's int
            return rating_messages.get(best_response, "Thanks for sharing your feelings.") 
        except:
            return "Thanks for sharing your feelings."
    else:
        return "Sorry, I couldn't understand your question clearly."


# Chat function
def mental_health_chat():
    print("Mental Health Bot: Hi! Ask me any mental health (DASS-21) question. (Type 'exit' to end)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Mental Health Bot: Stay positive! Goodbye.")
            break
        response = get_mental_health_response(user_input)
        print("Mental Health Bot:", response)


# Run
if __name__ == "__main__":
    mental_health_chat()
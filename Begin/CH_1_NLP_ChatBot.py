#$ pip install TextBlob
#$ NLP_ChatBot.py

#import TextBlob class from textblob module
from textblob import TextBlob

# Define intents dictionary and their corresponding responses based on keywords
intents = {
    'hours':{
        'keywords':['hours','open','close']
        'response': "We are open from 9am to 5pm, Mon - Fri."
    }
    'return':{
        'keywords':['refund','money back','return']
        'response': "I'd be happy to help you with the return process, let me transfer you to a live agent."
    }
}

def get_response(message):    
    # Convert the message to lowercase for consistent keyword matching
    message = message.lower()
    
    # Check if the message contains any keywords associated with defined intents
    if any(word in mesage for word in intent_data['keywords']):
        return intent_data['response']
    
    # Analyze the sentiment of the message using TextBlob
        sentiment = TextBlob(message).sentiment.polarity
        
    # Return a response based on the sentiment score
    return("That's great to hear!") if sentiment > 0 else
            "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
            "I see.  Can you tell me more about that?")

def chat():            
    # Greet the user and prompt for input
    print("Chatbot: Hi, how can I help you today?")
    # Continuously prompt the user for input until they choose to exit
    while (user_message := input("You: ").strip().lower()) not in ['exit','quit','bye']:
        print(f"\nChatbot: {get_response(user_message)}")
    # Thank the user for chatting when they exit
    print("Chatbot: Thanks for chatting.")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed

#Rule Based Chatbot
#Mohammad Zeeshan Mufti
#Internship Program AI At Decode Labs

print('\n',"Chatbot has started 🤖...")
print("Welcome to the Rule-Based Chatbot Created by Mohammad Zeeshan Mufti! Type 'exit' to quit.")
print("You can try saying things like 'hi', 'how are you', 'what is your name', or 'bye'.")

user_input = input("You: ") #Asks for user input
while user_input.lower() != 'exit': #Loop continues until user types 'exit'
    if user_input.lower() == 'exit': #If user types 'exit', chatbot says goodbye and breaks the loop
        print("Chatbot: Goodbye!")
        break
    if 'hi' in user_input.lower() or 'hello' in user_input.lower() or 'hey' in user_input.lower():
        print("Chatbot: Hello! How can I assist you today?")
    elif 'how are you' in user_input.lower():
        print("Chatbot: I am good, Thank you! How about you?")
    elif 'what is your name' in user_input.lower():

        print("ChatBot: I am a rule based chatbot created by Mohammad Zeeshan Mufti.")
    elif  "what is ai" in user_input.lower():
        print("Chatbot: Artificial Intelligence enables machines to mimic human intelligence.")

    elif 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
        print("Chatbot: Goodbye! See you later!")
        exit()
    else:
        print("Chatbot, I'm Sorry, I don't understand that.") 
        
    
    user_input = input("You: ") #Asks for user input again after responding to the previous input


















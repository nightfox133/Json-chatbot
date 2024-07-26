import json
import os
import datetime
import random

###
"""notes: 

"""
###

#File path for mem
file = r'C:\Users\marco\.vscode\python\projects\columbia\assingments\json\project\history.json'

#load mem from JSON file
def load():
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    else:
        return []

#save conversation history to JSON file
def save(conversation):
    with open(file, 'w') as f:
        json.dump(conversation, f, indent=4)
def last(b): #store last 
    return b
#response when promped with user input
def respond(inp, conversation):
    response = ""
    inp = inp.lower()
    # Check if the user input matches any previous input in the conversation history
    for entry in conversation:
        if inp in ['tell me a joke', 'tell me something', 'tell me a fact']:
            if 'joke' in inp:
                   jokes = ['j1', 'j2', 'j3']
                   r = jokes[random.randint(0,2)]
                   if entry['user_input'].lower() == r:
                       response = entry['bot_response']
                       break
            else:
                   facts = ['f1', 'f2', 'f3']
                   r = facts[random.randint(0,2)]
                   if entry['user_input'].lower() == r:
                       response = entry['bot_response']
                       break
        if entry['user_input'].lower() == inp:
            response = entry['bot_response']
            break
    
    if response == "":
        if 'what time' in inp or 'current time' in inp:
            now = datetime.datetime.now()
            response = f"The current time is {now.strftime('%H:%M')}."
        elif 'what date' in inp or 'the date' in inp:
            now = datetime.datetime.now()
            response = f"The current date is {now.strftime('%d/%m/%Y')}."
        else:
            response = input('Chatbot: this is a new question. how should i respond? ')
            if not response == '':
                #save to json
                conversation.append({'user_input': inp, 'bot_response': response}) 
                save(conversation)
                print("Chatbot: Thanks! I'll remember that.")

    return response

#extract user name from input
def extract_name(user_input, b):
    if b:
        if not 'how are you' in b:
            if 'my name is' in user_input.lower():
                return user_input.split('my name is', 1)[1].strip()
            elif 'i am' in user_input.lower():
                return user_input.split('i am', 1)[1].strip()
            elif 'im ' in user_input.lower():
                return user_input.split('im ', 1)[1].strip()
            else:
                return None
        else:
            return None
    else:
        if 'my name is' in user_input.lower():
            return user_input.split('my name is', 1)[1].strip()
        elif 'i am' in user_input.lower():
            return user_input.split('i am', 1)[1].strip()
        elif 'im ' in user_input.lower():
            return user_input.split('im ', 1)[1].strip()
        else:
            return None
# Main code for chat
def chat():
    print("Chatbot: Hi! Ask me anything or teach me something new. Type 'quit' to exit.")
    conversation = load()
    
    ### DO NOT TOUCH!!!! TOOK WAY TOO LONG
    #updates time last ran
    count = 0
    for entry in conversation:
        if entry['user_input'] in ['opened at', 'last opened']:
            count += 1
    for i in range(count):
        if i == 0:
            tL = conversation.pop(0)
        else:
            conversation.pop(0)
    conversation.insert(0, {'user_input': 'last opened', 'bot_response': tL['bot_response']})
    t = datetime.datetime.now()
    response = f"last opened on {t.strftime('%d/%m/%Y %H:%M')}"
    conversation.insert(0, {'user_input': 'opened at', 'bot_response': response}) 
    last(t)
    save(conversation)
    ### DO NOT TOUCH!!!! TOOK WAY TOO LONG

    b = None
    user_name = None
    while True:
        inp = input("You: ").strip().lower()

        if inp in ['quit', 'bye', 'end']:
            if user_name:
                print(f"Chatbot: Goodbye {user_name}!")
            else:
                print("Chatbot: Goodbye!")
            break
        
        if not user_name:
            extracted_name = extract_name(inp, b)
            if extracted_name:
                user_name = extracted_name
                print(f"Chatbot: Hello {user_name}!")
                continue
        
        response = respond(inp, conversation)
        if response != '':
            print(f"Chatbot: {response}")
        if 'current time' in inp or 'what time' in inp:
            save(conversation)
        b = last(inp)

# Run chatbot
if __name__ == "__main__": 
    chat()
    

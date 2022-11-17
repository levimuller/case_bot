#Start by importing the random library to choose random responses when more than one response is available.
import random as random

#Ask for the user's name and greet them.
print("CASE_BOT: Hello. What do you want me to call you?")
user_name = input()
print("CASE_BOT: Hello {0}. What would you like to talk about?".format(user_name))
bot_template = "CASE_BOT : {0}"
user_template = user_name + " : {0}"

#Create some variables. These are useful if the answer may change, like in the case of mood.
name = "Case Bot"
mood = "Excited"
band = "U2"
hometown = "Algona, Iowa"
live = "Orlando, Florida"
color = "Blue"


#These are the questions and responses that are available to the user. They can be greatly expanded.
responses = {
    "what's your name?": [
        "I am called {0}".format(name),
        "My name is {0}".format(name),
        "They call me {0}".format(name)],
 
    "where are you from?": [
        "I am from {0}".format(hometown),
        "I grew up in {0}".format(hometown),
        "My childhood was spent in {0}".format(hometown)],
    
    "what's your favorite band?": [
        "I like to listen to {0}".format(band),
        "My favorite is {0}".format(band),
        "Since highschool, I have liked {0}".format(band)],
    
    "are you a robot?": [
        "What do you think?",
        "Maybe I am. How would you know?",
        "I am a chatbot created by Muller Industries"],
    
    "how are you?": [
        "I am feeling {0}".format(mood),
        "I am {0}. How are you?".format(mood),
        "{0}. Yourself?".format(mood)],

    "where do you live?": [
        "I live in {0}".format(live),
        "I am living in {0}.".format(live),
        "{0}.".format(live)],

    "what is your favorite color?": [
        "My favorite color is {0}".format(color),
        "Mostly, I like {0}".format(color),
        "{0} is my color of choice".format(color)],
 
 #This is used when there is a blank entry sent from the user.
    "": [
        "Hello! Anyone home?",
        "Are you still there?",
        "Silence is golden, but this is creeping me out"],

#This is used when a question without an answer is asked.
    "default": [
        "Let me get back to you on that one."] }

#This is a function to send a random respose, if one is avaliable.
def respond(message):
    
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    
    return bot_message

#This checks for related text, so the user doesn't need to know the exact phrasing of the available questions.
def related(x_text):
    if "name" in x_text:
        y_text = "what's your name?"

    elif "from" in x_text:
        y_text = "where are you from?"

    elif "live" in x_text:
        y_text = "where do you live?"
                
    elif "band" in x_text:
        y_text = "what's your favorite band?"
        
    elif "robot" in x_text:
        y_text = "are you a robot?"
        
    elif "how are" in x_text:
        y_text = "how are you?"

    elif "color" in x_text:
        y_text = "what is your favorite color?"
        
    else:
        y_text = ""
        
    return y_text

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

#Ending with a call to the functions as well as a way to exit. 
while 1:
    my_input = input()
    my_input = my_input.lower()
    related_text = related(my_input)
    send_message(related_text)
    if my_input == "exit" or my_input == "stop":
    	break
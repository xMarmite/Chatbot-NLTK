from nltk.chat.util import Chat, reflections
import time
import datetime
import re
import random
import string
import json, requests
import sys
from oauth2client import client
from googleapiclient import sample_tools
count = 0
countm = 0
class ContextChat(Chat):
    def respond(self, str):
        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)    # pick a random response

                if callable(resp):
                    resp = resp(match.groups())
                
                resp = self._wildcards(resp, match) # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            response = response[:pos] + \
                self._substitute(match.group(num + 1)) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try: user_input = input(">")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.": user_input = user_input[:-1]    
                print(self.respond(user_input))

# === Your code should go here ===
questions = []
failsafe = ['quit']
defaultResponses = [
    "Please try again",
    "I'm sorry, I don't understand...",

]



def response1(answer, questions):
    if answer in questions:
        return "You've already asked me this!"
    else:
        feeling = input("I'm fine, and you?\n>")
        if 'bad' in feeling or 'not good' in feeling:
            return "That sucks."
        elif 'good' in feeling or 'fine' in feeling:
            return "That's great!"
        else:
            return "I don't understand..."

def response2(answer, questions):
    if answer in questions:
        return "You've already asked me this!"
    return "Look at the board!"

def response3(answer):
    if 'paper' in answer or 'marker' in answer or 'sharpie' in answer or 'compass' in answer or 'ruler' in answer or 'draw' in answer or 'books' in answer or 'how' in answer:
        return "They are in the drawing center"

    elif 'tape' in answer or 'scissors' in answer or 'glue' in answer:
        return "They are located on the bookshelf near Ms.Jordan's desk"
    elif 'portfolio' in answer:
        return "On the shelf labeled with your block number"
    elif 'brush' in answer or 'palette' in answer or 'painting paper' in answer or 'bowl' in answer:
        return "In the painting center"
    elif 'cloth' in answer or 'sponge' in answer or 'wash' in answer:
        return "In the labeled buckets near the sinks"
    else: 
        return "I'm not sure, ask Ms.Jordan"
def response4(answer):
    if 'brushes' in answer or 'palette' in answer or 'bowl' in answer:
        return "In the labeled buckets with soapy water"
    elif 'scrap paper' in answer:
        return "In the recycle bin (Labeled!!!!)"
    else:
        return "I'm not sure, ask Ms.Jordan"
    return None
def response6(answer):
    wednesdays = ['01-23','01-30','02-06','02-13','02-20','02-27','03-06','03-13','03-20','03-27','04-03','04-10','04-17','04-24','05-01','05-08','05-15','05-22','05-29','06-05','06-12','06-19','06-26','07-03','07-10','07-17','07-24','07-31']
    day = datetime.datetime.today()
    day = str(day)
    day = day[5:]
    day = day[:-10]
    hourmins = int(day[6:8])*60
    mins = int(day[9:])
    minstotal = mins + hourmins
    if minstotal < 510 or minstotal > 930:
        return "You shouldn't be in school right now. are you alright?"
    if day[0:5] in wednesdays:
        if minstotal > 570 and minstotal < 665:
            return "Class starts at 11:05"
        elif minstotal > 665 and minstotal < 745:
            return "Class starts at 12:25"
        elif minstotal > 745 and minstotal < 860:
            return "Class starts at 14:20"
    else:
        if minstotal > 510 and minstotal < 590:
            return "Class starts at 9:50"
        elif minstotal > 590 and minstotal < 700:
            return "Class starts at 11:40"
        elif minstotal > 700 and minstotal < 785:
            return "Class starts at 13:05"
        elif minstotal > 785 and minstotal < 860:
            return "class starts at 14:20"
    
def response7(answer):
    wednesdays = ['01-23','01-30','02-06','02-13','02-20','02-27','03-06','03-13','03-20','03-27','04-03','04-10','04-17','04-24','05-01','05-08','05-15','05-22','05-29','06-05','06-12','06-19','06-26','07-03','07-10','07-17','07-24','07-31']
    day = datetime.datetime.today()
    day = str(day)
    day = day[5:]
    day = day[:-10]
    hourmins = int(day[6:8])*60
    mins = int(day[9:])
    minstotal = mins + hourmins
    if minstotal < 510 or minstotal > 930:
        return "You shouldn't be in school right now. are you alright?"
    if day[0:5] in wednesdays:
        if minstotal > 510 and minstotal < 645:
            return "Class ends at 10:45"
        elif minstotal > 665 and minstotal < 735:
            return "Class ends at 12:15"
        elif minstotal > 745 and minstotal < 815:
            return "Class ends at 1:35"
    else:
        if minstotal > 510 and minstotal < 580:
            return "Class ends at 9:50"
        elif minstotal > 590 and minstotal < 660:
            return "Class ends at 11:00"
        elif minstotal > 700 and minstotal < 770:
            return "Class ends at 12:50"
        elif minstotal > 785 and minstotal < 855:
            return "Class ends at 14:15"
        elif minstotal > 860 and minstotal < 930:
            return "Class ends at 3:30"
def response8(answer, questions):
    if answer in questions:
        return "You've already asked me this!"
    return "You're supposed to be working."
def response10(answer):
    music = input("Will you work while you listen to music?\n>")
    if 'ok' in str(music.lower()) or 'sure' in str(music.lower()) or 'yes' in str(music.lower()):
        return "You may listen to music!"
    elif 'no' in str(music.lower()) or 'nah' in str(music.lower()):
        return "Then you may not listen to music."
    else: 
        print("Please give me an answer that makes sense.")
        response10(answer)
def response11(answer, questions):
    if answer in questions:
        print("I already gave you permission!")
    else:
        if 'can' in answer:
            print("I don't know, can you?")
            room = input(">")
            if 'yes' in room or 'may' in room or 'can' in room:
                return "Of course you may!"
        elif 'may' in answer:
            return "Of course you may!"
def response12(answer, name2):
    if name2 == name:
        return "I know that!"
    else:
        return "That's not your name..."
def default(answer, questions):
    if 'quit' not in answer:
        questions.append(answer)
        return random.choice(default)
    else:
        return "See you again!"

def name():
    name = input("First, please tell me your name!\n>")
    return name
    
pairs = [
    [
        r'How are you?',
        [lambda matches: response1(matches, questions)]
    ],
    [
        r'(what)(.*)(we) (gonna do|going to do|do) (today|today?)',
        [lambda matches: response2(matches, questions)]
    ],
    [
        r'(where) (can|do|is)(.*)',
        [lambda matches: response3(matches)]
    ],
    [
        r'(where) (can|do|should)(.*)',
        [lambda matches: response4(matches)]
    ],
    [
        r'(what time|when) (does) (class) (start?)',
        [lambda matches: response6(matches)]
    ],
    [
        r'(what time|when) (does|is) (class) (end|over)',
        [lambda matches: response7(matches)]
    ],
    [
        r'(what) (am|are) (i|we) (supposed|should) (do?|to do?)',
        [lambda matches: response8(matches, questions)]
    ],
    [
        r'(can|may) (i|we) (listen) (to) (music?|spotify?)',
        [lambda matches: response10(matches)]
    ],
    [
        r'(can|may) (i|we)(.*)(the) (toilet?|bathroom?)',
        [lambda matches: response11(matches, questions)]
    ],
    [
        r'(My name is|I am)(.*)',
        [lambda matches: response12(matches, name)]

    ],
    [
        r'(.*)',
        #Max W - find default answers (appropriate ones)
        [lambda matches: default(matches, questions)]
    ]
]
if __name__ == "__main__":
    print("Hi! This is a bot that is supposed to help you with art n stuff...")
    name = name()
    print("Please ask me for help if you have any questions,",name)
    chat = ContextChat(pairs, reflections)
    chat.converse()
    for item in questions:
        item = str(item)
        if item[2:-3] == 'quit':
            placeholder = True
        else:
            print(item[2:-3])
print(questions)

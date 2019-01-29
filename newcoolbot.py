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
default = [
    "Please try again",
    "I'm sorry, I don't understand...",
    "",
    "",
]



def response1(answer, count):
    if count > 0:
        return "You've already asked me this!"
    else:
        feeling = input("I'm fine, and you?\n>")
        if 'bad' in feeling or 'not good' in feeling:
            return "That sucks."
        elif 'good' in feeling or 'fine' in feeling:
            return "That's great!"
        else:
            return "I don't understand..."

def response2(answer):
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
    if 'brushes' in response3 or 'palette' in response3 or 'bowl' in response3
        return "In the labeled buckets with soapy water"
    elif 'scrap paper' in response3
        return "In the recycle bin (Labeled!!!!)"
    else:
        return "I'm not sure, ask Ms.Jordan"

def response5(answer):
    day = datetime.datetime.today()
    day = str(day)
    day = day[0:-10]
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')
    try:
     page_token = None
     while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
          print(event['summary'])
        page_token = events.get('nextPageToken')
        if not page_token:
          break
    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')
    if __name__ == '__main__':
    response5(sys.argv)
def response6(answer):
    class1Start = 510
    class1End = 580
    class2Start = 590
    class2End = 660
    class3Start = 700
    class3End = 770
    class4Start = 785
    class4End = 855
    class5Start = 860
    class5End = 930
    lunchStart = 660
    lunchEnd = 700
    wedClass1Start = 570
    wedClass1End = 645
    wedClass2Start = 665
    wedClass2End = 735
    wedClass3Start = 745
    wedClass3End = 815
    wedClass4Start = 860
    wedClass4End = 930
    wedLunchStart = 815
    wedLunchEnd = 860
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
    class1End = 580
    class2End = 660
    class3End = 770
    class4End = 855
    class5End = 930
    lunchEnd = 700
    wedClass1End = 645
    wedClass2End = 735
    wedClass3End = 815
    wedClass4End = 930
    wedLunchEnd = 860
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
        if minstotal > 510 and minstotal < 590:
            return "Class starts at 9:50"
        elif minstotal > 590 and minstotal < 700:
            return "Class starts at 11:40"
        elif minstotal > 700 and minstotal < 785:
            return "Class starts at 13:05"
        elif minstotal > 785 and minstotal < 860:
            return "class starts at 14:20"
def response8(answer):
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
def response11(answer):
    if count > 1:
        print("I already gave you permission!")
    else:
        if 'can' in answer:
            print("I don't know, can you?")
            room = input(">")
            if 'yes' in room or 'may' in room or 'can' in room:
                return "Of course you may!"
        elif 'may' in answer:
            return "Of course you may!"
def default(answer):
        unanswered.append(answer)
    if 'quit' not in answer:
        unanswered.append(answer)
        return random.choice(default)
    else:
        return "See you again!"

def name():
    name = input("First, please tell me your name!\n>")
    return name
    
pairs = [
    [
        r'How are you?',
        [lambda matches: response1(matches, count),count:=1]
    ],
    [
        r'(what)(.*)(we) (gonna do|going to do|do) (today|today?)',
        [lambda matches: response2(matches)]
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
        r'(what|which) (block)(.*)(next)',
        #working on api
       [lambda matches: response5(matches)]
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
        [lambda matches: response8(matches)]
    ],
    [
        r'(can|may) (i|we) (listen) (to) (music?|spotify?)',
        [lambda matches: response10(matches)]
    ],
    [
        r'(can|may) (i|we)(.*)(the) (toilet?|bathroom?)',
        [lambda matches: response11(matches)]
    ],
    [
        r'(.*)',
        #Max W - find default answers (appropriate ones)
        [lambda matches: default(matches), questions.append(answered)]
    ]
]
if __name__ == "__main__":
    print("Hi! This is a bot that is supposed to help you with art n stuff...")
    name = name()
    print("Please ask me for help if you have any questions,",name)
    chat = ContextChat(pairs, reflections)
    chat.converse()
    for item in unanswered:
        item = str(item)
        if item[2:-3] == 'quit':
            placeholder = True
        else:
            print(item[2:-3])
print(unanswered)

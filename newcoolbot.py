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


# === This is the extension code for the NLTK library ===
#        === You dont have to understand it ===
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
unanswered = []
failsafe = ['quit']
default = [
    "Please try again",
    "I'm sorry, I don't understand...",
    "",
    "",
]

class1Start = "8:30"
class1End = "9:40"
class2Start = "9:50"
class2End = "11:00"
class3Start = "11:40"
class3End = "12:50"
class4Start = "1:05"
class4End = "2:15"
class5Start = "2:20"
class5End = "3:30"
lunchStart = "11:00"
lunchEnd = "11:40"
wedClass1Start = "9:30"
wedClass1End = "10:45"
wedClass2Start = "11:05"
wedClass2End = "12:15"
wedClass3Start = "12:25"
wedClass3End = "1:35"
wedClass4Start = "2:20"
wedClass4End = "3:30"
wedLunchStart = "1:35"
wedLunchEnd = "2:20"

def response1(answer):
    feeling = input("I'm fine, and you?\n>")
    if 'bad' in feeling or 'not good' in feeling:
        return "That sucks."
    elif 'good' in feeling or 'fine' in feeling:
        return "That's great!"
    else:
        return "I don't understand..."

def response2(answer):
    return str(answer)

def response3(answer):
    return str(answer)

def response4(answer):
    return str(answer)

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
    return str(answer)

def response7(answer):
    time = datetime.datetime.today()
    time = str(time)
    time = time[0:-10]
    day = time[5:10]
    time = time[11:]
    if day in wednesdays:
        print("x")
    else:
        print("y")
    return str(answer)

def response8(answer):
    return str(answer)

def response9(answer):
    return str(answer)

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
        [lambda matches: response1(matches)]
    ],
    [
        r'(what)(.*)(we) (gonna do|going to do|do) (today|today?)',
        #talk and api
        [lambda matches: response2(matches)]
    ],
    [
        r'(where) (can|do|is)(.*)',
        #need to talk
        [lambda matches: response3(matches)]
    ],
    [
        r'(where) (can|do|should)(.*)',
        #need to talk
        [lambda matches: response4(matches)]
    ],
    [
        r'(what|which) (block)(.*)(next)',
        #working on api
       # [lambda matches: response5(matches)]
    ],
    [
        r'(what time|when) (does) (class) (start?)',
        # need api
        [lambda matches: response6(matches)]
    ],
    [
        r'(what time|when) (does|is) (class) (end|over)',
        [lambda matches: response7(matches)]
    ],
    [
        r'(what) (am|are) (i|we) (supposed|should) (do?|to do?)',
        #talk and api
        [lambda matches: response8(matches)]
    ],
    [
        r'(what) (is|are) (global issues?|the global issues?|a global issue?)',
        #talk
        [lambda matches: response9(matches)]
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
        [lambda matches: default(matches)]
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

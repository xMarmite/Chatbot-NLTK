from nltk.chat.util import Chat, reflections
import time
import datetime
import re
import random
import string
import json, requests

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
    block = requests.get("https://www.googleapis.com/calendar/v3/calendars/aswarsaw.org_oo26u99kpp6rlbq0ahrmnk8v14@group.calendar.google.com/events")
    parsed_json = json.loads(block.text)
    return str(parsed_json)

def response6(answer):
    return str(answer)

def response7(answer):
    return str(answer)

def response8(answer):
    return str(answer)

def response9(answer):
    return str(answer)

def response10(answer):
    return str(answer)

def response11(answer):
    return str(answer)

def default(answer):
    return str(answer)

def name():
    name = input("First, please tell me your name!\n>")
    return name
    
pairs = [
    [
        r'How are you?',
        #done
        [lambda matches: response1(matches)]
    ],
    [
        r'(what)(.*)(we)(gonna do|going to do|do)(today|today?)',
        #talk and api
        [lambda matches: response2(matches)]
    ],
    [
        r'(where)(can|do|is)(.*)',
        #need to talk
        [lambda matches: response3(matches)]
    ],
    [
        r'(where)(can|do|should)(.*)',
        #need to talk
        [lambda matches: response4(matches)]
    ],
    [
        r'(what|which) (block)(.*)(next)',
        #working on api
        [lambda matches: response5(matches)]
    ],
    [
        r'(what time|when)(does)(class)(start?)',
        # need api
        [lambda matches: response6(matches)]
    ],
    [
        r'(what time|when)(does|is)(class)(end|over)',
        #need api
        [lambda matches: response7(matches)]
    ],
    [
        r'(what)(am|are)(i|we)(supposed|should)(do?|to do?)',
        #talk and api
        [lambda matches: response8(matches)]
    ],
    [
        r'(what)(is|are)(global issues?|the global issues?|a global issue?)',
        #talk and api
        [lambda matches: response9(matches)]
    ],
    [
        r'(can|may)(i|we)(listen to)(music?|spotify)?',
        # max W
        [lambda matches: response10(matches)]
    ],
    [
        r'(can|may)(i|we)(go to|use)(the toilet|the bathroom)',
        #max W
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

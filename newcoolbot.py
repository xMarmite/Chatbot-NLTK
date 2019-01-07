from nltk.chat.util import Chat, reflections
import re
import random
import string

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
classes = [] #this should be a list of names of all students
shopping_list = []
failsafe = ['quit']

def response1():
    feeling = input("I'm fine, and you?\n>")
    if 'bad' in feeling or 'not good' in feeling:
        return "That sucks."
    elif 'good' in feeling or 'fine' in feeling:
        return "That's great!"
    else:
        return "I don't understand..."

def response2():
    return None

def response3(answer):
    return answer

def response4(answer):
    return answer

def response5():
    return None

def response6():
    return None

def response7():
    return None

def response8():
    return None

def response9():
    return None

def response10():
    return None

def response11():
    return None

def default():
    return None

def name():
    name = input("First, please tell me your name!\n>")
    return name
    
pairs = [
    [
        r'How are you?',
        [lambda matches: response1()]
    ],
    [
        r'(what)(.*)(we)(gonna do|going to do|do)(today|today?)',
        [lambda matches: response2()]
    ],
    [
        r'(where)(can|do|is)(.*)',
        [lambda matches: response3(matches)]
    ],
    [
        r'(where)(can|do|should)(.*)',
        [lambda matches: response4(matches)]
    ],
    [
        r'(what|which)(block)(is next|is next?)',
        [lambda matches: response5()]
    ],
    [
        r'(what time|when)(does)(class)(start|start?)',
        [lambda matches: response6()]
    ],
    [
        r'(what time|when)(does|is)(class)(end|over)',
        [lambda matches: response7()]
    ],
    [
        r'(what)(am|are)(i|we)(supposed|should)(do|to do|do?|to do?)',
        [lambda matches: response8()]
    ],
    [
        r'(what)(is|are)(a global issue|a global issue?|global issues|global issues?|the global issues?|the global issue)',
        [lambda matches: response9()]
    ],
    [
        r'(can|may)(i|we)(listen to)(music|music|spotify|spotify)?',
        [lambda matches: response10()]
    ],
    [
        r'(can|may)(i|we)(go to|use)(the toilet|the bathroom)',
        [lambda matches: response11()]
    ],
    [
        r'(.*)',
        [lambda matches: default()]
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

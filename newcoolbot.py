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

def responseTree(answer):
    feeling = input("I'm fine, and you?\n>")
    if 'bad' in feeling:
        return "That sucks."
    elif 'good' in feeling:
        return "That's great!"
    else:
        return "I don't understand..."

def name():
    name = input("First, please tell me your name!\n>")
    #if name in classes:
    return name
    #else:
    #    print("Unfortunately, you aren't taking art, which means that I can't help you :) Please enter a valid name!")
    #    name()

def add_to_list(item):
    '''
    This function adds an item to the shopping list.
    If given item is already in the list it returns
    False, otherwise it returns True
    '''

    if item in shopping_list:
        return False
    else:
        shopping_list.append(item)
        return True

def helper(item):
    '''
    This function adds all unanswered questions
    To a list, which is printed at the end of the session!
    '''
    if item in unanswered:
        return False
    else:
        unanswered.append(item)
        return True

pairs = [
    [
        r'(.*)(add|put)( )(.*)( )(on|to)(.*)', 
        [lambda matches: 'Noted!' if add_to_list(matches[3]) else '%3 is already on the list!']
    ],
    [
        r'What is on the list?',
        [lambda matches: ','.join(shopping_list)],
    ],
    [
        r'How are you?',
        [lambda matches: responseTree(matches)]
    ],
    [
        r'(.*)',
        [lambda matches: 'Your question has been added to a list of unanswered questions. Please be patient! :)' if helper(matches) else '%1 is already on the list of questions!']
    ],
]

if __name__ == "__main__":
    print("Hi! This is a bot that is supposed to help you with art n stuff...")
    name()
    print("Please ask me for help if you have any questions!")
    chat = ContextChat(pairs, reflections)
    chat.converse()
    for item in unanswered:
        item = str(item)
        if item[2:-3] == 'quit':
            placeholder = True
        else:
            print(item[2:-3])
#HANGMAN

#dictionary of words done
#randomly choose a word from the dictionary << 

#remove the word from the dictionary
#if the person's chosen letter is in the word:
#replace the underscore(s) with the letter
#if it is not, 1 life is subtracted from 10

import os
import random
import time

#CONSTANTS
DELAY = 0.0

#FUNCTIONS

def typing(text):
  words = text
  for char in words:
    time.sleep(DELAY)
    print(char, end='', flush=True)
    

def random_word(key):
    lives = 10
    print(f"HANGMAN\n\nyou have {lives} lives")
    #word = list(random.choice(topics_dict[key]))
    word = list("hello")
    line = []
    for index in range(0, len(word)):
        line.append("-")
    print (line)
    #^^ above is working, rest of the funciton needs work
    
    guess = input("\n>> ").lower()
    
    #find the index(es) of the guess in the string
    #then use that index to replace the - in line with guess
    #print line as a string, convert back to list and repeat
    if guess in word:
        index = word.index(guess)
        line[index] = guess
        print(line)
    
    
    #while lives > 0:
        #guess = input("\n>> ").lower()
        #if guess in word:
            #line = line.replace(line[0], guess)
            #print(line)
        #else:
            #lives -= 1
            #print(f"you have {lives} lives")

def gameplay(topic):
    os.system("clear")
    
    typing(topic)
    print("\n")
    random_word(topic)
    
#LISTS + DICTIONARIES
used_letters = []
topics_dict = {}

topics_dict["Flowers"] = ["carnation", "hyacinth", "chrysanthemum", "alstroemeria", "hibiscus", "lechenaultia", "pointsettia", "pelargonium", "wallflower","delphinium"]
topics_dict["Astronomy"] = ["constellation", "eccentricity", "ephemeris", "parallax", "supernova", "kuiper", "geostationary", "zenith", "perihelion","eclipse"]
topics_dict["Music"] = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
topics_dict["Literature"] = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
topics_dict["Animals"] = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]

#GAMEPLAY
typing("Welcome to HANGMAN.")
print("\n")

typing("\nA) Choose a Topic \nB) Random Choice?")
topic_or_random = input("\n>> ").upper()

if topic_or_random == "A":
    os.system("clear")
    time.sleep(DELAY)
    for key in topics_dict:
        print(key)
    time.sleep(DELAY)
    topic_choice = input("1-5 >> ")
    keys = list(topics_dict.keys())
    topic_choice = int(topic_choice)
    gameplay(keys[topic_choice-1])
    #print(f"{key[int(topic_choice)]}") oh cool; prints the letter at the index from topic_choice in the key
    
else:
    os.system("clear")
    topic_choice = (random.choice(topics))
    gameplay(topic_choice)

print("thanks for playing HANGMAN. Would you like to play again?")

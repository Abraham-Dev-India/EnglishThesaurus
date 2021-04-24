import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


words = json.load(open("data.json"))

def returnMeaning(dkey):
    dkey = dkey.lower()
    dkeyNoun = dkey.title()
    dkeyAcronym = dkey.upper()

    if dkey in words:
        return(words[dkey])
    
    elif dkeyNoun in words:
        return(words[dkeyNoun])
    
    elif dkeyAcronym in words: #in case user enters words like USA or NATO
        return words[dkeyAcronym]
    
    else:
        similiarList = get_close_matches(dkey,words.keys()) # returns closest matching words to {dkey}
        
        if(len(similiarList) == 0):
            return("The word doesn't exist")
        else:
            yorn = input(f"Did you mean - {similiarList[0]} ? \n(Type y for yes or n for no): ")
            yorn = yorn.lower()
            if(yorn == 'y'):
                return(words[similiarList[0]])
            elif(yorn == 'n'):
                return("The entered word doesn't exist")
            else:
                return("Invalid input!")
    
        

print("\nWELCOME TO ENGLISH THESAURUS! (type exit to quit)")
while True:
    word = input("\nEnter the word: ")
    word = word.lower()
    if(word == "exit"):
        break
    else:
        meanings = returnMeaning(word)
        if(type(meanings) == str):
            print(meanings)
            continue
        else:
            i = 1
            print("\nMEANINGS")
            print("**************************************")
            for meaning in meanings:
                print(f"\nMeaning {i}: " + meaning)
                i = i+1
                continue
        
        





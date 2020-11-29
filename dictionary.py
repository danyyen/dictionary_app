import json                              #IMPORT DICTIONARY DATA
from difflib import get_close_matches    #IMPORT LIBRARY USED TO GET CLOSE MATCHES
File = open("data.json")                 #OPEN THE DICTIONARY
dataset = json.load(File)                #READ CONTENT OF DICTIONARY DATA




def word_meaning(word):
    
    ''' 
    THIS IS A FUNCTION THAT TAKES IN WORD AND RETURNS ITS MEANING 
    
    '''
    
    word = word.lower()
    matches = get_close_matches(word, dataset.keys(), 3, 0.5)
    
    if word in dataset:
        return dataset[word]
    
    elif word.title() in dataset:
        return dataset[word.title()]
    
    elif word.upper() in dataset:
        return dataset[word.upper()]
    
    elif len(matches) > 0:
        options = input ( 'Do you mean --> {}, {}, or {} ? OR type in exact word or another word here --> '.format(matches[0], matches[1], matches[2]) )
        
        if options == matches[0]:
            return dataset[matches[0]]
        elif options == matches[1]:
            return dataset[matches[1]]
        elif options == matches[2]:
            return dataset[matches[2]]
        elif options in dataset.keys():
                return dataset[options]
        else:
            return "Word does not exist or not yet added to oxford dictionary"
            
    else:
        return 'Word does not exist OR has not been added to World Dictionary'


def gui():
    n = 1
    if type(word_list) == list:
        for meaning in word_list:
            print(n, '--> ', meaning)
            n += 1
    else:
        print(word_list)

word = input('Enter word here to get meaning: ')
word_list = word_meaning(word)
gui()
exit_or_not= input('Enter "Y" if you want to check for another word OR "N" if you want to exit: ')
exit_or_not= exit_or_not.lower()

cont= True
while cont:        
    
    if exit_or_not == 'y':
        word = input('Enter word here to get meaning: ')
        word_list = word_meaning(word)
        gui()
        exit_or_not= input('Enter "Y" if you want to check for another word OR "N" if you want to exit: ')
        exit_or_not= exit_or_not.lower()
        cont= True

    elif exit_or_not == 'n':
        print('Ok Bye')
        cont= False
        
    else:
        print('wrong input, try again')
        exit_or_not= input('Enter "Y" if you want to check for another word OR "N" if you want to exit: ')
        exit_or_not= exit_or_not.lower()
        cont= True


    

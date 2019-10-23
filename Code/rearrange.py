import random
import sys


def rearrange_words(params):
    word_list = []
    word_list = params # establishes that input will be from terminal
    random_list = [] # new list made from random picks out of word_list

    while len(random_list) < len(word_list): # stop doing this function after all words entered have been randomly returned
        random_word = random.choice(params) #choose random word from params
        if random_word not in random_list: # don't repeat a word that has already been chosen
            random_list.append(random_word) # add random words to new list


    print(" ".join(random_list)) # print the list as a concatinated string with spaces in between 


if __name__ == "__main__":
    params = sys.argv[1:]
    rearrange_words(params)





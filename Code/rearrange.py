import random
import sys


def rearrange_words(params):
    word_list = params.copy() # establishes that input will be from terminal
    random_list = [] # new list made from random picks out of word_list

    while len(word_list) > 0: # stop doing this function after all words entered have been randomly returned
        random_word = random.choice(word_list) #choose random word from params
        random_list.append(random_word) # add random words to new list
        word_list.remove(random_word)



    print(" ".join(random_list)) # print the list as a concatinated string with spaces in between


if __name__ == "__main__":
    params = sys.argv[1:]
    rearrange_words(params)





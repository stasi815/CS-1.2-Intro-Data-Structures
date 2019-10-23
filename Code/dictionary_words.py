import random
import sys

def get_random_word():
    with open('/usr/share/dict/words', 'r') as f:
        words_list = f.read().splitlines() # read text file
    random_word = random.choice(words_list) # get random word from file
    return random_word

def sentence_build(params):
    list_one = [] # list of randomly chosen words from file
    list_two = []

    count = 0

    while count < int(params):
        list_one.append(get_random_word())
        count += 1

    print(" ".join(list_one) + ".")
    # print(list_one)




if __name__ == "__main__":
    params = sys.argv[1]
    sentence_build(params)

# def rearrange_words(params):
#     word_list = []
#     word_list = params # establishes that input will be from terminal
#     random_list = [] # new list made from random picks out of word_list

#     while len(random_list) < len(word_list): # stop doing this function after all words entered have been randomly returned
#         random_word = random.choice(params) #choose random word from params
#         if random_word not in random_list: # don't repeat a word that has already been chosen
#             random_list.append(random_word) # add random words to new list


#     print(" ".join(random_list)) # print the list as a concatinated string with spaces in between


# if __name__ == "__main__":
#     params = sys.argv[1:]
#     rearrange_words(params)
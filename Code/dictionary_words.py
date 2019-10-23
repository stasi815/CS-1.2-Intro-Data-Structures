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


import random
import sys
import time

def time_it(func):
    # Made wth love by Ben <3 - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 10000) + ' ms')
        return result

    return wrapper

def load_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        words_list = f.read().splitlines() # read text file
    return words_list


@time_it
def sentence_build(words_list, params):
    list_one = [] # list of randomly chosen words from file
    count = 0

    while count < int(params):
        random_word = random.choice(words_list) # get random word from file
        list_one.append(random_word)
        count += 1

    print(" ".join(list_one) + ".")
    # print(list_one)




if __name__ == "__main__":
    params = sys.argv[1]
    words_list = load_dictionary() # only opens file once per run
    sentence_build(words_list, params)


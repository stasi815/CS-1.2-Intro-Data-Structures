import random
import sys

if __name__ == "__main__":
    word_list = []
    params = sys.argv[1:]
    word_one = str(params[0])
    word_two = str(params[1])
    word_three = str(params[2])
    word_four = str(params[3])

    word_list.append(word_one)
    word_list.append(word_two)
    word_list.append(word_three)
    word_list.append(word_four)


    random.shuffle(word_list)
    print(word_list)

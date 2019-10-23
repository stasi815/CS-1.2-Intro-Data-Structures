import random

def get_random_word():
    with open('dict_words.txt', 'r') as f:
        words_list = f.readlines()
    random_word = random.choice(words_list)
    return random_word

# def sentence_build():


if __name__ == "__main__":
    print(get_random_word())
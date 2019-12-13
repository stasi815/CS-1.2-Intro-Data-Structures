# TUTORIAL
from dictogram import Dictogram, print_histogram
from queue import Queue
import histogram_sentence
from word_frequency_analysis import load_text
import random

# def markov_histo(word_list):
#     '''Creates histogram that represents markov chain for each word in a list.'''
#     histo = {}
#     for i in range(len(word_list)-1):
#         key_word = word_list[i]
#         next_key_word = word_list[i + 1]

#         if key_word not in histo.keys():
#             key_histo = []
#             histo[key_word] = key_histo
#             # STINE TESTING Thank you Aucoeur!!

#         histo[key_word].append(next_key_word)

#     value_list = histo.items()
#     for key, value in value_list:
#         histo[key] = Dictogram(value)

#     return histo

def second_order_markov_histo(word_list):
    '''Creates histogram that represents markov chain for each word in a list.'''
    histo = {}
    for i in range(len(word_list)-1):
        key_word = word_list[i]
        next_key_word = word_list[i + 1]
        new_key = (key_word, next_key_word)

        if i+2 < len(word_list):
            next_next_key = word_list[i + 2]

            if new_key not in histo.keys():
                key_histo = []
                histo[new_key] = key_histo
            # STINE TESTING Thank you Aucoeur!!
            histo[new_key].append(next_next_key)


    value_list = histo.items()
    for key, value in value_list:
        histo[key] = Dictogram(value)

    return histo

def markov_run(markov_histos, steps):
    keys_list = markov_histos.keys() # makes list of tupled words
    first_tuple = random.choice(list(keys_list)) # picks random tuple of words to begin sentence
    markov_key = markov_histos.get(first_tuple) # dictogram values for selected tuple
    next_word = markov_key.sample() # picks weighted word from histogram of keys
    first_word = first_tuple[0]
    second_word = first_tuple[1]

    sentence = []
    sentence.append(first_word)
    sentence.append(second_word)

    next_tuple = (second_word, next_word)

    sentence.append(next_word)

    i = 2
    while i != steps:
        dict_sample = markov_histos.get(next_tuple)
        next_word2 = dict_sample.sample()
        sentence.append(next_word2)
        next_tuple = (next_tuple[1], next_word2)
        i += 1
    return sentence



def main():
    # filename = "corpus_texts/one_fish_two.txt"
    # filename = "corpus_texts/parks_and_rec.txt"
    filename = "corpus_texts/bhagavad_gita.txt"
    word_list = load_text(filename)
    markov_histos = second_order_markov_histo(word_list)
    word_one = markov_run(markov_histos)
    print(word_one)



if __name__ == '__main__':
    main()

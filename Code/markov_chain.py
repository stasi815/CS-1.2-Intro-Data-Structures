from dictogram import Dictogram, print_histogram
import histogram_sentence
from word_frequency_analysis import load_text
import random

def markov_histo(word_list):
    '''Creates histogram that represents markov chain for each word in a list.'''
    histo = {}
    for i in range(len(word_list)-1):
        key_word = word_list[i]
        next_key_word = word_list[i + 1]

        if key_word not in histo.keys():
            key_histo = []
            histo[key_word] = key_histo
            # STINE TESTING Thank you Aucoeur!!

        histo[key_word].append(next_key_word)

    value_list = histo.items()
    for key, value in value_list:
        histo[key] = Dictogram(value)

    return histo

def ho_markov_histo(word_list):
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

def markov_run(markov_histos):
    keys_list = markov_histos.keys()
    first_word = random.choice(list(keys_list))
    markov_key = markov_histos.get(first_word)
    return(markov_key.sample())


def main():
    # import sys
    # arguments = sys.argv[1:]  # Exclude script name in first argument
    # if len(arguments) >= 1:
    #     # Test histogram on given arguments
    #     print_histogram(arguments)
    # else:
    #     # Test histogram on letters in a word
    #     word = 'abracadabra'
    #     print_histogram(list(word))
    #     # Test histogram on words in a classic book title
    #     fish_text = 'one fish two fish red fish blue fish'
    #     print_histogram(fish_text.split())
    #     # Test histogram on words in a long repetitive sentence
    #     woodchuck_text = ('how much wood would a wood chuck chuck'
    #                       ' if a wood chuck could chuck wood')
    #     print_histogram(woodchuck_text.split())
    filename = "corpus_texts/one_fish_two.txt"
    word_list = load_text(filename)
    markov_histos = ho_markov_histo(word_list)
    print(markov_histos)
    print(markov_run(markov_histos))


if __name__ == '__main__':
    main()

from dictogram import Dictogram, print_histogram
import histogram_sentence
from word_frequency_analysis import load_text
import random

def key_histos(word_list):
    histo = {}


    for i in range(len(word_list)-1):
        key_word = word_list[i]
        next_key_word = word_list[i + 1]

        if key_word not in histo.keys():
            key_histo = []
            histo[key_word] = key_histo
            # STINE TESTING Thank you Aucoeur!!
            # print(histo)

        histo[key_word].append(next_key_word)
        # print(key_histo)
        # print(histo)

    value_list = histo.items()
    for key, value in value_list:
        # print(value)
        histo[key] = Dictogram(value)
        # print(histo[key])

    return histo




def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)
    pass

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
    histogram = Dictogram(word_list)
    print(histogram)
    print(word_list)
    # print(key_histos(word_list))
    print(key_histos(word_list))


if __name__ == '__main__':
    main()

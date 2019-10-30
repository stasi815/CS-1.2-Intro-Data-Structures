from word_frequency_analysis import  dict_histogram, load_text, unique_words, frequency
import random

def select_random_word(histogram):
    histo_list = [key for key in histogram]
    rand_index = random.randint(0, (len(histo_list)-1))
    random_word = histo_list[rand_index]

    return random_word

def word_prob(histogram):
    rand_word = select_random_word(histogram)
    word_freq = int(frequency(rand_word, histogram))
    sample_size = int(unique_words(histogram))
    selection_prob = word_freq/sample_size
    print(word_freq)
    print(rand_word)

    return selection_prob

if __name__ == "__main__":
    filename = '/Users/makeschoolloaner/dev/CS1.2/CS-1.2-Intro-Data-Structures/Code/tutorial/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    # print(histogram)
    # print(rand_word)
    print(unique_words(histogram))
    print(word_prob(histogram))
from word_frequency_analysis import dict_histogram, load_text, unique_words, frequency
from random import uniform
from fractions import Fraction

def calculate_tokens(histogram):
    """Calcultes total numnber of tokens in the histogram."""
    num_tokens = sum(histogram.values())
    return num_tokens

def word_prob_num(word, histogram):
    """Returns the selection probability value for a single word."""
    word_freq = int(frequency(word, histogram))
    sample_size = int(calculate_tokens(histogram))
    selection_prob = Fraction(word_freq, sample_size) # word_freq/sample_size

    return selection_prob

def word_prob_list(histogram):
    """Creates a list of tuples that include each word and its selection probability."""
    word_prob = []
    for word in histogram:
        word_prob.append((word_prob_num(word, histogram), word))
    return word_prob

def weighted_word(histogram):
    """Returns a random word based on how likely it is to be chosen."""
    word_prob = word_prob_list(histogram)
    total = 0

    dart = uniform(0,1)

    for item in word_prob:
        total += item[0]
        if dart <= total:
            return item[1]


# def select_random_word(histogram):
#     histo_list = [key for key in histogram]
#     rand_index = random.randint(0, (len(histo_list)-1))
#     random_word = histo_list[rand_index]

#     return random_word


if __name__ == "__main__":
    filename = 'corpus_texts/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    word_prob = word_prob_list(histogram)
    print(weighted_word(histogram))
    # print(word_prob)
    # print(histogram)
    # print("Total number of words in text: " + str(calculate_tokens(histogram)))
    # # print(unique_words(histogram))
    # print("Probability word will appear: " + str(word_prob_num(word, histogram)))

    # probability test with 1000 function calls
    # filename = '/Users/makeschoolloaner/dev/CS1.2/CS-1.2-Intro-Data-Structures/Code/tutorial/corpus_texts/one_fish_two.txt'
    # source_text = load_text(filename)
    # histogram = dict_histogram(source_text)
    # word_prob = word_prob_list(histogram)
    # tracker = {}
    # count = 0
    # while count != 1000:
    #     word = cum_prob_list(histogram)
    #     tracker[word] = tracker.get(word, 0) +1
    #     count += 1
    # print(tracker)
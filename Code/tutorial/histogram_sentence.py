from word_frequency_analysis import dict_histogram, load_text, unique_words, frequency
from random import uniform
from fractions import Fraction

# def select_random_word(histogram):
#     histo_list = [key for key in histogram]
#     rand_index = random.randint(0, (len(histo_list)-1))
#     random_word = histo_list[rand_index]

#     return random_word

def calculate_tokens(histogram):
    num_tokens = sum(histogram.values())
    return num_tokens

def word_prob_num(word, histogram):
    # rand_word = select_random_word(histogram)
    word_freq = int(frequency(word, histogram))
    sample_size = int(calculate_tokens(histogram))
    selection_prob = Fraction(word_freq, sample_size) #word_freq/sample_size
    # print("Times word is found in text: " + str(word_freq))
    # print("Random word selected: " + rand_word)

    return selection_prob

def word_prob_list(histogram):
    word_prob = []
    for word in histogram:
        word_prob.append((word_prob_num(word, histogram), word))
    return word_prob

def weighted_word(histogram):
    word_prob = word_prob_list(histogram)
    # cum_prob = []
    total = 0

    dart = uniform(0,1)

    for item in word_prob:
        total += item[0]
        if dart <= total:
            return item[1]


if __name__ == "__main__":
    filename = '/Users/makeschoolloaner/dev/CS1.2/CS-1.2-Intro-Data-Structures/Code/tutorial/corpus_texts/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    word_prob = word_prob_list(histogram)
    # print(word_prob)
    print(weighted_word(histogram))
    # print(histogram)
    # print("Total number of words in text: " + str(calculate_tokens(histogram)))
    # # print(unique_words(histogram))
    # print("Probability word will appear: " + str(word_prob_num(word, histogram)))

    # probability test
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
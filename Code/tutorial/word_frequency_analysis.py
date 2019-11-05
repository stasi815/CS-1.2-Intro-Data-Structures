def load_text(filename):
    with open(filename, 'r') as f:
        doc_text = f.read().splitlines()
        source_text = ((" ".join(doc_text)).lower()).split()
    return source_text

def dict_histogram(source_text):
    """Dictionary version of histogram"""

    histogram = {}

    for word in source_text:
        if word not in histogram:
            histogram[word] = 1 # uses "hash function" to jump straight to that key in memory
        else:
            histogram[word] += 1

    return histogram


# def tuple_histogram(source_text):
#     """List of tuples for histogram."""
#     histogram = []
#     word_frequencies = []
#     add_word = True
#     for word in source_text:
#         if word not in histogram:
#             histogram.append(word)
#             word_frequencies.append(1)
#         else:
#             word_index = histogram.index(word)
#             word_frequencies[word_index] += 1
#     tuple_list = zip(histogram, word_frequencies)
#     tuple_list = list(tuple_list)
#     return tuple_list


# def list_histogram(source_text):
#     """ Nested array histogram. Search cost in comparison to dictionary format."""
#     histogram = []
#     add_word = True
#     for word in source_text:
#         for list_item in histogram:
#             if list_item[0] == word:# have to search for a specific word that we're looking for
#                 list_item[1] += 1
#                 add_word = False
#         if add_word is True:
#             histogram.append([word, 1])
#         add_word = True

#     return histogram

def unique_words(histogram):
    num_words = len(histogram)
    return num_words

def frequency(word, histogram):
    word_freq = histogram.get(word, 'Word not in text.')
    return word_freq


if __name__ == "__main__":
    filename = 'corpus_texts/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    # histogram = list_histogram(source_text)
    print(histogram)
    print(unique_words(histogram))
    # print(frequency('cow', histogram))

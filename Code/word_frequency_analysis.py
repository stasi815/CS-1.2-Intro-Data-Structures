def load_text():
    with open('/Users/makeschoolloaner/dev/CS1.2/CS-1.2-Intro-Data-Structures/Code/parks_and_rec_test.txt', 'r') as f:
        doc_text = f.read().splitlines()
        source_text = ((" ".join(doc_text)).lower()).split()
    return source_text

def dict_histogram(source_text):

    histogram = {}

    for word in source_text:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


# def tuple_histogram(source_text):

# def list_histogram(source_text):

# def unique_words(histogram):

# def frequency(word, histogram):


if __name__ == "__main__":
    source_text = load_text()
    print(dict_histogram(source_text))
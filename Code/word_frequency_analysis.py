def load_text():
    with open('/Users/makeschoolloaner/dev/CS1.2/CS-1.2-Intro-Data-Structures/Code/parks_and_rec_test.txt', 'r') as f:
        doc_text = f.read().splitlines()
        source_text = (" ".join(doc_text)).split()
    return source_text

# def histogram(source_text):

# def unique_words(histogram):

# def frequency(word, histogram):


if __name__ == "__main__":
    source_text = load_text()
    print(source_text)
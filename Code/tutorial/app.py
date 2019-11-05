from flask import Flask, render_template
from random import randint, uniform
from Code.tutorial.word_frequency_analysis import load_text, dict_histogram
import Code.tutorial.histogram_sentence



app = Flask(__name__)

@app.route('/')
def rand_sentence_generator():
    """Returns a random sentence based on weighted word probability."""
    filename = 'corpus_texts/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    word_list = []
    count = 0
    while count < randint(5, 15):
        random_word = Code.tutorial.histogram_sentence.weighted_word(histogram)
        word_list.append(random_word)
        count += 1

    random_sentence = " ".join(word_list) + "."
    return render_template("index.html", sentence=random_sentence)
    # return f"{ random_sentence }"


if __name__ == '__main__':
    app.debug = True
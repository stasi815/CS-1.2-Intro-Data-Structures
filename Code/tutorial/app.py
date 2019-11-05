from flask import Flask, render_template
from random import randint, uniform
from word_frequency_analysis import load_text, dict_histogram
import histogram_sentence



app = Flask(__name__)

@app.route('/')
def rand_sentence_generator():
    filename = 'corpus_texts/parks_and_rec.txt'
    source_text = load_text(filename)
    histogram = dict_histogram(source_text)
    word_prob = histogram_sentence.word_prob_list(histogram)

    word_list = []
    count = 0
    while count < randint(5, 15):
        random_word = histogram_sentence.weighted_word(histogram)
        word_list.append(random_word)
        count += 1

    random_sentence = " ".join(word_list) + "."
    return render_template("index.html", string=random_sentence)
    # return f"{ random_sentence }"


if __name__ == '__main__':
    app.debug = True
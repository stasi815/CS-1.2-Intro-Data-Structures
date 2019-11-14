from flask import Flask, render_template
from random import randint, uniform
from Code.tutorial.word_frequency_analysis import load_text, dict_histogram
# import Code.tutorial.histogram_sentence
from Code.tutorial.markov_chain import markov_histo, markov_run



app = Flask(__name__)

@app.route('/')
def rand_sentence_generator():
    """Returns a random sentence based on weighted word probability."""
    filename = 'Code/tutorial/corpus_texts/parks_and_rec.txt'
    word_list = Code.tutorial.word_frequency_analysis.load_text(filename)
    markov_histos = Code.tutorial.markov_chain.markov_histo(word_list)

    word_list = []
    count = 0
    while count < randint(5, 15):
        random_word = Code.tutorial.markov_chain.markov_run(markov_histos)

        word_list.append(random_word)
        count += 1


    random_sentence = " ".join(word_list).capitalize() + "."
    return render_template("index.html", sentence=random_sentence)
    # return f"{ random_sentence }"


if __name__ == '__main__':
    app.debug = True
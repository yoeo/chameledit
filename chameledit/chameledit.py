from flask import Flask, render_template, request, jsonify

from guesslang import Guess


app = Flask(__name__)
app.config.update(dict(DEBUG=True, SECRET_KEY='development key'))

guess = Guess()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/language-name', methods=['POST'])
def language():
    source_code = request.form['code']
    print(source_code)
    return guess.language_name(source_code)


def main():
    app.run()

from flask import Flask, request
from .goodreads import get_random_book_from_shelf

app = Flask(__name__)


@app.route('/')
def index():
    return """
    Hello world
    """

@app.route('/lol')
def lol():
    text = request.args.get('text')
    return f'lol {text}'

@app.route('/slack', methods=['POST'])
def slack():
    text = request.form.get('text')
    return f'lol {text}'

# Will take a random book from your to-read list
@app.route('/random_book', methods=['POST'])
def random_book():
    try:
        return get_random_book_from_shelf()
    except Exception as err:
        print(err)
        return "Failed to get random book from shelf."

if __name__ == '__main__':
    app.run()
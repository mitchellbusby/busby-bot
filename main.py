from flask import Flask, request

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

@app.route('/random_book', methods=['POST'])
def random_book():
    return f'The Fault In Our Stars!'

if __name__ == '__main__':
    app.run()
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

if __name__ == '__main__':
    app.run()
from flask import Flask, request
import frontends

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

# Register blueprints
app.register_blueprint(frontends.slack_frontend.flask_blueprint, url_prefix='/slack')

if __name__ == '__main__':
    app.run()
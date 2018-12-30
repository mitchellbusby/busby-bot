import os
import requests
from flask import Blueprint, request
import traceback

from goodreads import get_random_book_from_shelf

SLACK_BEARER_TOKEN = os.environ.get('SLACK_BEARER_TOKEN')

def send_message(text, event_type, channel):
  '''Send a message of a particular type to a slack channel.'''
  if text:
    json_response = {'type': event_type, 'text': text, 'channel': channel}
    headers = {
      'Authorization': f'Bearer {SLACK_BEARER_TOKEN}',
      'Content-Type': 'application/json',
    }
    requests.post('https://slack.com/api/chat.postMessage', json=json_response, headers=headers)

flask_blueprint = Blueprint('slack_frontend', __name__)

@flask_blueprint.route('/bot', methods=['GET', 'POST'])
def slack_bot():
    # TODO: verification
    if request.json['type'] == 'url_verification':
        return request.json['challenge'] 

    # TODO: parse and filter and delegate responses
    event_type = request.json['event']['type']
    channel = request.json['event']['channel']

    def reply(text):
      '''A reply is just a message back to the channel that messaged us.'''
      return send_message(text, event_type, channel)

    reply('gudday')

    return ''


@flask_blueprint.route('/lol', methods=['POST'])
def lol():
    text = request.form.get('text')
    return f'lol {text}'

# Will take a random book from your to-read list
@flask_blueprint.route('/random_book', methods=['POST'])
def random_book():
    try:
        return get_random_book_from_shelf()
    except Exception:
        traceback.print_exc()
        return "Failed to get random book from shelf."

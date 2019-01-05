import os
import requests
from flask import Blueprint, request
from functools import lru_cache
import traceback
from bot import handle_message
from goodreads import get_random_book_from_shelf

SLACK_BEARER_TOKEN = os.environ.get('SLACK_BEARER_TOKEN')

@lru_cache()
def get_bot_username():
  '''Retrieve the user information of the bot and return it. cached.'''
  headers = {
    'Authorization': f'Bearer {SLACK_BEARER_TOKEN}',
    'Content-Type': 'application/json',
  }
  body = {
      'token': SLACK_BEARER_TOKEN,
    }
  response = requests.post('https://slack.com/api/auth.test', json=body, headers=headers).json()
  print(response)
  if response['ok']:
    # use user_id to get the bot id - helpful to test if has been mentioned if
    # more than the app_mention event is subscribed to
    # return response['user_id']
    return response['user']
  else:
    raise RuntimeError("couldn't retrieve bot info")


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

    # Check if it's the bot's message - ignore it
    # This does not work at all!
    username = request.json['event'].get('username', '')

    # print(request.json['event'])

    if get_bot_username() == username:
        return ''

    def reply(text):
      '''A reply is just a message back to the channel that messaged us.'''
      return send_message(text, event_type, channel)

    # TODO: what field is the message?
    handle_message('', reply)

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

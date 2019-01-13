import requests

def get_nearest_emoji(query):
    url = f"https://emojibuff.appspot.com/api/q?q={query}"

    response = requests.get(url)

    blob = response.json()

    results = blob.get('results')

    if len(results) > 0:
        # Get only the first result
        name, emoji = results[0][:2]
        return emoji
    
    return 'Could not find an emoji'

if __name__ == '__main__':
    print(get_nearest_emoji('nice'))
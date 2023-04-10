import os
import requests
import base64
import time
from dotenv import load_dotenv

load_dotenv()

user_agent = 'web:product-scraper:v1 (by u/asdfasdfs)'
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')

# Encode the client ID and secret in base64 format for authentication
auth_string = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
headers = {'User-Agent': user_agent, 'Authorization': f'Basic {auth_string}'}

# We will stop requesting comments when we get to 200
MAX_RESULTS = 199
def search_comments_by_keyword(keyword):
    # Set up the API endpoint and parameters
    url = 'https://www.reddit.com/search.json'
    params = {'q': keyword, 'type': 'comment', 'limit': 100, 'sort': 'new', 'include_facets': False,}
    comments = []
    while len(comments) < MAX_RESULTS:
        # Send the request and get the response JSON data
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        comments.extend(data['data']['children'])
        # break if no more comments
        if len(data["data"]["children"]) == 0:
            break
        # update after param to query comments prior to first one
        if len(comments) < MAX_RESULTS:
            last_comment_id = comments[-1]["data"]["name"]
            params["after"] = last_comment_id
        else:
            break
        time.sleep(0.1)  # Sleep for 100ms between each loop
    return comments

# Check that comment has the keyword and some form of the verbs we are looking for
def extract_string(s, keyword, verb):
    keyword_forms = generate_verb_forms(verb.lower())
    for keyword in keyword_forms:
        start_index = s.find(keyword)
        end_index = s.find(keyword)
        if start_index != -1 and end_index != -1:
            if start_index > end_index:
                start_index, end_index = end_index, start_index
            return True
    return False

# This will generate all possible verb forms for a search term: i.e. 'trades'
def generate_verb_forms(verb_root):
    suffixes = ['s', 'ing', 'ed', 'en', 'er', 'est', 'able']
    verb_forms = [verb_root]

    for suffix in suffixes:
        if suffix == 's':
            if verb_root[-1] == 's' or verb_root[-1] == 'x' or verb_root[-1] == 'z' or (verb_root[-2:] == 'ch' or verb_root[-2:] == 'sh'):
                verb_forms.append(verb_root + 'es')
            else:
                verb_forms.append(verb_root + suffix)
        elif suffix == 'ing':
            if verb_root[-1] == 'e':
                verb_forms.append(verb_root[:-1] + suffix)
            else:
                verb_forms.append(verb_root + suffix)
        elif suffix == 'ed':
            if verb_root[-1] == 'e':
                verb_forms.append(verb_root[:-1] + suffix)
            else:
                verb_forms.append(verb_root + suffix)
        elif suffix == 'en':
            if verb_root[-1] == 'e':
                verb_forms.append(verb_root[:-1] + suffix)
            else:
                verb_forms.append(verb_root + suffix)
        elif suffix == 'er' or suffix == 'est' or suffix == 'able':
            verb_forms.append(verb_root + suffix)
    return verb_forms

def query_product(product, verbs):
    comments = search_comments_by_keyword(product)
    valid = []
    for comment in comments:
        for verb in verbs:
            if extract_string(comment['data']['selftext'], product, verb):
                valid.append(comment['data'])
                break
    
    return valid


hits = query_product('drum kits', ['sell','buy', 'trade'])
for hit in hits:
    print(hit['selftext'])

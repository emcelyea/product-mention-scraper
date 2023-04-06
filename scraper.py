import json
import praw
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = 'web:product-scraper:v1 (by u/collectorius)'
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

q='terrier' #query
sub='dogs' #subreddit
sort = "new" 
limit = 1

top_posts = reddit.subreddit(sub).search(q, sort=sort, limit=limit)

for post in top_posts:
    print(vars(post))

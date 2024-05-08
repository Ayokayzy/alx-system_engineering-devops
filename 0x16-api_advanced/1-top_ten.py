#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """
    Function Docs
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Ubuntu:0-sub.py:1.3 (by /u/Ayokayzy)'
    }
    response = requests.get('{}/r/{}/.json?sort={}&limit={}'.format(
        url, subreddit, 'top', 10),
        headers=header,
        allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)

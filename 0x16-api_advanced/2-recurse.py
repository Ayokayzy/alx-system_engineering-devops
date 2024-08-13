#!/usr/bin/python3
"""
Module Docs
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    2-recurse.py
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Ubuntu:2-recurse.py:1.3 (by /u/Ayokayzy)'
    }
    if after is None:
        after = ''
    response = requests.get(
            '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
                url, subreddit, 'hot', 30, count, after),
            headers=header,
            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if len(posts) >= 30 and response.json()['data']['after']:
            return recurse(subreddit, hot_list,
                           count + len(posts),
                           response.json()['data']['after']
                           )
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None

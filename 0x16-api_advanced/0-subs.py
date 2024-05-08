#!/usr/bin/python3
"""
0-subs.py
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number
       of subscribers (not active users, total subscribers)
       for a given subreddit.

        Args:
            subreddit
        Return:
            If an invalid subreddit is given, the function should return 0.
            returns the number of subscribers
    """

    header = {
        "User-Agent": "Ubuntu:0-sub.py:1.3 (by /u/Ayokayzy)",
        "Accept": "application/json",
    }
    base_url = "https://www.reddit.com/"
    r = requests.get(
        f"{base_url}r/{subreddit}/about/.json",
        headers=header,
        allow_redirects=False
    )
    if r.status_code == 200:
        jsonData = r.json()
        subs = jsonData['data']['subscribers']
        return subs
    else:
        return 0

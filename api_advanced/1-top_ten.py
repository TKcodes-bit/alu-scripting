#!/usr/bin/python3
"""
Fetches and prints the titles of the first 10 hot posts
of a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "HolbertonSchool"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print("None")
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")

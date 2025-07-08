#!/usr/bin/python3
"""
Reddit API: Prints the titles of the first 10 hot posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    Args:
        subreddit (str): The subreddit name to query.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.posts:v1.0 (by /u/username)"}
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

        data = response.json()
        if not data or "data" not in data:
            print("None")
            return

        posts = data["data"]["children"]
        if not posts:
            print("None")
            return

        for post in posts:
            title = post["data"]["title"]
            print(title)

    except (KeyError, ValueError, requests.exceptions.RequestException):
        print("None")
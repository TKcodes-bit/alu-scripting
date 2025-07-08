#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditAPIClient/1.0"}  # Must be custom

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return  # Do not print anything

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        return

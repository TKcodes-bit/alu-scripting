#!/usr/bin/python3
"""Fetches and prints the titles of the top 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "HolbertonSchoolProject"}
    params = {"limit": 10}

    try:
        res = requests.get(url, headers=headers,
                           params=params, allow_redirects=False)
        if res.status_code != 200:
            print("None")
            return

        posts = res.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")

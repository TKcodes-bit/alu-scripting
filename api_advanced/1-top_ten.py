#!/usr/bin/python3
"""Fetch and print the titles of the first 10 hot posts on a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "HolbertonSchool"}

    response = requests.get(
        url, headers=headers, params={"limit": 10}, allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data")
    if not data:
        print("None")
        return

    posts = data.get("children")
    if not posts:
        print("None")
        return

    for post in posts:
        print(post.get("data").get("title"))

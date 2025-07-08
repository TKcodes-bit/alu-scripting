#!/usr/bin/python3
"""Recursive function to get all hot post titles from a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list of titles of all hot articles for a subreddit.
    If the subreddit is invalid or no results found, returns None.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children and not hot_list:
            return None

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        next_after = data.get("after")
        if next_after:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list

    except Exception:
        return None

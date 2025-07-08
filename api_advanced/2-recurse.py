#!/usr/bin/python3
"""
Reddit API: Recursively retrieve all hot article titles
for a given subreddit.

This module defines the function `recurse` that connects
to Reddit and collects all hot post titles using recursion.
Returns None if subreddit is invalid or returns no posts.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively returns a list of titles of all hot articles
    for a subreddit.

    Args:
        subreddit (str): Name of subreddit to query.
        hot_list (list): List collecting titles (internally used).
        after (str): Pagination token from Reddit API.

    Returns:
        list: Titles of all hot posts, or None if invalid/no posts.
    """
    if hot_list is None:
        hot_list = []

    if not isinstance(subreddit, str) or subreddit == "":
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "HolbertonSchool"}

    try:
        response = requests.get(
            url, headers=headers, params={"after": after},
            allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children and not hot_list:
            return None

        for post in children:
            title = post.get("data", {}).get("title")
            hot_list.append(title)

        next_after = data.get("after")
        if next_after:
            return recurse(subreddit, hot_list, next_after)

        return hot_list

    except Exception:
        return None

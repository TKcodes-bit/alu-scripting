#!/usr/bin/python3
"""
Reddit API: Recursively retrieve all hot article titles for a given subreddit.

This script defines a function `recurse` that connects to the Reddit API
without authentication and collects all titles of hot posts from a specified
subreddit. It uses recursion and handles pagination via the `after` parameter.

If the subreddit is invalid or there are no results, the function returns None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list of titles of all hot articles for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list used to store retrieved titles.
        after (str): The pagination token for the next page (from Reddit API).
    
    Returns:
        list: List of post titles, or None if subreddit is invalid or empty.
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

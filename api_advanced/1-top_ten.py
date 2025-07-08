#!/usr/bin/python3
"""
Module to query Reddit API and print top 10 hot posts from a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:reddit_api:v1.0 (by /u/yourusername)'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(url,
                               headers=headers,
                               params=params,
                               allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
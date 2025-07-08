#!/usr/bin/python3
"""
Recursively counts and prints keyword occurrences in Reddit hot articles.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Queries the Reddit API recursively to count the occurrences
    of each keyword in word_list found in hot article titles.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): The list of keywords to count.
        word_count (dict): Dictionary tracking word counts (used internally).
        after (str): Token for pagination (used internally).

    Returns:
        None. Prints the sorted word counts if available.
    """
    if word_count is None:
        word_count = {}

    if not isinstance(subreddit, str):
        return

    headers = {"User-Agent": "HolbertonSchool"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "")
            words = title.lower().split()

            for word in words:
                for keyword in word_list:
                    if word == keyword.lower():
                        word_count[word] = word_count.get(word, 0) + 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, word_count, after)

        if len(word_count) == 0:
            return

        final_count = {}
        for word in word_list:
            key = word.lower()
            final_count[key] = final_count.get(key, 0) + word_count.get(key, 0)

        sorted_words = sorted(
            [(k, v) for k, v in final_count.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_words:
            print("{}: {}".format(word, count))

    except Exception:
        return

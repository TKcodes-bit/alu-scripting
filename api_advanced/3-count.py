#!/usr/bin/python3
"""
Recursively counts and prints keyword occurrences in Reddit hot posts.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API, parses hot titles,
    and prints sorted keyword counts.
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
            url, headers=headers, params=params, allow_redirects=False
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
        else:
            if len(word_count) == 0:
                return

            # Combine duplicates in word_list (case-insensitive)
            final_count = {}
            for word in word_list:
                key = word.lower()
                final_count[key] = final_count.get(key, 0) + word_count.get(key, 0)

            # Sort by count desc, then alphabetically
            sorted_words = sorted(
                [(k, v) for k, v in final_count.items() if v > 0],
                key=lambda x: (-x[1], x[0])
            )

            for word, count in sorted_words:
                print("{}: {}".format(word, count))

    except Exception:
        return

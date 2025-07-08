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
    if not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                children = data.get("children", [])
                for i, child in enumerate(children):
                    if i >= 10:
                        break
                    title = child.get("data", {}).get("title")
                    if title:
                        print(title)
            else:
                print("None")
        else:
            print("None")
            
    except Exception:
        print("None")
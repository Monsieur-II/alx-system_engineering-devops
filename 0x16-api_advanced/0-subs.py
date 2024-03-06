#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Lizzie"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception:
        return 0
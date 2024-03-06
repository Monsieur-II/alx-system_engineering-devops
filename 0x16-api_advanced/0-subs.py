#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    user = {'User-Agent': 'evansayeh'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=user).json()
    try:
        return response['data']['subscribers']
    except Exception:
        return 0


if __name__ == "__main__":
    print(argv[1])
    print(number_of_subscribers(argv[1]))

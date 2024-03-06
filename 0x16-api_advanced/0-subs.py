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
    user = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=user).json()
    try:
        return response['data']['subscribers']
    except Exception:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))

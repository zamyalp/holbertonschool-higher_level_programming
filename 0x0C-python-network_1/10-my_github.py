#!/usr/bin/python3
'''
Takes your Github credentials (username and password) and uses
the Github API to display your id
'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = 'Zamyalp'
    username = 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[1]
    token = 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[2]
    headers = {'Authorization': 'token {}'.format(token)}
    req = requests.get(url, headers=headers)
    print(req.json().get('id'))

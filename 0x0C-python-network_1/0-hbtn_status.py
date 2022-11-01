#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request

url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))

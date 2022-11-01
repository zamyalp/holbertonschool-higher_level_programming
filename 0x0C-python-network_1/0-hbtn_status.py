#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request

url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as response:
    response = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
    print('\t- utf8 content: {}'.format(response.decode('utf-8'))),
    sep='\n\t')

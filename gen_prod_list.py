__author__ = 'saipc'

import requests

def get_prods(url, method, headers=None):
    if str(method).lower() == 'get':
        r = requests.get(url, None, headers=headers)
    else:
        r = requests.post(url, None,headers=headers)
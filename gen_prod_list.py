__author__ = 'saipc'

import requests
from bs4 import BeautifulSoup

def get_prods(url, method, headers=None):
    if str(method).lower() == 'get':
        r = requests.get(url, None, headers=headers)
    else:
        r = requests.post(url, None,headers=headers)

def soupify(text):
    try:
        s = BeautifulSoup(text)
    except Exception as e:
        return None
    return s
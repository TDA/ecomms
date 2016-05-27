__author__ = 'saipc'

import requests
from bs4 import BeautifulSoup

def get_prods_html(url, method, headers=None):
    if str(method).lower() == 'get':
        r = requests.get(url, None, headers=headers)
    else:
        r = requests.post(url, None,headers=headers)
    return r.text

def soupify(text):
    try:
        s = BeautifulSoup(text, 'lxml')
    except Exception as e:
        return None
    return s

if __name__ == '__main__':
    headers = {
        'Host':' www.ribbon-gifts.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':' en-US,en;q=0.5',
        'Accept-Encoding':' gzip, deflate, br',
        'Referer': 'https://www.ribbon-gifts.com/11906OPNCONSAmway/shop/all-occasions--100-ribbon--treasure/_/N-117929',
        'Cookie':' BIGipServerpool_p_www.ribbon-gifts.com_all=84781248.0.0000; JSESSIONID=B4310C8F76B0BCF8E1F9DF59C580908A; ccu=C2OzISe+nbcowSOkIxgczWBumiUo/lpK; s_fid=3F6BC5BE5EA9C971-22F26D2960C395AA; s_ppn=ahq%3Aen%3Atreasure%3Alisting; s_ppvl=ahq%253Aen%253Atreasure%253Alisting%2C49%2C49%2C734%2C1173%2C734%2C1440%2C900%2C2%2CP; s_ppv=ahq%253Aen%253Atreasure%253Alisting%2C100%2C48%2C1522%2C1173%2C433%2C1440%2C900%2C2%2CP; s_getNewRepeat=1464320558461-New; s_vnum=1464764400833%26vn%3D1; s_invisit=true; s_dslv=1464320558461; s_dslv_s=First%20Visit; s_cc=true; s_sq=%5B%5BB%5D%5D; BVImplMain%20Site=16188',
        'Connection':' keep-alive',
        'Cache-Control':' max-age=0'
    }

    url = 'https://www.ribbon-gifts.com/11906OPNCONSAmway/shop/treasure/_/N-118025'

    text = get_prods_html(url, 'get', headers)
    html = soupify(text)
    print(html)

__author__ = 'saipc'

from functions import get_prods_html

if __name__ == '__main__':
    headers = {
        'Host':' www.ribbon-gifts.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':' en-US,en;q=0.5',
        'Accept-Encoding':' gzip, deflate, br',
        'Referer': 'https://www.ribbon-gifts.com/11906OPNCONSAmway/shop/all-occasions--100-ribbon--treasure/_/N-117929',
        'Cookie':"BIGipServerpool_p_www.ribbon-gifts.com_all=84781248.0.0000; JSESSIONID=F5D9326F436D35F4EE1A792D6A62E248; ccu=C2OzISe+nbcowSOkIxgczWBumiUo/lpK; s_fid=3F6BC5BE5EA9C971-22F26D2960C395AA; s_ppvl=ahq%253Aen%253Aall%2520occasions%253Alisting%2C65%2C47%2C1039%2C1173%2C433%2C1440%2C900%2C2%2CP; s_ppv=ahq%253Aen%253Aall%2520occasions%253Alisting%2C100%2C65%2C1598%2C1173%2C433%2C1440%2C900%2C2%2CP; s_getNewRepeat=1464324095204-Repeat; s_vnum=1464764400833%26vn%3D2; s_dslv=1464324095204; s_cc=true; s_sq=maritzprod%3D%2526pid%253Dahq%25253Aen%25253Aall%252520occasions%25253Alisting%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.ribbon-gifts.com%25252F11906OPNCONSAmway%25252Fbrowse%25252Fcategory.jsp%25253FcatId%25253Dcat290019%2526ot%253DA; BVImplMain%20Site=16188; s_ppn=ahq%3Aen%3Aall%20occasions%3Alisting; s_invisit=true; s_dslv_s=Less%20than%201%20day",
        'Connection':' keep-alive',
        'Cache-Control':' max-age=0'
    }

    url = 'https://www.ribbon-gifts.com/11906OPNCONSAmway/shop/treasure/_/N-118025?No=0&Nrpp=48'

    text = get_prods_html(url, 'get', headers)
    with open('prod.html', 'w') as ht:
        ht.write(text.encode('ascii', 'ignore'))

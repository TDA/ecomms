__author__ = 'saipc'

from functions import *

def load_file(file):
    try:
        with open(file, 'r') as f:
            data = f.read()
    except Exception as e:
        return None
    return data

def generate_list(text):
    html = soupify(text)
    items_list = html.select('body > .container #itemsList li.shortDescription')

    #.shortDescription
    for item in items_list:
        print(str(item.select('div a')[0].text).lstrip())
    # print(items_list)

if __name__ == '__main__':
    text = load_file('prod.html')
    generate_list(text)
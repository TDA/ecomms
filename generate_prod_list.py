__author__ = 'saipc'

def load_file(file):
    try:
        with open(file, 'r') as f:
            data = f.read()
    except Exception as e:
        return None
    return data


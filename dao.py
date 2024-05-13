import json

def load_menu():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)

import json

DATA_FILE = 'data/expenditures.json'

def load_expenditures():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenditures(expenditures):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenditures, file)

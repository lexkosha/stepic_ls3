import json
from data import teachers


def create_json(data):
    with open('data.json', 'a', encoding='UTF-8') as f:
        for i in data:
            json.dump(i, f, ensure_ascii=False)


create_json(teachers)


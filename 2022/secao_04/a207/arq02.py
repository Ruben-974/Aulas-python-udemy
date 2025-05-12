import json
from arq01 import directory_file

print(directory_file)

with open(directory_file, encoding='UTF8') as persons:

    for person in json.load(persons):
        print(f'Name: {person["name"]} / {person["years"]}: years')
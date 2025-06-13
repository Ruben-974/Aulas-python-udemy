import json

with open('arq.json') as arq:
    print(json.load(arq, indent=4))

a190
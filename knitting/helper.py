def readList(fileName):
    with open(fileName, 'r') as file:
        file.readline()
        data = []
        for line in file.readlines():
            data.append(line.split(',')[0])
    return data[:-1]

import json

with open('/Users/adam.stepanek/Desktop/Projects/knittingScraper/knitting/product.json', 'r') as file:
    data = json.loads(file.read())
for item in data:
    print(item['url'])
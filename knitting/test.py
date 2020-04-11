import json
with open('knitting/url.json', 'r') as file:    
    file.readline()
    data = []
    for line in file.readlines():
        data.append(line.split(',')[0])
    data.remove(']')  
    for url in data:
        print(json.loads(url)['url'])
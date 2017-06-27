import requests
import json
import csv

BASE_URL = "https://api.github.com"

with open('database.csv', 'rb') as f:
    reader = csv.reader(f)
    database = list(reader)
print database

z = len(database[0])
print z

for i in range(0, z):
    request_url = (BASE_URL + '/repos/%s/%s/stats/contributors') % (database[i][0], database[i][1])
    print 'Requesting URL : %s' % request_url
    data = requests.get(request_url).json()
    with open('repo_data.json', 'w') as outfile:     # create a json data dump
        json.dump(data, outfile)

f = open('repo_data.json')
data = json.load(f)
f.close()
f = csv.writer(open('output.csv','wb+'))

for item in data:
    f.writerow([item['weeks'], item['total']] + item['author'].values())
import ao3
import json
import datetime
import csv

user = ao3.User('<user>', '<session cookie>')

bookmarks = user.bookmarks()

def convertdt(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()

output = []
work_keys = 'work_id','title','author','fandom','warnings','relationships','characters','freeforms','works','words','chapters','comments','kudos','bookmarks','hits','pubdate'

for work in bookmarks:
	output.append(dict(zip(work_keys, work)))


with open('bookmarks.json', 'w') as outfile:
	outfile.write(json.dumps(output, default=convertdt))

with open('bookmarks.csv', 'w') as f: 
    w = csv.DictWriter(f, work_keys)
    w.writeheader()
    w.writerows(output)
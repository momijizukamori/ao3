import ao3
import json
import csv
import datetime

user = ao3.User('<user>', '<session cookie>')

reading = user.reading_history()

def convertdt(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()

output = []
work_keys = 'work_id','date','numvisits','title','author','fandom','warnings','relationships','characters','freeforms','words','chapters','comments','kudos','bookmarks','hits','pubdate'

for work in reading:
	output.append(dict(zip(work_keys, work)))


with open('reading_history.json', 'w') as outfile:
	outfile.write(json.dumps(output, default=convertdt))

with open('reading_history.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, work_keys)
    w.writeheader()
    w.writerows(output)
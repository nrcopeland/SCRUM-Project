#python3

import csv
import json

csv_kwargs = {
    'dialect': 'excel',
    'doublequote': True,
    'quoting': csv.QUOTE_MINIMAL
}

inpfile = open('business.json', 'r', encoding='utf-8') 
outfile = open('business.csv', 'w', encoding='utf-8')

writer = csv.writer(outfile, **csv_kwargs, lineterminator="\n")

for line in inpfile:
    d = json.loads(line)
    writer.writerow([d['business_id'],d['name'],d['state'],d['stars'],d['review_count'],d['is_open'],d['categories']])

inpfile.close()
outfile.close()


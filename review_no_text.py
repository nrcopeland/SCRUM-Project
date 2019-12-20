#python3

import csv
import json
import re

csv_kwargs = {
    'dialect': 'excel',
    'doublequote': True,
    'quoting': csv.QUOTE_MINIMAL
}

inpfile = open('review.json', 'r', encoding='utf-8') 
outfile = open('review_no_text.csv', 'w', encoding='utf-8')

writer = csv.writer(outfile, **csv_kwargs, lineterminator="\n")

for line in inpfile:
    d = json.loads(line)
    for date in d['date'].split(','):        
      writer.writerow([d['business_id'],d['stars'],date[0:10]])

inpfile.close()
outfile.close()

import csv
import json

f = open('names.csv', 'r')
reader = csv.DictReader(f, fieldnames = ("yob", "gender", "eth", "name", "count", "rank"))
out = "[\n\t" + ",\n\t".join([json.dumps(row) for row in reader]) + "\n]"

file_out = open('new_names.json', 'w')
file_out.write(out)
file_out.close()

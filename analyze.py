"""
This program converts the downloaded json data into .csv format that can be used in Excel.
The json file needs to located in the data folder.

"""

import json
import csv
from datetime import datetime

file_name = "data/%s" % str(raw_input("Please enter the name of the file:\n"))
# file_name = "data/all2015.json"

with open(file_name) as data_file:    
    data = json.load(data_file)

raw_data = data["datapoints"]

for d in raw_data:
	dt = datetime.fromtimestamp(d[0])
	dt = dt.isoformat(" ")
	d[0] = dt

# print raw_data

d_list = list()
parameters = data["sensors"]
for i in range(0, len(raw_data)):
	d_list.append(dict())
	for j in range(0, len(d)):
		# d_list[i].append(dict())
		# d_list[i][j] = "\"%s\"" % (parameters[j]) + " : " + "\"%s\"" % (raw_data[i][j])
		d_list[i][str(parameters[j])] = str(raw_data[i][j])



# print d_list

file_save = file_name.replace(".json", ".csv")
f = csv.writer(open(file_save, "wb+"))

f.writerow(parameters)
f.writerow(data["units"])

for d in d_list:
	f.writerow(
			[d["time"], d["pm"], d["tmp"], d["hum"], d["co2"], d["voc"], d["allpollu"]]
		)




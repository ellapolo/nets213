import sys
import urllib2
import json 
import csv


def make_dict(filename): 
	truck_dict = {}
	for row in csv.DictReader(open(filename)) :
		menu = {}
		for items in row:
			if row[items] != '':
				menu[items] = row[items]
		truck_dict[row['Truck Name']] = menu
	return truck_dict

if __name__ == '__main__' : 
	data = make_dict(sys.argv[1])
	with open('data.json', 'w') as f:
		json.dump(data, f)
import sys
import urllib2
import json 
import csv


def make_dict(filename): 
	truck_dict = [line.strip().split('\t') for line in open(filename).readlines()]
	return truck_dict

if __name__ == '__main__' : 
	data = make_dict(sys.argv[1])
	with open('data.json', 'w') as f:
		json.dump(data, f)
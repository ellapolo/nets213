import sys
import urllib2
import json 
import csv


def make_json(filename): 
	data = [line.strip().split('\t') for line in open(filename).readlines()]
	return data

def make_labels(filename) : 
	for row in csv.DictReader(open(filename)) : 
		print row['url'], '\t', row['does_the_article_describe_gun_violence_required']

if __name__ == '__main__' : 

	raw_data = get_data(sys.argv[1])
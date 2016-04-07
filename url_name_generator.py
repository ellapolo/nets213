import sys
import urllib2
import requests, json 
import csv

#The purpose of this file is to create the urls and input them into a CSV file to be used for the 1st HIT on crowdflower
#(image transcription). The urls are generated using the dropbox formula to save time, and the CSV file will be the images
#'food_truck_images.csv' that is used as the input data

output = csv.writer(open('food_truck_images.csv', 'w'))

headers = ['url1', 'url2', 'url3', 'url4', 'url5', 'url6', 'url7']
output.writerow(headers)

for i in range(1,30) :
	urls = {}
	row = []
	for j in range(1,8) :
		urls[j] = "https://dl.dropboxusercontent.com/u/17481094/" + str(i) + "foodtruck_" + str(j) + ".jpg"
	row = [urls[1],urls[2],urls[3],urls[4],urls[5],urls[6],urls[7]]
	output.writerow(row)

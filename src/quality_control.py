from __future__ import division
import sys
from itertools import izip

def quality_control(filename):

    food_truck_data = open(filename, 'r')
    # columns: HIT_ID, img_url, truck_name, item1, price1, item2, price2, item3, price3.....
    truck_menus = {}
    truck_names = {}
    food_truck_data.read()
    for line in food_truck_data:
        columns = line.split(',')
        if len(columns) < 2:
            print "bad row, no HIT_ID, img_url, or truck_name"
            continue
        if len(columns) == 2:
            print "no menu data"
            continue
        truck_data = columns[:2]
        print truck_data
        id, img, truck_name = tuple(truck_data)
        print id, truck_name
        truck_menu = {}
        try:
            truck_names[id].append(truck_name)
            truck_menu = truck_menus[id]
        except KeyError:
            truck_names[id] = [truck_name]
            truck_menu = {}
        menu = columns[2:]
        menu = [x for x in menu if x]
        for item, price in pairwise(menu):
            num_price = 0.0
            try:
                num_price = float(price)
            except ValueError:
                print "Price is not a valid number"
                print price
            try:
                truck_menu[item].append(num_price)
            except KeyError:
                truck_menu[item] = [num_price]
        truck_menus[id] = truck_menu
    
    print truck_menus
    print truck_names

def pairwise(l):
    a = iter(l)
    return izip(a, a)
            
quality_control("../data/qc_input_sample.csv")

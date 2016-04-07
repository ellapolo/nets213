from __future__ import division
import sys
from itertools import izip

def quality_control(filename):

    food_truck_data = open(filename, 'r')
    # columns: HIT_ID, img_url, truck_name, item1, price1, item2, price2, item3, price3.....
    truck_menus = {}
    truck_names = {}
    for line in food_truck_data:
        columns = line.split(',')
        if len(columns) < 3:
            print "bad row, no HIT_ID, img_url, or truck_name"
            continue
        if len(columns) == 3:
            print "no menu data"
            continue
        truck_data = columns[:3]
        id, img, truck_name = tuple(truck_data)
        try:
            truck_names[id].append(truck_name)
        except KeyError:
            truck_names[id] = [truck_name]
        menu = columns[3:]
        for item, price in pairwise(l):
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
        

    def pairwise(l):
        a = iter(l)
        return izip(a, a)
            

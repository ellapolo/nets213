from __future__ import division
import sys
from collections import defaultdict
from itertools import izip

def combine_truck_info(filename):

    food_truck_data = open(filename, 'r')
    # columns: HIT_ID, img_url, truck_name, item1, price1, item2, price2, item3, price3.....
    truck_menus = {}
    truck_names = {}
    for line in food_truck_data:
        columns = line.split(',')
        if len(columns) < 2:
            print "bad row, no HIT_ID, img_url, or truck_name"
            continue
        if len(columns) == 2:
            print "no menu data"
            continue
        truck_data = columns[:2]
        id, truck_name = tuple(truck_data)
        truck_menu = {}
        try:
            truck_name_counts = truck_names[id]
            truck_menu = truck_menus[id]
        except KeyError:
            truck_name_counts = defaultdict(int)
            truck_menu = {}
        if truck_name.lower() not in [x.lower() for x in truck_name_counts.keys()]:
            truck_name_counts[truck_name] = 1
        else:
            for key in truck_name_counts:
                if key.lower() == truck_name.lower():
                    truck_name_counts[key] += 1
        truck_names[id] = truck_name_counts
        menu = columns[2:]
        # Loops through all the menu inputs of the crowdworker, and stores the information as a dict of item: [price list] 
        # TODO: normalize price names by removing punctuation and special characters and lowercasing it
        for item, price in pairwise(menu):
            if not item or not price:
                continue
            item = item.lower()
            num_price = 0.0
            try:
                num_price = float(price)
            except ValueError:
                print "Price is not a valid number", price
            try:
                truck_menu[item].append(num_price)
            except KeyError:
                truck_menu[item] = [num_price]
        truck_menus[id] = truck_menu
    return truck_menus, truck_names

def quality_control(truck_menus, truck_names):
    final_truck_names = {}
    final_truck_menus = {}
    
    # Majority vote on truck names
    for id in truck_names:
        name_counts = truck_names[id]
        max_name, max_value = "", -1
        for name in name_counts:
            if name_counts[name] > max_value:
                max_name = name
                max_value = name_counts[name]
        if max_name == "":
            continue
        final_truck_names[id] = max_name

        # Majority vote on menus and the items
        final_menu = {}
        try:
            menu = truck_menus[id]
        except KeyError:
            continue
        for item in menu:
            price = -1.0
            prices = menu[item]
            if len(prices) < 2:
                continue
            if len(prices) == 2:
                if prices[0] == prices[1] or prices[0] > 0:
                    price = prices[0]
                elif prices[1] > 0:
                    price = prices[1]
                else:
                    continue
            elif len(prices) == 3:
                for s_price in prices:
                    for n_price in prices:
                        if s_price == n_price:
                            price = s_price
                            break
                if price == -1.0:
                    if prices[0] > 0:
                        price = prices[0]
                    elif prices[1] > 0:
                        price = prices[1]
                    else:
                        prices = prices[3]
            if price == -1.0:
                price = "IDK"
            final_menu[item] = price
        final_truck_menus[id] = final_menu
#    print "NAMES: ",  final_truck_names
#    print "MENUS: ", final_truck_menus
    return final_truck_names, final_truck_menus
                
def pairwise(l):
    a = iter(l)
    return izip(a, a)
            
names, menus = combine_truck_info("../data/qc_input_sample.csv")
qc_names, qc_menus = quality_control(names, menus)


from __future__ import division
import sys
from collections import defaultdict
from itertools import izip

def combine_truck_info(filename):

    food_truck_data = open(filename, 'r')
    # columns: HIT_ID, img_url, truck_name, item1, price1, item2, price2, item3, price3.....
    truck_menus = {}
#    fill this in later with manual mapping of truck numbers to names
#    truck_names = {}
    for line in food_truck_data:
        columns = line.split(',')
        if len(columns) < 2:
            print "bad row, no HIT_ID, img_url, or truck_name"
            continue
        if len(columns) == 2:
            print "no menu data"
            continue
        id, url = tuple(columns[:2])
        truck_id = int(url.split("/")[-1].split("foodtruck")[0])
        try:
            truck_menu = truck_menus[truck_id]
        except KeyError:
            truck_menu = {}
        menu = columns[2:]
        # Loops through all the menu inputs of the crowdworker, and stores the information as a dict of item: [price list] 
        # TODO: normalize price names by removing punctuation and special characters and lowercasing it
        for item, price in pairwise(menu):
            if not item:
                continue
            item = item.lower()
            price = price.replace("$", "")
            num_price = 0.0
            try:
                num_price = float(price)
            except ValueError:
                price = "NA"
                continue
            try:
                truck_menu[item].append(num_price)
            except KeyError:
                truck_menu[item] = [num_price]
        truck_menus[truck_id] = truck_menu
    return truck_menus

def quality_control(truck_menus, filename):
    final_truck_menus = {}
    item_counts = open(filename + "_item_counts.csv", "w")
    truck_menus_file = open(filename + "_menus.csv", "w")
    # Majority vote on truck names
    for id in truck_menus:
#        truck_name = truck_names[id]
         # Majority vote on menus and the items
        final_menu = {}
        try:
            menu = truck_menus[id]
        except KeyError:
            continue
        for item in menu:
            price = -1.0
            prices = menu[item]
            if not prices:
                continue
            elif len(prices) == 1:
                price = prices[0]
            elif len(prices) == 2:
                if prices[0] == prices[1] or prices[0]:
                    price = prices[0]
                elif prices[1]:
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
                    if prices[0] != "NA":
                        price = prices[0]
                    elif prices[1] != "NA":
                        price = prices[1]
                    else:
                        prices = prices[3]
            if price == -1.0:
                price = "NA"
            final_menu[item] = price
        final_truck_menus[id] = final_menu
        item_counts.write(str(id) + "," + str(len(final_menu.keys())) + "\n")
        truck_menus_file.write(str(id) + "," + str(final_menu) + "\n")
#    print "NAMES: ",  final_truck_names
#    print "MENUS: ", final_truck_menus
    item_counts.close()
    truck_menus_file.close()
    return final_truck_menus
                
def pairwise(l):
    a = iter(l)
    return izip(a, a)
            
internal_menus = combine_truck_info("../data/cf_internal.csv")
qc_internal_menus = quality_control(internal_menus, "internal")

external_menus = combine_truck_info("../data/cf_external.csv")
qc_external_menus = quality_control(external_menus, "external")


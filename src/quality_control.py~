from __future__ import division
import sys
import collections
from collections import defaultdict
from itertools import izip
import json 

def get_truck_info():
    truck_info = {}
    truck_info_file = open("../data/truck_info.csv",  "r")
    for line in truck_info_file:
        id, name, lat, long = line.split(",")
        truck_info[int(id)] = (name, lat, long)
    return truck_info

TRUCK_INFO = get_truck_info()

def url_to_truck_id(url):
    return int(url.split("/")[-1].split("foodtruck")[0])

def truck_id_to_name(truck_id):
    return TRUCK_INFO[truck_id][0]

def qc(in_filename, out_filename):

    food_truck_data = open(in_filename, 'r')
    # columns: HIT_ID, img_url, truck_name, item1, price1, item2, price2, item3, price3.....
    truck_items = {}
    truck_prices = {}
#    fill this in later with manual mapping of truck numbers to names
#    truck_names = {}
    item_agreement = defaultdict(int)
    for line in food_truck_data:
        columns = line.split(',')
        if len(columns) < 2:
            print "bad row, no HIT_ID, img_url, or truck_name"
            continue
        if len(columns) == 2:
            print "no menu data"
            continue
        id, url = tuple(columns[:2])
        try:
            items = truck_items[url]
        except KeyError:
            items = {}
        try:
            prices = truck_prices[url]
        except KeyError:
            prices = {}

        menu = columns[2:]
        # Loops through all the menu inputs of the crowdworker, and stores the information as a dict of item: [price list] 
        # TODO: normalize price names by removing punctuation and special characters and lowercasing it
        i = 1
        for item, price in pairwise(menu):
#            print item, "\t", price
            if not item:
                continue
            item = item.lower()
            price = price.replace("$", "")
            num_price = 0.0
            try:
                num_price = float(price)
            except ValueError:
                print "Invalid price: ", price
                num_price = "NA"
            try:
                items[i].append(item)
            except KeyError:
                items[i] = [item]
            try:
                prices[i].append(num_price)
            except:
                prices[i] = [num_price]
            i += 1

        truck_items[url] = items
        truck_prices[url] = prices

    final_truck_menus = {}
    price_agreements = defaultdict(int)
    item_agreements = defaultdict(int)
    item_counts = defaultdict(int)
    truck_menus_file = open("../data/" + out_filename + "_menus.json", "w")
    agreement_file = open("../data/" + out_filename + "_agreements.csv", "w")
    # Majority vote on truck items and prices
    for url in truck_items:
        try: 
            items = truck_items[url]
            prices = truck_prices[url]
        except KeyError:
            print "don't have items or prices for this url... problematic"
            continue
        item_counts[url] = len(items.keys())
        id = url_to_truck_id(url)
        try: 
            final_menu = final_truck_menus[id]
        except KeyError:
            final_menu = {}
            # MAJORITY VOTE ON ITEMS AND PRICES
        for item_id in items:
            final_price = -1.0
            item_names = items[item_id]
            if not item_names or len(item_names) < 2:
                continue
            item_agreement, final_name = max([(item_names.count(name), name) for name in item_names])
            item_agreement -= 1
            
            item_prices = prices[item_id]
            if not prices:
                continue
            price_agreement, final_price = max([(item_prices.count(price), price) for price in item_prices if (price == "NA" or price < 20)]) 
            price_agreement -= 1
            if final_price == -1.0:
                price = "NA"
            price_agreements[url] += price_agreement
            item_agreements[url] += item_agreement
            final_menu[final_name] = final_price
            
        final_truck_menus[id] = final_menu
    # print item_agreements, "\n\n\n", item_counts
    trucks = []
    for truck_id in final_truck_menus:
        truck_info = collections.OrderedDict([("id", truck_id), ("lat", TRUCK_INFO[truck_id][1]), ("long", TRUCK_INFO[truck_id][2]),  ("name", truck_id_to_name(truck_id)), ("menu", json.dumps(final_truck_menus[truck_id]))])
        trucks.append(truck_info)
    truck_menus_file.write(json.dumps(trucks))
    truck_menus_file.close()

    for url in item_agreements:
        agreement_file.write(url + "\t" + str(item_agreements[url]/item_counts[url]) + "\t" + str(price_agreements[url]/item_counts[url]) + "\n")
    agreement_file.close()

    return final_truck_menus
                
def pairwise(l):
    a = iter(l)
    return izip(a, a)
            
internal_menus = qc("../data/cf_internal.csv", "internal")

external_menus = qc("../data/cf_external.csv", "external")



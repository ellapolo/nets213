from __future__ import division
import sys


f = open("../data/external_agreements.csv", "r")

scatter_array = [["Item Agreement", "Price Agreement"]]
item_agreement = [["Average Item Agreement", "Average Price Agreement"]]
item, price, n = 0, 0, 0
for line in f:
    url, item_agree, price_agree = line.split("\t")
    item_agree = float(item_agree)
    price_agree = float(price_agree)
    item += item_agree
    price += price_agree
    n += 1
    id  = int(url.split("/")[-1].split("foodtruck")[0])
    scatter_array.append([item_agree, price_agree])
item_agreement.append([item/n, price/n])


print scatter_array
print "\n\n\n"
print item_agreement

int(url.split("/")[-1].split("foodtruck")[0])



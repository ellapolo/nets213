import sys
import operator

f1 = open("internal_item_counts.csv", "r")
f2 = open("external_item_counts.csv", "r")
item_counts_1 = {}
item_counts_2 = {}
actual_item_counts = {1: 33, 2: 30, 3: 79, 4: 90, 5: 16, 6: 8, 7: 14, 8: 15, 9: 16, 10: 89, 11: 70, 12: 14, 13: 54, 14: 70, 15: 54, 16: 36, 17: 27, 18: 21, 19: 14, 20: 83, 21: 8, 22: 14, 23: 23, 24: 12, 25: 16, 26: 48, 27: 18, 28: 86, 29: 35 }

for line in  f1:
    truck_id, count = line.split(",")
    item_counts_1[int(truck_id)] = int(count)

for line in f2:
    truck_id, count = line.split(",")
    item_counts_2[int(truck_id)] = int(count)

outputlist = []
outputlist.append(["truck_number", "internal_item_diff", "external_item_diff"])
for truck_id, actual_item_count in sorted(actual_item_counts.items(), key=operator.itemgetter(1)):
    outputlist.append([truck_id, abs(actual_item_count - item_counts_1[truck_id]), abs(actual_item_count - item_counts_2[truck_id])])

print(outputlist)

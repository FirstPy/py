# -*- coding: utf-8 -*-
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

counts = {
    "banana": 8,
    "apple": 2,
    "orange": 2
}
def compute_bill(food):
    total = 0
    for key in food:
        if stock[key]>0:
            total += prices[key]
    return total

def compute_count(list):
    bill = 0
    for count in list:
        if list[count] > stock[count]:
            list[count] = stock[count]
        else:
            list[count] = list[count]
        bill +=prices[count] *list[count]
    return bill

print  compute_bill(prices)
print compute_count(counts)
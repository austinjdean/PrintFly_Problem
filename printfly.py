import random

def main():
    MAX = 15 # max stores we want to deal with
    TOP = 3 # you may change the top X cheapest and closest milk stores to be printed here. 3 by default.

    print # blank line as requested

    stores = populate_milk_stores(MAX) # you may substitute your own array of Milk objects here

    cheap = []
    close = []

    for store in stores:
        # sorting objects by attribute: http://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-in-python-based-on-an-attribute-of-the-objects
        cheap.append(store)
        cheap.sort(key=lambda x: x.price, reverse=False)

        close.append(store)
        close.sort(key=lambda x: x.distance, reverse=False)

    print 'Cheapest'
    for x in cheap[:TOP]:
        print x

    print;print

    print 'Closest'
    for x in close[:TOP]:
        print x

class Milk:
    def __init__(self, price, store_name, distance):
        self.price = price
        self.store_name = store_name
        self.distance = distance

    def __str__(self):
        return self.store_name + '\t$' + '%0.2f' % self.price #+ '\t' + str(self.distance)

def populate_milk_stores(MAX):
    stores = []
    i = 0

    while i < MAX:
        stores.append(gen_random_milk())
        i += 1
    return stores

def gen_random_milk():
    names = ['Wawa', 'A-Plus', 'Sheetz', '7-11', 'Sunoco', 'Exxon', 'EZ Mart', 'Hess', 'Shell']
    price =  random.uniform(1, 5) # milk is priced between $1 and $5
    name = random.choice(names)
    distance = round(random.uniform(0.5, 10), 1) # milk is between .5 and 10 miles away
    x = Milk(price, name, distance)
    return x

main()

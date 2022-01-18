allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(name, item):
    num_brought = 0

    for k, v in allGuests.items():
        num_brought += v.get(item,0)
    return num_brought

def print_total():
    print('Number of things being brought:')
    print(' - Apples         ' + str(total_brought(allGuests, 'apples')))
    print(' - Cups           ' + str(total_brought(allGuests, 'cups')))
    print(' - Cakes          ' + str(total_brought(allGuests, 'cakes')))
    print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
    print(' - Apple Pies     ' + str(total_brought(allGuests, 'apple pies')))

def main():
    print_total()

main()

